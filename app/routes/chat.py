from fastapi import FastAPI, HTTPException
from app.models.request_model import QuestionRequest
from app.services.pdf_reader import extract_text_from_pdf
from app.services.qa_engine import QAModel
from app.utils.logger import logger

app = FastAPI()
qa_model = QAModel()

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        logger.info(f"Received question: {request.question} on {request.pdf_path}")
        context = extract_text_from_pdf(request.pdf_path)
        answer = qa_model.answer(request.question, context)
        return {"answer": answer}
    except Exception as e:
        logger.error(f"Error answering question: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")
