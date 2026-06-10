import re
import validators

def validate_url(url):
    """
    Validate the format of a URL.
    """
    if not url:
        return False, "URL cannot be empty."
    
    if not validators.url(url):
        return False, "Invalid URL format. Example: https://example.com"
    
    return True, ""

def validate_ip(ip):
    """
    Validate the format of an IPv4 or IPv6 address.
    """
    if not ip:
        return False, "IP address cannot be empty."
    
    # IPv4 regex
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    # Simple IPv6 regex (can be improved)
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    if re.match(ipv4_pattern, ip):
        # Additional check for IPv4 octet values
        octets = ip.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            return True, ""
    
    if re.match(ipv6_pattern, ip):
        return True, ""
        
    return False, "Invalid IP address format."
