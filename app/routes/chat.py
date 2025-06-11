from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from app.models.request_model import QuestionRequest
from app.services.pdf_reader import extract_text_from_pdf
from app.services.qa_engine import QAModel
from app.utils.logger import logger
from typing import Any

app = FastAPI()

def get_qa_model():
    return QAModel()

@app.post("/ask", response_model=dict, summary="Ask a question about a PDF")
def ask_question(
    request: QuestionRequest,
    qa_model: QAModel = Depends(get_qa_model)
) -> Any:
    """
    Answers a question based on the content of a PDF.
    """
    logger.info(f"Received question: {request.question} on {request.pdf_path}")
    try:
        context = extract_text_from_pdf(request.pdf_path)
        answer = qa_model.answer(request.question, context)
        return {"answer": answer}
    except FileNotFoundError:
        logger.error(f"PDF not found: {request.pdf_path}")
        raise HTTPException(status_code=404, detail="PDF file not found")
    except ValueError as ve:
        logger.error(f"Value error: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")
