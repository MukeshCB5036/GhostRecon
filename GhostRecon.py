import argparse
import os
from ghostrecon.core import get_subdomains_crtsh, resolve_dns, bruteforce_subdomains
from ghostrecon.output import save_to_file, format_result

def print_banner():
    banner = r"""

                👻 External Attack Surface Mapper 👻
    """
    print(banner)

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="GhostRecon: External Attack Surface Mapper")
    parser.add_argument('--domain', required=True, help="Target domain (e.g., tesla.com)")
    parser.add_argument('--wordlist', default="wordlists/subdomains-large.txt",
                        help="Path to subdomain wordlist file (default: wordlists/subdomains-large.txt)")
    parser.add_argument('--no-bruteforce', action='store_true', help="Skip subdomain bruteforce")

    args = parser.parse_args()

    domain = args.domain.strip()

    print(f"\n[*] Starting crt.sh enumeration for {domain}...\n")
    subdomains = get_subdomains_crtsh(domain)

    if not subdomains:
        print("[!] No subdomains found from crt.sh.")
        subdomains = []

    bruteforce_results = []
    if not args.no_bruteforce:
        if os.path.isfile(args.wordlist):
            bruteforce_results = bruteforce_subdomains(domain, args.wordlist)
        else:
            print(f"[!] Wordlist file not found: {args.wordlist}")
            print("[!] Skipping bruteforce.")

    # Combine unique subdomains from both methods
    all_subdomains = list(set(subdomains + bruteforce_results))

    if not all_subdomains:
        print("[!] No subdomains found. Exiting.")
        return

    os.makedirs("reports", exist_ok=True)
    results = []

    print("\n[*] Resolving discovered subdomains...\n")
    for sub in all_subdomains:
        ip = resolve_dns(sub)
        line = format_result(sub, ip)
        print(line)
        results.append(line)

    output_file = "reports/ghostrecon_output.txt"
    save_to_file(output_file, results)

if __name__ == "__main__":
    main()
