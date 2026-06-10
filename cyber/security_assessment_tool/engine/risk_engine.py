def calculate_risk(security_data):
    """
    Calculate risk score based on VirusTotal findings and categorize it.
    """
    if security_data.get("status") == "not_found":
        return {
            "score": 0,
            "category": "UNKNOWN",
            "reasons": ["No previous analysis found. Treat with caution."]
        }
    
    if security_data.get("status") == "error":
         return {
            "score": 0,
            "category": "ERROR",
            "reasons": [security_data.get("message", "API Error")]
        }

    malicious = security_data.get("malicious", 0)
    suspicious = security_data.get("suspicious", 0)
    
    # Base scoring rules
    # Note: The PRD mentioned Malware, Phishing, Malicious, Suspicious.
    # VirusTotal 'malicious' often covers malware/phishing.
    # We will use the counts directly for a simplified logic.
    
    score = 0
    reasons = []
    
    if malicious > 0:
        score += malicious * 20 # 20 points per malicious detection
        reasons.append(f"{malicious} security vendors flagged this as malicious.")
    
    if suspicious > 0:
        score += suspicious * 10 # 10 points per suspicious detection
        reasons.append(f"{suspicious} security vendors flagged this as suspicious.")

    # Normalize score to 100
    if score > 100:
        score = 100
    
    # Categorize risk
    if score == 0:
        category = "SAFE"
    elif score <= 20:
        category = "LOW RISK"
    elif score <= 50:
        category = "MEDIUM RISK"
    elif score <= 80:
        category = "HIGH RISK"
    else:
        category = "CRITICAL"
        
    return {
        "score": score,
        "category": category,
        "reasons": reasons
    }
