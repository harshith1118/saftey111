import google.generativeai as genai
from config.settings import GEMINI_API_KEY

def generate_report(findings, risk_analysis):
    """
    Generate a professional cybersecurity report using Gemini AI with fallback models.
    """
    if not GEMINI_API_KEY:
        return "Gemini API Key is missing. Cannot generate AI report."

    genai.configure(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    You are a professional Cybersecurity Analyst. 
    Generate a concise security assessment report based on the following data:
    
    Target: {findings.get('target')}
    VirusTotal Malicious Detections: {findings.get('malicious')}
    VirusTotal Suspicious Detections: {findings.get('suspicious')}
    VirusTotal Harmless Detections: {findings.get('harmless')}
    
    Calculated Risk Score: {risk_analysis.get('score')}/100
    Risk Category: {risk_analysis.get('category')}
    Risk Reasons: {', '.join(risk_analysis.get('reasons', []))}
    
    Please structure the report with these sections:
    1. Executive Summary
    2. Security Findings
    3. Risk Explanation
    4. Recommendations
    5. Final Advice
    
    Use a professional and clear tone.
    """

    # List of models to try in order of preference
    models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    last_error = ""

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            last_error = str(e)
            continue # Try the next model
            
    return f"Error generating AI report: All attempted models failed. Last error: {last_error}"
