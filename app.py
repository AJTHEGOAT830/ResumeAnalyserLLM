import streamlit as st
from analyser import extract_text_from_pdf, analyze_resume

# Page configuration
st.set_page_config(page_title="AI Resume Analyser", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyser & ATS Optimiser")
st.caption("Evaluate your resume against any job description instantly using GenAI.")

# Sidebar for Setup
with st.sidebar:
    st.header("🔑 Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.markdown("[Get a free API key here](https://aistudio.google.com/)")
    st.divider()
    st.markdown(
        "### How it works:\n1. Paste the target Job Description.\n2. Upload your PDF Resume.\n3. Get targeted, structured feedback.")

# Main Layout: Two columns for inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Target Job Description")
    job_desc = st.text_area("Paste the job posting details here...", height=250)

with col2:
    st.subheader("📤 Upload Resume")
    uploaded_file = st.file_uploader("Choose your Resume (PDF format)", type=["pdf"])

st.divider()

# Execution Button
if st.button("🚀 Analyze Resume", type="primary"):
    if not api_key:
        st.error("Please provide your Gemini API key in the sidebar.")
    elif not job_desc:
        st.error("Please paste a Job Description to match against.")
    elif not uploaded_file:
        st.error("Please upload a PDF resume.")
    else:
        with st.spinner("Analyzing candidate profile and processing metrics..."):
            try:
                # 1. Extract text from uploaded PDF
                resume_text = extract_text_from_pdf(uploaded_file)

                # 2. Get Structured AI Analysis
                analysis = analyze_resume(resume_text, job_desc, api_key)

                # 3. Render Results UI
                st.success("Analysis Complete!")

                # Metrics Display
                score_color = "green" if analysis.ats_score >= 75 else "orange" if analysis.ats_score >= 50 else "red"
                st.markdown(f"## ATS Match Score: :{score_color}[{analysis.ats_score}/100]")
                st.progress(analysis.ats_score / 100)

                st.markdown(f"### 📋 Role Fit Summary\n{analysis.role_fit}")

                # Split columns for Skills breakdown
                sk_col1, sk_col2 = st.columns(2)
                with sk_col1:
                    st.success("✅ Matched Skills")
                    for skill in analysis.matched_skills:
                        st.markdown(f"- {skill}")
                with sk_col2:
                    st.error("❌ Missing Keywords / Skills")
                    for skill in analysis.missing_skills:
                        st.markdown(f"- {skill}")

                st.divider()

                # Strengths and Improvements
                st.markdown("### 💪 Key Strengths")
                for strength in analysis.strengths:
                    st.markdown(f"⭐ {strength}")

                st.markdown("### 🛠️ Recommended Improvements")
                for imp in analysis.improvements:
                    st.markdown(f"📌 {imp}")

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")