from src.ingestion.embedder import get_embedding
from src.retrieval.vectordb import search

def retrieve(query):
    emb = get_embedding(query)
    result = search(emb)
    return result["documents"][0]