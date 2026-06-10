import streamlit as st
import json
from config.settings import validate_config
from utils.validators import validate_url, validate_ip
from utils.file_handler import validate_file_type
from scanners.virustotal import scan_url, scan_ip, scan_file
from engine.risk_engine import calculate_risk
from ai.report_generator import generate_report

st.set_page_config(page_title="AI Powered Security Assessment Tool", page_icon="🛡️", layout="wide")

def main():
    st.title("🛡️ AI Powered Security Assessment Tool")
    st.markdown("Analyze URLs, IP Addresses, and Files for security threats using VirusTotal and Gemini AI.")

    # Check for missing API keys
    missing_keys = validate_config()
    if missing_keys:
        st.error(f"Missing API Keys: {', '.join(missing_keys)}. Please set them in your .env file.")
        st.stop()

    # Sidebar / Scan Area
    st.sidebar.header("Scan Settings")
    scan_type = st.sidebar.radio("Select Scan Type:", ["Website URL Scan", "IP Address Scan", "File Security Scan"])

    # Initialize session state for results
    if 'results' not in st.session_state:
        st.session_state.results = None
    if 'risk' not in st.session_state:
        st.session_state.risk = None
    if 'report' not in st.session_state:
        st.session_state.report = None

    # Input Section
    target_input = None
    if scan_type == "Website URL Scan":
        target_input = st.text_input("Enter Website URL:", placeholder="https://example.com")
    elif scan_type == "IP Address Scan":
        target_input = st.text_input("Enter IP Address:", placeholder="8.8.8.8")
    elif scan_type == "File Security Scan":
        target_input = st.file_uploader("Upload File (.exe, .zip, .pdf):", type=["exe", "zip", "pdf"])

    if st.button("Start Security Scan"):
        # Validation
        valid = False
        error_msg = ""
        
        if scan_type == "Website URL Scan":
            valid, error_msg = validate_url(target_input)
        elif scan_type == "IP Address Scan":
            valid, error_msg = validate_ip(target_input)
        elif scan_type == "File Security Scan":
            if target_input:
                if validate_file_type(target_input.name):
                    valid = True
                else:
                    error_msg = "Invalid file type. Only .exe, .zip, and .pdf are allowed."
            else:
                error_msg = "Please upload a file."

        if not valid:
            st.error(error_msg)
        else:
            with st.spinner("Analyzing security threats..."):
                # Scanning
                if scan_type == "Website URL Scan":
                    results = scan_url(target_input)
                elif scan_type == "IP Address Scan":
                    results = scan_ip(target_input)
                elif scan_type == "File Security Scan":
                    results = scan_file(target_input)
                
                # Risk Analysis
                risk = calculate_risk(results)
                
                # AI Report Generation
                with st.spinner("Generating AI security report..."):
                    report = generate_report(results, risk)
                
                # Store in session state
                st.session_state.results = results
                st.session_state.risk = risk
                st.session_state.report = report

    # Result Area
    if st.session_state.results:
        st.divider()
        st.header("Security Assessment Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Target Information")
            st.write(f"**Target:** {st.session_state.results.get('target')}")
            st.write(f"**Status:** {st.session_state.results.get('status').replace('_', ' ').title()}")
            
            st.subheader("VirusTotal Findings")
            m_col, s_col, h_col = st.columns(3)
            m_col.metric("Malicious", st.session_state.results.get('malicious'), delta_color="inverse")
            s_col.metric("Suspicious", st.session_state.results.get('suspicious'), delta_color="off")
            h_col.metric("Harmless", st.session_state.results.get('harmless'))

        with col2:
            st.subheader("Risk Analysis")
            risk_score = st.session_state.risk.get('score')
            st.metric("Risk Score", f"{risk_score}/100")
            st.progress(risk_score / 100)
            
            category = st.session_state.risk.get('category')
            color = "green"
            if category == "CRITICAL": color = "red"
            elif category == "HIGH RISK": color = "orange"
            elif category == "MEDIUM RISK": color = "yellow"
            
            st.markdown(f"**Risk Category:** :{color}[{category}]")
            
            if st.session_state.risk.get('reasons'):
                st.write("**Key Reasons:**")
                for reason in st.session_state.risk.get('reasons'):
                    st.write(f"- {reason}")

        st.divider()
        st.subheader("AI Generated Security Report")
        st.markdown(st.session_state.report)
        
        st.divider()
        with st.expander("View Raw Security API Response"):
            st.json(st.session_state.results.get('details'))
            
        # Export and Clear Features
        export_data = {
            "findings": st.session_state.results,
            "risk": st.session_state.risk,
            "report": st.session_state.report
        }
        json_string = json.dumps(export_data, indent=4)
        
        col_exp1, col_exp2 = st.columns([1, 1])
        with col_exp1:
            st.download_button(
                label="Export Security Report (JSON)",
                data=json_string,
                file_name="security_report.json",
                mime="application/json",
                use_container_width=True
            )
        with col_exp2:
            if st.button("Clear Results", use_container_width=True):
                st.session_state.results = None
                st.session_state.risk = None
                st.session_state.report = None
                st.rerun()

if __name__ == "__main__":
    main()
