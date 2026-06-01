from pydantic import BaseModel, Field
from typing import List

class DetailedAnalysis(BaseModel):
    ats_score: int = Field(description="An ATS suitability score from 0 to 100 based on the job description.")
    role_fit: str = Field(description="A brief summary of how well the candidate matches the target role.")
    matched_skills: List[str] = Field(description="Key skills found in the resume that match the job description.")
    missing_skills: List[str] = Field(description="Crucial skills or keywords missing from the resume but required by the job description.")
    strengths: List[str] = Field(description="Top 3 core strengths identified in the candidate's background.")
    improvements: List[str] = Field(description="Actionable bullet points on how to improve the resume for this specific role.")