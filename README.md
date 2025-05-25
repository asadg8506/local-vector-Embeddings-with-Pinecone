# 🧠 PDF AI Embedder with Pinecone & Sentence Transformers

This project extracts text from a PDF, generates embeddings, and stores them in Pinecone for semantic search.

---

## 📂 Folder Structure

pdf-ai-pinecone/
├── main.py
├── requirements.txt
├── README.md
└── AI.pdf ← Your PDF file here

---


## 🛠️ Setup

1. Clone repo and go inside:

git clone https://github.com/asadg8506/local-vector-Embeddings-with-Pinecone.git
cd pdf-ai-pinecone


Install dependencies:

pip install -r requirements.txt
Add your Pinecone API key in main.py:


pinecone_api_key = "your-pinecone-api-key"
Place your PDF file as AI.pdf in root.

▶️ Run

python main.py
🔍 Query
Change query text in main.py:


query_text = "What is AI?"
📄 License
MIT License © 2025 Asad Ashfaq


---


This project allows you to:
- Extract text from a PDF
- Convert it into embeddings using Sentence Transformers
- Store them in Pinecone (Vector Database)
- Query for semantic answers like "What is AI?"

## Run
python main.py
📌 Requirements
Python 3.7+

Internet connection (for embeddings & Pinecone)

Pinecone account & API key

🔍 Sample Query
Change this line in main.py to ask a different question:

query_text = "What is AI?"
📄 License
MIT License © 2025 Asad Ashfaq























