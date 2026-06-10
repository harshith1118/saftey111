# 🛡️ AI Powered Security Assessment Tool

A modular, AI-driven cybersecurity dashboard that analyzes URLs, IP addresses, and files to detect threats and generate professional, human-readable security reports.

## 🚀 Key Features

-   **Website URL Scanning:** Analyzes URL reputation and identifies malicious or suspicious indicators.
-   **IP Address Reputation:** Checks global threat intelligence databases for IP reputation.
-   **File Security Analysis:** Scans uploaded `.exe`, `.zip`, and `.pdf` files using SHA256 hashing and VirusTotal.
-   **Intelligent Risk Engine:** Calculates a normalized risk score (0-100) and categorizes threats (SAFE to CRITICAL).
-   **AI-Powered Reports:** Transforms technical findings into professional reports using Google Gemini AI.
-   **Raw Data Transparency:** View the underlying JSON responses from the Security API.
-   **Exportable Results:** Download your security assessment results as a standardized JSON report.
-   **Clean UI:** Modern Streamlit interface with real-time feedback and result persistence.

## 🛠️ Tech Stack

-   **Frontend:** [Streamlit](https://streamlit.io/)
-   **Programming Language:** Python 3.x
-   **Threat Intelligence:** [VirusTotal v3 API](https://developers.virustotal.com/reference/overview)
-   **Generative AI:** [Google Gemini API](https://ai.google.dev/)
-   **Libraries:** `requests`, `python-dotenv`, `google-generativeai`, `validators`

## 📁 Project Structure

```text
security_assessment_tool/
├── app.py                  # Main Streamlit Dashboard
├── ai/
│   └── report_generator.py  # Gemini AI logic & dynamic model selection
├── config/
│   └── settings.py         # Environment configuration
├── engine/
│   └── risk_engine.py      # Risk scoring & normalization logic
├── scanners/
│   └── virustotal.py       # VirusTotal API integration
├── utils/
│   ├── file_handler.py     # SHA256 hashing & file validation
│   └── validators.py       # URL & IP format validation
├── docs/
│   └── architecture.md     # System design & data flow
├── .env.example            # Environment variable template
├── requirements.txt         # Project dependencies
└── README.md               # User documentation
```

## ⚙️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd security_assessment_tool
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Keys:**
    -   Create a `.env` file in the root directory (or copy `.env.example`).
    -   Add your API keys:
        ```env
        VIRUSTOTAL_API_KEY=your_key_here
        GEMINI_API_KEY=your_key_here
        ```

## 🖥️ Usage

Start the application using the following command:
```bash
streamlit run app.py
```

1.  Select the **Scan Type** from the sidebar (URL, IP, or File).
2.  Provide the necessary input.
3.  Click **"Start Security Scan"**.
4.  View the findings, risk score, and AI-generated report.
5.  (Optional) **Export** the results to JSON or **Clear** to start over.

## 🛡️ Security Disclaimer
This tool is for educational and informational purposes only. It relies on third-party APIs (VirusTotal and Google Gemini) and does not guarantee 100% accuracy in threat detection. Always use multiple sources for critical security assessments.

---
Built with ❤️ by Gemini CLI
