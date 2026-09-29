# AI Resume Analyser & ATS Optimiser

An AI-powered web application that evaluates resumes against job descriptions, calculates an ATS match score, and delivers structured, actionable feedback using Google Gemini (`gemini-2.5-flash`) and Streamlit.

---

## Features

- **Automated PDF Parsing:** Extracts plain text from uploaded PDF resumes using `PyPDF2`.
- **Targeted ATS Scoring:** Computes a compatibility score (0–100) based on role requirements.
- **Skill Gap Breakdown:** Identifies directly matched skills alongside critical missing keywords.
- **Structured LLM Output:** Enforces strict JSON schemas using Pydantic models with the official `google-genai` SDK.
- **Actionable Critique:** Highlights candidate strengths and provides concrete resume improvement suggestions.

---

## Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Engine:** [Google Gemini API](https://ai.google.dev/) (`gemini-2.5-flash` via `google-genai`)
- **Schema Validation:** [Pydantic v2](https://docs.pydantic.dev/)
- **PDF Extraction:** [PyPDF2](https://pypi.org/project/PyPDF2/)

---

## Project Structure

```text
├── analyser.py       # PDF parsing & Gemini API integration
├── app.py            # Streamlit dashboard and UI logic
├── models.py         # Pydantic schema for structured output
├── requirements.txt  # Project dependencies
└── README.md         # Documentation
