# ghostrecon/utils.py

import requests
import time

def load_wordlist(filepath):
    """
    Load a wordlist file and return a list of non-empty stripped lines.
    """
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {filepath}")
        return []

def http_get(url, headers=None, retries=3, delay=1):
    """
    Perform HTTP GET request with retry logic.
    Returns the response object or None on failure.
    """
    headers = headers or {}
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
            else:
                print(f"[!] Warning: Status {response.status_code} for {url}")
        except requests.RequestException as e:
            print(f"[!] Request error for {url}: {e}")

        if attempt < retries:
            time.sleep(delay)
    return None
