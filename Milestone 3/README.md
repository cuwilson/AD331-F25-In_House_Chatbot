# Muffin Mate – Internal HR Chatbot Prototype 

This repository contains the functional prototype for **Muffin Mate**, an internal HR chatbot designed for Muffin Maniacs.  
The goal of this prototype is to demonstrate one core system interaction:  
**Retrieval-Augmented Generation (RAG) using local HR documents and a fully local LLM hosted through Ollama.**

This prototype loads company HR policy PDFs, embeds them using a local embedding model, and uses **Llama 3** (via Ollama) to answer employee questions securely and offline.

---

## 🚀 Features Demonstrated

- Local LLM (Llama 3) via Ollama  
- Local embedding model (sentence-transformers)  
- RAG (Retrieval-Augmented Generation) using `llama-index`  
- Grounded answers pulled directly from HR PDFs  
- Response verification  
- Logging of interactions  
- HR notification placeholder  
- Command-line question loop  

This satisfies the Milestone 2 flowchart and deliverable requirements.

---

## 📂 Project Structure

prototype/
│
├── prototype.py # Main HR chatbot prototype
├── rag_demo.py # Simple test version (optional)
├── requirements.txt # Python dependencies
│
├── documents/ # Place your HR PDFs here
│
└── logs/
└── interactions.json # Auto-created when prototype runs


---

##  Prerequisites

### 1. Install **Ollama**

Download from:  
https://ollama.com/download

Ollama is required to run Llama 3 locally.

---

##  Python Setup

### 2. Install Python 3.12+
Download from:  
https://www.python.org/downloads/

**Make sure to check:  
 “Add Python to PATH” during installation**

---

## Install Dependencies

In a terminal (Command Prompt or PowerShell):

```bash
pip install -r requirements.txt
```
This installs
- llama-index
- chormadb
- sentence-transformers
- docx2txt

## Pull Required Ollama Models

### 3. Pull Llama 3

`ollama pull llama3`

### 4. Pull the local embedding model

`ollama pull nomic-embed-text`

## Running the Prototype

### 5. Navigate to the project folder

`cd path/to/prototype`

### 6. Run it!

`python prototype.py`

### You can now ask questions!