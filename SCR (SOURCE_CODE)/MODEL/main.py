from fastapi import FastAPI, UploadFile
import time

from src.ingestion.parser import extract_pdf_content
from src.ingestion.chunker import chunk_text
from src.ingestion.embedder import get_embedding
from src.retrieval.vectordb import add_doc
from src.retrieval.retriever import retrieve
from src.models.llm import generate_answer
from src.models.vision import image_to_text

app = FastAPI()
start_time = time.time()
docs = 0

@app.get("/health")
def health():
    return {"status": "ok", "uptime": time.time() - start_time}

@app.post("/ingest")
async def ingest(file: UploadFile):
    global docs

    path = f"temp_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    texts, images = extract_pdf_content(path)

    for t in texts:
        chunks = chunk_text(t["content"])
        for c in chunks:
            emb = get_embedding(c)
            add_doc(c, emb, t)

    for img in images:
        text = image_to_text(img)
        emb = get_embedding(text)
        add_doc(text, emb, img)

    docs += 1
    return {"message": "done"}

@app.post("/query")
async def query(q: str):
    docs = retrieve(q)
    ans = generate_answer(q, docs)
    return {"answer": ans}