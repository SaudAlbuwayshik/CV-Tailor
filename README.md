# CV Tailor: Section-Based AI Paraphrasing Tool

**CV Tailor** is a simple Streamlit app that helps job seekers paraphrase specific sections of their CV (like work experience or summaries) to better align with job descriptions. This tool uses NLP models from Hugging Face to provide accurate and targeted paraphrasing.

---

## 🔧 Features

- Paste a **CV section** and a **job description**
- Receive a **paraphrased version** of the CV section tailored to the job
- Supports **downloading** the output for easy use in resumes

---

## 🚀 Demo

You can run this tool locally by following the steps below.

---

## 🛠️ Installation

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/cv-tailor.git
cd cv-tailor
```

2. **Install dependencies**  
We recommend using a virtual environment:
```bash
pip install -r requirements.txt
```

3. **Run the app**  
```bash
streamlit run app.py
```

---

## 🧠 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (`T5`)
- PyMuPDF (for PDF text handling)
- Tempfile (for download feature)

---

## ✍️ How It Works

1. Paste **a section** of your CV.
2. Paste the **full job description**.
3. Click **Paraphrase**.
4. Download the **tailored text** to use in your resume.

---

## 📂 File Structure

```
cv-tailor/
├── app.py             # Streamlit app
├── requirements.txt   # Python dependencies
└── README.md          # Project info
```

---

## 👨‍💻 Author

**Saud Albuwayshik**  
[GitHub Profile](https://github.com/SaudAlbuwayshik)

---

## 📜 License

MIT License
