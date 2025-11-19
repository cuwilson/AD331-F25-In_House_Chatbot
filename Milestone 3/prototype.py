import json
import os
from datetime import datetime

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding




# --------------
# CONFIGURATION
# --------------

DOCS_FOLDER = "./documents"        # Folder with HR PDFs
LOG_FILE = "./logs/interactions.json" # Log storage location
MODEL_NAME = "llama3"                 # The model you pulled with Ollama

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


# --------------
# LOAD DOCUMENTS AND SET UP RAG
# --------------

print("Loading HR documents...")
documents = SimpleDirectoryReader(DOCS_FOLDER).load_data()

print("Building vector index (local embeddings)...")

# Local embedding model (no API keys needed)
embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Build vector store index using local embeddings
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# Connect Llama 3 via Ollama
llm = Ollama(model="llama3")

# Create Query Engine (retriever + LLM)
query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=3
)

print("\nMuffin Mate Prototype Ready!")
print("Ask HR-related questions. Type 'exit' to quit.\n")


# --------------
# LOGGING
# --------------

def log_interaction(user_question, answer, retrieved_context):
    """Save each interaction in a JSON log file."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "question": user_question,
        "answer": str(answer),
        "retrieved_context": retrieved_context,
    }

    # Append to JSON file
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([entry], f, indent=4)
    else:
        with open(LOG_FILE, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)


# --------------
# HR NOTIFICATION (Placeholder)
# --------------

def notify_hr(question):
    """
    Placeholder for notifying HR when the answer is incomplete or uncertain.
    In a full system, this could send an email or push message.
    """
    print("\n[ALERT SENT TO HR]")
    print(f"Flagged question: {question}\n")


# --------------
# RESPONSE VERIFIER
# --------------

def verify_response(answer, retrieved_text):
    """
    Simple check: ensure the answer references or uses retrieved text.
    """
    answer_lower = str(answer).lower()
    context_lower = " ".join(retrieved_text).lower()

    # Compare a few key words from the retrieved text
    if any(word in answer_lower for word in context_lower.split()[:10]):
        return True  # Contains meaningful overlap
    return False



# --------------
# MAIN QUESTION LOOP
# --------------

while True:
    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print("\nRetrieving relevant HR policy sections...")
    response = query_engine.query(question)

    # Extract retrieved context 
    retrieved_chunks = [
        node.node.get_content() for node in response.source_nodes
    ]

    print("\nAnswer:\n", response, "\n")

    # Verify response uses retrieved text
    is_valid = verify_response(response, retrieved_chunks)

    # Log interaction
    log_interaction(question, response, retrieved_chunks)

    # Notify HR if not grounded
    if not is_valid:
        print("⚠ The system is not fully confident this answer is grounded in policy.")
        notify_hr(question)

    print("-" * 60)
