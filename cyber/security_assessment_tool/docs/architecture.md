# System Architecture

## Overview
The AI Powered Security Assessment Tool is a modular Python application designed to analyze URLs, IP addresses, and files for security threats. It integrates VirusTotal for threat intelligence and Google Gemini AI for human-readable report generation.

## Workflow Flow
1. **User Interface (Streamlit):** Accepts user input (URL, IP, or File).
2. **Input Validation (utils/validators.py):** Ensures the input is correctly formatted before processing.
3. **Security Scanning (scanners/virustotal.py):**
   - For Files: Calculates SHA256 hash (utils/file_handler.py) and queries VirusTotal.
   - For URLs/IPs: Queries VirusTotal API directly.
4. **Risk Calculation (engine/risk_engine.py):** Processes VirusTotal detections to calculate a normalized risk score (0-100) and category.
5. **AI Report Generation (ai/report_generator.py):** Sends the technical findings and risk score to Google Gemini AI to generate a professional report.
6. **Result Display:** Shows findings, risk metrics, and the AI report on the Streamlit dashboard.

## Module Responsibilities
- `app.py`: Main entry point, UI layout, and state management.
- `config/settings.py`: Environment variable loading and validation.
- `scanners/`: Integration with external security APIs.
- `engine/`: Business logic for threat assessment.
- `ai/`: LLM integration for natural language generation.
- `utils/`: Reusable helper functions for hashing and validation.
