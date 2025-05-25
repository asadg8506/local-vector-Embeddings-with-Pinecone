import fitz  # PDF text extraction
from sentence_transformers import SentenceTransformer  # Free local embeddings
import pinecone  # ✅ Pinecone vector DB


# === 1️⃣ Extract Text from PDF === #
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])  
    return text

pdf_path = r"C:\Users\Asad\Desktop\AI.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
print("✅ PDF text extracted successfully!")



# === 2️⃣ Generate Embeddings === #
model = SentenceTransformer("all-MiniLM-L6-v2")  # 384-dim embedding

def get_local_embeddings(text):
    return model.encode(text).tolist()

pdf_embedding = get_local_embeddings(pdf_text)

if pdf_embedding:
    print("✅ Local Embedding Generated Successfully!")
else:
    print("❌ Failed to generate embeddings. Exiting...")
    exit()



# === 3️⃣ Initialize Pinecone === #
pc = pinecone.Pinecone(api_key="^^^^^^^^^^^^^^^^^^")

index_name = "pdf-embeddings"
embedding_dimension = 384  # Match your model output size



# === 4️⃣ Create Index if Not Exists === #
if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=embedding_dimension,
        metric="cosine",
        spec={
            "serverless": {
                "cloud": "aws",
                "region": "us-east-1"
            }
        }
    )
    print(f"✅ Index '{index_name}' created!")
else:
    print(f"ℹ️ Index '{index_name}' already exists.")



# === 5️⃣ Connect to the Index === #
index = pc.Index(index_name)



# === 6️⃣ Store Embeddings in Pinecone === #
index.upsert(vectors=[("ai_pdf", pdf_embedding)])
print("✅ Embeddings stored in Pinecone!")



# === 7️⃣ Query Pinecone for Similarity Search === #
query_text = "What is AI?"
query_embedding = get_local_embeddings(query_text)

if query_embedding:
    response = index.query(vector=query_embedding, top_k=5, include_metadata=True)
    print("🔍 Search Results:", response)
else:
    print("❌ Failed to generate query embedding!")
