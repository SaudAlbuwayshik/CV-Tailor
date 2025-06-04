import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="CV Paraphraser (Section-Based)", layout="centered")

@st.cache_resource
def get_paraphraser():
    return pipeline("text2text-generation", model="ramsrigouthamg/t5_paraphraser")

st.title("📝 CV Section Paraphraser")

cv_section = st.text_area("Paste a section from your CV (e.g., a work experience)", height=250)
job_description = st.text_area("Paste the full Job Description", height=300)

if st.button("Paraphrase CV Section"):
    if not cv_section.strip() or not job_description.strip():
        st.warning("Please provide both your CV section and the job description.")
    else:
        with st.spinner("Paraphrasing to match job description..."):
            prompt = f"Paraphrase this CV section to match the following job description:
Job Description: {job_description}
CV Section: {cv_section}"
            model = get_paraphraser()
            result = model(prompt, max_length=512, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1)
            st.subheader("🎯 Paraphrased Output:")
            st.text_area("Updated CV Section", result[0]['generated_text'], height=300)
