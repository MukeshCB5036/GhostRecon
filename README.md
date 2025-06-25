# GHOSTRECON

**GhostRecon** is a simple and effective external attack surface mapping tool designed to enumerate subdomains of a given domain. It leverages public data sources like certificate transparency logs and allows optional brute-force enumeration using wordlists.

---

## 📌 Features

- Performs passive subdomain enumeration using crt.sh
- Optionally performs brute-force subdomain discovery
- Resolves discovered subdomains to IP addresses
- Generates a clean report of discovered assets
- Easy to use with CLI arguments
- Modular design with clean code and logical structure

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MukeshCB5036/GhostRecon.git
cd GhostRecon
Install required dependencies:

pip install -r requirements.txt
🚀 Usage

To run GhostRecon, execute the following command:

python3 ghostrecon.py --domain example.com
Optional parameters:

--wordlist PATH       Specify custom wordlist for bruteforce
--no-bruteforce       Skip the bruteforce phase
💡 Example

$ python3 ghostrecon.py --domain tesla.com

   ____ _               _     ____                                 
  / ___| |__   ___  ___| |_  |  _ \ ___  ___ ___  _ __ ___  ___ ___ 
 | |  _| '_ \ / _ \/ __| __| | |_) / _ \/ __/ _ \| '__/ _ \/ __/ __|
 | |_| | | | |  __/\__ \ |_  |  _ <  __/ (_| (_) | | |  __/\__ \__ \
  \____|_| |_|\___||___/\__| |_| \_\___|\___\___/|_|  \___||___/___/

                👻 External Attack Surface Mapper 👻

[*] Starting crt.sh enumeration for tesla.com...
[+] Found 45 unique subdomains
[*] Running DNS resolution...
[*] Saving output to reports/ghostrecon_output.txt
📄 Report Generation

After the scan is completed, GhostRecon automatically creates a report in the reports/ directory, listing all found subdomains and their resolved IPs.

Example output format:

Domain: tesla.com
Total Subdomains Found: 45

subdomain1.tesla.com - 192.0.2.10
subdomain2.tesla.com - 192.0.2.22
...
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature-branch)
Create a new pull request
📝 License

This project is licensed under the MIT License. See the LICENSE file for more details.

🙏 Acknowledgments

crt.sh for providing passive subdomain data
Python libraries: requests, dnspython, tqdm
Inspiration from tools like Sublist3r and assetfinder

---

### ✅ Next Steps

1. Copy this content into your `README.md` file.
2. Save and commit:

```bash
git add README.md
git commit -m "Updated README with simplified and professional layout"
git push
