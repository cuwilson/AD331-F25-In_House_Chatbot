from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load documents
documents = SimpleDirectoryReader("./documents").load_data()

# Local embedding model (fully offline)
embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Build vector index
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# Connect to Ollama
llm = Ollama(model="llama3")
query_engine = index.as_query_engine(llm=llm)

print("RAG Demo Ready. Ask an HR Question:")
while True:
    user_q = input("You: ")
    if user_q.lower() in ["exit", "quit"]:
        break
    response = query_engine.query(user_q)
    print("Answer:", response)
