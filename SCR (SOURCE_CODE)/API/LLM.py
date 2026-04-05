def generate_answer(query, docs):
    context = " ".join(docs)
    return f"Answer:\n{context[:400]}"