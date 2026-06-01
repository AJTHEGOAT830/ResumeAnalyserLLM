import io
from PyPDF2 import PdfReader
from google import genai
from google.genai import types
from models import DetailedAnalysis


def extract_text_from_pdf(uploaded_file) -> str:
    """Extracts raw text from an uploaded PDF file."""
    pdf_file = io.BytesIO(uploaded_file.read())
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def analyze_resume(resume_text: str, job_description: str, api_key: str) -> DetailedAnalysis:
    """Sends the resume and JD to Gemini and forces a structured JSON response."""
    # Initialize the modern standard Google GenAI Client
    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are an expert technical recruiter and Applicant Tracking System (ATS) optimization engine.
    Analyze the following resume against the provided job description.

    JOB DESCRIPTION:
    {job_description}

    RESUME TEXT:
    {resume_text}
    """

    # Instruct the model to strictly follow our Pydantic schema
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=DetailedAnalysis,
            temperature=0.2,
        ),
    )

    # Parse the returned JSON text directly into our Pydantic model
    return DetailedAnalysis.model_validate_json(response.text)