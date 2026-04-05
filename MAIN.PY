from fastapi import FastAPI, UploadFile
import time

from src.ingestion.parser import extract_pdf_content
from src.ingestion.chunker import chunk_text
from src.ingestion.embedder import get_embedding
from src.retrieval.vectordb import add_to_db
from src.retrieval.retriever import retrieve
from src.models.llm import generate_answer
from src.models.vision import image_to_text

app = FastAPI()

start_time = time.time()
doc_count = 0

@app.get("/health")
def health():
    return {
        "status": "running",
        "documents": doc_count,
        "uptime": time.time() - start_time
    }

@app.post("/ingest")
async def ingest(file: UploadFile):
    global doc_count

    path = f"temp_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    text_chunks, images = extract_pdf_content(path)

    total_chunks = 0

    # Process text
    for item in text_chunks:
        chunks = chunk_text(item["content"])
        for chunk in chunks:
            emb = get_embedding(chunk)
            add_to_db(chunk, emb, item)
            total_chunks += 1

    # Process images
    for img in images:
        text = image_to_text(img["image_bytes"])
        emb = get_embedding(text)
        add_to_db(text, emb, img)
        total_chunks += 1

    doc_count += 1

    return {
        "message": "Ingestion complete",
        "chunks": total_chunks
    }

@app.post("/query")
async def query(q: str):
    docs = retrieve(q)
    answer = generate_answer(q, docs)

    return {
        "query": q,
        "answer": answer,
        "sources": docs
    }