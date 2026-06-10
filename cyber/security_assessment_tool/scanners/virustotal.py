import requests
import base64
from config.settings import VIRUSTOTAL_API_KEY
from utils.file_handler import calculate_sha256

BASE_URL = "https://www.virustotal.com/api/v3"

def get_headers():
    return {
        "x-apikey": VIRUSTOTAL_API_KEY,
        "accept": "application/json"
    }

def process_response(response, target):
    """
    Common logic to extract malicious, suspicious, and harmless counts.
    """
    if response.status_code == 200:
        data = response.json()
        stats = data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})
        return {
            "target": target,
            "malicious": stats.get('malicious', 0),
            "suspicious": stats.get('suspicious', 0),
            "harmless": stats.get('harmless', 0),
            "details": data,
            "status": "success"
        }
    elif response.status_code == 404:
        return {
            "target": target,
            "malicious": 0,
            "suspicious": 0,
            "harmless": 0,
            "details": response.json() if response.content else {},
            "status": "not_found",
            "message": "No previous analysis found for this target."
        }
    else:
        return {
            "target": target,
            "status": "error",
            "message": f"API Error: {response.status_code}",
            "details": response.json() if response.content else {}
        }

def scan_url(url):
    """
    Scan a URL using VirusTotal.
    """
    # VirusTotal v3 URL ID is base64 without padding
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    endpoint = f"{BASE_URL}/urls/{url_id}"
    response = requests.get(endpoint, headers=get_headers())
    return process_response(response, url)

def scan_ip(ip):
    """
    Get IP address report from VirusTotal.
    """
    endpoint = f"{BASE_URL}/ip_addresses/{ip}"
    response = requests.get(endpoint, headers=get_headers())
    return process_response(response, ip)

def scan_file(uploaded_file):
    """
    Calculate hash and check VirusTotal for existing analysis.
    """
    file_hash = calculate_sha256(uploaded_file)
    endpoint = f"{BASE_URL}/files/{file_hash}"
    response = requests.get(endpoint, headers=get_headers())
    return process_response(response, uploaded_file.name)
