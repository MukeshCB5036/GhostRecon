# ghostrecon/utils.py

import requests
import time

def load_wordlist(filepath):
    """
    Loads lines from a wordlist file into a list.
    Skips empty lines and strips whitespace.
    """
    try:
        with open(filepath, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {filepath}")
        return []

def http_get(url, headers=None, retries=3, delay=1):
    """
    Performs a GET request with retry logic.
    Returns response object or None on failure.
    """
    headers = headers or {}
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
            else:
                print(f"[!] Warning: Received status {response.status_code} for {url}")
        except requests.RequestException as e:
            print(f"[!] Error during GET {url}: {e}")
        if attempt < retries:
            time.sleep(delay)
    return None
