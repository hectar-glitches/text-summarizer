from transformers import pipeline

class QAModel:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def answer(self, question: str, context: str) -> str:
        result = self.qa_pipeline(question=question, context=context)
        return result["answer"]

