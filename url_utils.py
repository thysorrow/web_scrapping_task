import ipaddress
from urllib.parse import urlparse
import re

def normalize_url(url:str) -> str:
    try:
        url = url.strip()
        if not url:
            raise ValueError("Your URL is empty")
    except:
        raise ValueError("Your URL is empty")
        
    if not re.match(r"^https?://", url):
        url = "https://" + url
        return url
    else:
        return url

def validate_url(url: str) -> tuple[bool, str]:
    try:
        url = url.strip()
        if not url:
            return (False, "URL is empty")
        if len(url) >=2048:
            return (False, "Maximum length of URL is 2048")
        result = urlparse(url)
    except ValueError:
        return (False, "URL format is incorrect")
    
    if result.scheme not in ['http', 'https']:
        return (False, "Only http/https schema allowed")
    
    hostname = result.hostname
    if not hostname:
        return (False, "Hostname is required")
    
    if hostname.lower() == 'localhost':
        return (False, "localhost is not allowed")
    
    try:
        ipaddress.ip_address(hostname)
        return (False, "IP addresses are not allowed")
    except ValueError:
        pass
    
    if result.port is not None:
        return (False, "Ports are not allowed")
    
    return (True, "")

def main():
    pass

if __name__ == "__main__":
    main()