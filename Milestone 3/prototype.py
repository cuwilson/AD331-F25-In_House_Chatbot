import json
import os
from datetime import datetime

# ------------------------------
# CORRECT MODULAR IMPORTS
# ------------------------------
import importlib

# --- Import VectorStoreIndex + SimpleDirectoryReader ---
vector_candidates = [
    ("llama_index.core", ["VectorStoreIndex", "SimpleDirectoryReader"]),
    ("llama_index", ["VectorStoreIndex", "SimpleDirectoryReader"]),
]

VectorStoreIndex = None
SimpleDirectoryReader = None

for module_name, attrs in vector_candidates:
    try:
        module = importlib.import_module(module_name)
        VectorStoreIndex = getattr(module, attrs[0], None)
        SimpleDirectoryReader = getattr(module, attrs[1], None)
        if VectorStoreIndex and SimpleDirectoryReader:
            break
    except ImportError:
        continue

if not VectorStoreIndex or not SimpleDirectoryReader:
    raise ImportError("Could not import VectorStoreIndex or SimpleDirectoryReader.")


# --- Import Ollama LLM ---
ollama_candidates = [
    ("llama_index.llms.ollama", "Ollama"),
    ("llama_index.core.llms.ollama", "Ollama"),
    ("llama_index.llms", "Ollama"),
    ("llama_index.core.llms", "Ollama"),
]

Ollama = None
for module_name, attr in ollama_candidates:
    try:
        module = importlib.import_module(module_name)
        Ollama = getattr(module, attr, None)
        if Ollama:
            break
    except ImportError:
        continue

if not Ollama:
    raise ImportError("Could not import Ollama from ANY known llama_index module path.")


# --- Import HuggingFaceEmbedding ---
embedding_candidates = [
    ("llama_index.embeddings.huggingface", "HuggingFaceEmbedding"),
    ("llama_index.embeddings", "HuggingFaceEmbedding"),
    ("llama_index.core.embeddings", "HuggingFaceEmbedding"),
]

HuggingFaceEmbedding = None
for module_name, attr in embedding_candidates:
    try:
        module = importlib.import_module(module_name)
        HuggingFaceEmbedding = getattr(module, attr, None)
        if HuggingFaceEmbedding:
            break
    except ImportError:
        continue

if not HuggingFaceEmbedding:
    raise ImportError("Could not import HuggingFaceEmbedding.")

print("Imported OK!")



# ------------------------------
# CONFIGURATION
# ------------------------------
DOCS_FOLDER = "./documents"
LOG_FILE = "./logs/interactions.json"
MODEL_NAME = "llama3"

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


# ------------------------------
# LOAD DOCUMENTS & BUILD INDEX
# ------------------------------
print("Loading HR documents...")
documents = SimpleDirectoryReader(DOCS_FOLDER).load_data()

print("Building vector index (local embeddings)...")

embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# ------------------------------
# CONNECT LLM (OLLAMA)
# ------------------------------
llm = Ollama(model=MODEL_NAME)

query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=3
)

print("\nSecure Internal Chatbot Prototype Ready!")
print("Ask HR questions. Type 'exit' to quit.\n")


# ------------------------------
# LOGGING
# ------------------------------
def log_interaction(user_question, answer, retrieved_context):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "question": user_question,
        "answer": str(answer),
        "retrieved_context": retrieved_context,
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([entry], f, indent=4)
    else:
        with open(LOG_FILE, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)


# ------------------------------
# HR NOTIFICATION (PLACEHOLDER)
# ------------------------------
def notify_hr(question):
    print("\n[ALERT SENT TO HR]")
    print(f"Flagged question: {question}\n")


# ------------------------------
# RESPONSE VERIFIER
# ------------------------------
def verify_response(answer, retrieved_text):
    answer_lower = str(answer).lower()
    context_lower = " ".join(retrieved_text).lower()

    if any(word in answer_lower for word in context_lower.split()[:10]):
        return True
    return False


# ------------------------------
# MAIN LOOP
# ------------------------------
while True:
    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print("\nRetrieving relevant HR sections...")
    response = query_engine.query(question)

    # Extract retrieved chunks correctly
    retrieved_chunks = [
        node.get_content() for node in response.source_nodes
    ]

    print("\nAnswer:\n", response, "\n")

    is_valid = verify_response(response, retrieved_chunks)

    # Log interaction
    log_interaction(question, response, retrieved_chunks)

    if not is_valid:
        print("⚠ The system is not confident this answer is grounded.")
        notify_hr(question)

    print("-" * 60)
