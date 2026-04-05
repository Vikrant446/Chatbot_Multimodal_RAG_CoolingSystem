import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("rag_db")

def add_doc(text, emb, meta):
    collection.add(
        documents=[text],
        embeddings=[emb],
        metadatas=[meta],
        ids=[str(hash(text))]
    )

def search(emb):
    return collection.query(query_embeddings=[emb], n_results=3)