# 🏥 MedGemma Clinical Triage Assistant
### Kaggle MedGemma Impact Challenge 2026 Submission

**Team:** [Your Team Name]  
**Track:** Main Track + Edge AI Prize  
**License:** CC BY 4.0

---

## ⚠️ DISCLAIMER
This project is for **educational and research purposes only**. It does NOT provide medical advice. Always consult qualified healthcare professionals for medical decisions.

---

## 📋 Overview

A **clinical triage assistant** powered by Google's **MedGemma-1.5-4b-it** that analyzes patient symptoms and provides urgency assessment (LOW/MEDIUM/HIGH).

**Problem:** 1.5 billion people lack access to timely healthcare, especially in rural areas without internet.

**Solution:** AI-powered triage that works offline after initial setup, running on standard hardware.

---

## 🚀 Quick Start

### Option 1: Streamlit App (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

**Important:** You need a Hugging Face token to use MedGemma!

1. Get token from: https://huggingface.co/settings/tokens
2. Request MedGemma access: https://huggingface.co/google/medgemma-1.5-4b-it
3. Paste token in app sidebar
4. Click "Load MedGemma Model"

Opens in browser at: `http://localhost:8501`

**Full guide:** See `GET_HF_TOKEN.md`

### Option 2: Kaggle Notebook

1. **Go to:** https://www.kaggle.com/code
2. **Upload:** `medgemma_cpu_fixed.ipynb`
3. **Run** all cells
4. **Record** your screen for the demo video

---

## 📦 Files Included

| File | Purpose |
|------|---------|
| `app.py` | **Streamlit web application** |
| `medgemma_cpu_fixed.ipynb` | Optimized Kaggle notebook (CPU) |
| `medgemma_fixed.ipynb` | Basic demo notebook |
| `medgemma_final.ipynb` | Complete demo with metrics |
| `medgemma_complete_notebook.ipynb` | Extended version |
| `STREAMLIT_DEPLOYMENT.md` | **Streamlit deployment guide** |
| `WRITEUP.md` | 3-page competition writeup |
| `VIDEO_SCRIPT.md` | 3-minute video recording guide |
| `SUBMISSION_GUIDE.md` | Step-by-step Kaggle submission |
| `README.md` | Project documentation |
| `requirements.txt` | Python dependencies |

---

## 🎯 How to Submit

### 1. Create Kaggle Notebook
```
1. Go to: https://www.kaggle.com/code
2. Click "New Notebook"
3. Upload: medgemma_cpu_fixed.ipynb
4. Run all cells to show MedGemma working
5. Save and make Public
6. Copy the notebook URL
```

### 2. Record Demo Video (3 min max)
```
1. Open your Kaggle Notebook OR Streamlit app
2. Start screen recording (OBS/Loom)
3. Run analysis showing MedGemma triage
4. Explain problem, solution, impact
5. Export as MP4 (< 100MB)
```

### 3. Convert Writeup to PDF
```
1. Open WRITEUP.md
2. Fill in your team details
3. Print/Export to PDF (3 pages max)
```

### 4. Submit to Kaggle
```
1. Go to: https://www.kaggle.com/competitions/med-gemma-impact-challenge
2. Click "Submit Your Work"
3. Upload: Video + PDF Writeup + Notebook URL
4. Select: Main Track + Edge AI Prize
5. Submit before deadline!
```

---

## 🏆 Competition Alignment

| Criteria | Weight | Our Approach |
|----------|--------|--------------|
| **Execution & Communication** | 30% | Clear notebook, professional demo |
| **Effective HAI-DEF Usage** | 20% | MedGemma core to triage logic |
| **Product Feasibility** | 20% | Runs on CPU, standard hardware |
| **Problem Domain** | 15% | Real healthcare access gap |
| **Impact Potential** | 15% | 1.5B people without healthcare |

---

## 📊 Demo Cases

The app includes 3 patient cases:

1. **HIGH Urgency:** 55M with chest pain (possible heart attack)
2. **MEDIUM Urgency:** 25F with abdominal pain (possible appendicitis)
3. **LOW Urgency:** 32M with mild headache (tension headache)

---

## 🌍 Edge AI Deployment

**Hardware Requirements:**
- Minimum: 8GB RAM, 4-core CPU
- Recommended: 16GB RAM, 8-core CPU
- GPU: Optional (3x faster)

**Deployment Scenarios:**
- Rural clinics (no internet after setup)
- Ambulances (pre-hospital assessment)
- Emergency departments (triage)
- Telemedicine (initial screening)

---

## 📝 Model Information

- **Model:** `google/medgemma-1.5-4b-it`
- **Size:** 4B parameters
- **Use:** Clinical reasoning and triage
- **Access:** Available on Kaggle (gated on Hugging Face)

---

## 🔗 Resources

- **MedGemma:** https://huggingface.co/google/medgemma-1.5-4b-it
- **Docs:** https://developers.google.com/health-ai-developer-foundations/medgemma
- **Competition:** https://www.kaggle.com/competitions/med-gemma-impact-challenge
- **Streamlit Guide:** STREAMLIT_DEPLOYMENT.md

---

## 📧 Contact

**Team:** [Your Team Name]  
**Email:** [your.email@example.com]  
**Kaggle:** [your username]

---

**License:** CC BY 4.0  
**MedGemma Impact Challenge 2026**
