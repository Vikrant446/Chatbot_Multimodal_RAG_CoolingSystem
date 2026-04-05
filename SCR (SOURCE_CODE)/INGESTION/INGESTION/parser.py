import fitz

def extract_pdf_content(Vikrant446/Chatbot_Multimodal_RAG_CoolingSystem/Data/Cooling _System.pdf):
    doc = fitz.open(Vikrant446/Chatbot_Multimodal_RAG_CoolingSystem/Data/Cooling _System.pdf)
    texts, images = [], []

    for page_num, page in enumerate(doc):
        texts.append({
            "content": page.get_text(),
            "page": page_num,
            "type": "text"
        })

        for img in page.get_images(full=True):
            base = doc.extract_image(img[0])
            images.append({
                "image_bytes": base["image"],
                "page": page_num,
                "type": "image"
            })

    return texts, images