# PDF QA Chatbot

An AI-powered chatbot API that can answer questions from the contents of a PDF.

## Features
- 📄 Extracts text from PDF files
- 🤖 Uses Transformers QA model (`distilbert-base-cased-distilled-squad`)
- 🚀 REST API built with FastAPI
- 🧪 Includes unit tests

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the app:
```bash
python main.py
```
3. Make a POST request to `http://localhost:8000/ask` with:
```json
{
  "question": "What is this document about?",
  "pdf_path": "./tests/sample.pdf"
}
```

## Test
```bash
pytest
```
