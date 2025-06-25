"""
Core GhostRecon functions:
- crt.sh subdomain enumeration
- DNS resolution
- Subdomain bruteforce
"""

import requests
import dns.resolver
from ghostrecon.utils import load_wordlist

HEADERS = {'User-Agent': 'GhostRecon/1.0'}

def get_subdomains_crtsh(domain):
    """
    Query crt.sh certificate transparency logs for subdomains of the target domain.
    Returns a list of unique subdomains.
    """
    print(f"[*] Searching crt.sh for subdomains of {domain}...")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = set()

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                names = entry['name_value'].split("\n")
                for name in names:
                    name = name.strip().lower()
                    if domain in name:
                        subdomains.add(name)
            print(f"[+] Found {len(subdomains)} subdomains from crt.sh")
        else:
            print(f"[!] crt.sh returned status code {response.status_code}")
    except Exception as e:
        print(f"[!] Error querying crt.sh: {e}")

    return list(subdomains)

def resolve_dns(subdomain):
    """
    Resolve the A record of a subdomain.
    Returns IP address as string or None if resolution fails.
    """
    try:
        answers = dns.resolver.resolve(subdomain, 'A')
        for rdata in answers:
            return rdata.to_text()
    except Exception:
        return None

def bruteforce_subdomains(domain, wordlist_path, limit=None):
    """
    Bruteforce subdomains by prefixing each word from wordlist to domain.
    Optionally limit the number of words checked.
    Returns list of subdomains that successfully resolve.
    """
    print(f"[*] Starting bruteforce on {domain} using wordlist {wordlist_path}...")

    words = load_wordlist(wordlist_path)
    if limit:
        words = words[:limit]

    found = []

    for word in words:
        subdomain = f"{word}.{domain}"
        ip = resolve_dns(subdomain)
        if ip:
            print(f"[+] Found: {subdomain} -> {ip}")
            found.append(subdomain)

    print(f"[+] Bruteforce complete. Found {len(found)} subdomains.")
    return found

