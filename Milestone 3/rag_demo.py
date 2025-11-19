from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.llms import Ollama

# Load documents
documents = SimpleDirectoryReader("./documents/hr").load_data()

# Build vector index
index = VectorStoreIndex.from_documents(documents)

# Connect to Ollama
llm = Ollama(model="llama3")
query_engine = index.as_query_engine(llm=llm)

print("RAG Prototype Ready. Ask an HR Question:")
while True:
    user_q = input("You: ")
    response = query_engine.query(user_q)
    print("Answer:", response)
