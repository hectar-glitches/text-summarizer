from app.services.pdf_reader import extract_text_from_pdf
import os

def test_extract_text_from_sample_pdf():
    sample_pdf = os.path.join("tests", "sample.pdf")
    text = extract_text_from_pdf(sample_pdf)
    assert isinstance(text, str)
    assert len(text) > 0
