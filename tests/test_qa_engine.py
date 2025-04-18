from app.services.qa_engine import QAModel

def test_answer():
    model = QAModel()
    context = "Albert Einstein was a physicist who developed the theory of relativity."
    question = "Who developed the theory of relativity?"
    answer = model.answer(question, context)
    assert "Einstein" in answer
