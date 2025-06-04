# 📄 CV Tailor: AI-Powered Resume Customizer

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

CV Tailor helps you adapt specific sections of your resume to better match a job description using AI-powered paraphrasing.

---

## 🚀 Features

- 🧠 Uses transformers to paraphrase your CV based on a job description
- 📄 Accepts PDF uploads of your resume
- 🌐 Scrapes job descriptions from public URLs or takes text input
- ✍️ Generates rewritten CV sections tailored to specific roles
- 📥 Downloadable paraphrased CV text

---

## 🖥️ How to Use

1. Upload a section of your CV as a PDF or type it into the input.
2. Paste the job description in the adjacent box.
3. Click "Paraphrase" to generate an aligned version.
4. Review the result and download the paraphrased text.

---

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📚 Requirements

- Python 3.7+
- Streamlit
- Transformers (HuggingFace)
- PyMuPDF
- BeautifulSoup4
- Requests

---

## 🔗 Live App Deployment

To deploy this on [Streamlit Cloud](https://streamlit.io/cloud):

1. Push the repo to your GitHub.
2. Go to https://streamlit.io/cloud and log in.
3. Click **“New App”** > select your GitHub repo.
4. Point to `app.py`, click **Deploy**.

Once deployed, copy your app link and update this README:

```markdown
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-deployed-app-link)
```

---

## 🤖 Built With

- `transformers` by Hugging Face
- `streamlit`
- `PyMuPDF`
- `BeautifulSoup`
- `requests`
