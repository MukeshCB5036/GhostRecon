# ghostrecon/output.py

def save_to_file(filename, lines):
    """
    Save a list of strings to a file, each on a new line.
    """
    try:
        with open(filename, 'w') as f:
            for line in lines:
                f.write(line + '\n')
        print(f"[✔] Results saved to {filename}")
    except Exception as e:
        print(f"[!] Error saving file {filename}: {e}")

def format_result(subdomain, ip):
    """
    Format subdomain and IP into a consistent output string.
    """
    ip_text = ip if ip else "Unresolved"
    return f"{subdomain} -> {ip_text}"
