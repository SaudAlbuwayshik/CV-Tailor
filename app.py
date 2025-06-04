import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import re
from transformers import pipeline
import tempfile

# Set Streamlit page configuration
st.set_page_config(page_title="CV Tailor", layout="centered")

# Cache NER and paraphrasing pipelines to avoid reloading
@st.cache_resource
def get_paraphraser():
    # Load a text-to-text generation model for paraphrasing
    return pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

# Function to paraphrase a given CV section based on a job description
def paraphrase_cv(cv_section, job_description):
    paraphraser = get_paraphraser()
    # Prompt for the paraphrasing model
    prompt = f"Paraphrase the following CV section to better match this job description:
Job: {job_description}
CV: {cv_section}"
    # Generate a paraphrased version
    output = paraphraser(prompt, max_length=512, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1)
    return output[0]['generated_text']

# Streamlit UI layout
st.title("🎯 CV Tailor: Section-Based Paraphrasing Tool")

# Input fields
cv_input = st.text_area("✍️ Paste a section from your CV:", height=250)
job_input = st.text_area("📄 Paste the full job description:", height=250)

# When user clicks button, trigger paraphrasing
if st.button("🔁 Paraphrase CV Section"):
    if not cv_input.strip() or not job_input.strip():
        st.warning("Please fill both fields before paraphrasing.")
    else:
        with st.spinner("Paraphrasing..."):
            result = paraphrase_cv(cv_input, job_input)
            st.subheader("📝 Paraphrased Output")
            st.text_area("Updated CV Text", result, height=300)

            # Allow download of result
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8")
            tmp.write(result)
            tmp.close()
            with open(tmp.name, "rb") as f:
                st.download_button("📥 Download as Text", f, file_name="updated_cv_section.txt")
