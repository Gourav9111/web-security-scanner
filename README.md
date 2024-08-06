# Basic Web Security Scanner Tool

This is a basic web security scanner tool developed in Python. It can detect basic vulnerabilities such as XSS and SQL Injection, check for the existence of `robots.txt`, and retrieve the IP address of the website.

## Requirements

- Python 3.x
- Requests
- BeautifulSoup4

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Gourav9111/web-security-scanner.git

2.Navigate to the project directory:
   cd web_security_scanner

3.Install the dependencies:
 pip install -r requirements.txt

Usage
Run the tool by executing:
python web_scanner.py

Sure! Let's add two more features: checking for the existence of robots.txt and retrieving the IP address of the website.

Updated requirements.txt
txt
Copy code
requests
beautifulsoup4
Updated web_scanner.py
python
Copy code
import requests
from bs4 import BeautifulSoup
import socket

def check_xss(url):
    xss_payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={'q': xss_payload})
    if xss_payload in response.text:
        print(f"[!] XSS vulnerability detected on {url}")
    else:
        print(f"[-] No XSS vulnerability detected on {url}")

def check_sql_injection(url):
    sql_payload = "' OR '1'='1"
    response = requests.get(url, params={'id': sql_payload})
    if "mysql" in response.text.lower() or "syntax" in response.text.lower():
        print(f"[!] SQL Injection vulnerability detected on {url}")
    else:
        print(f"[-] No SQL Injection vulnerability detected on {url}")

def check_robots_txt(url):
    robots_url = url.rstrip('/') + "/robots.txt"
    response = requests.get(robots_url)
    if response.status_code == 200:
        print(f"[!] Found robots.txt at {robots_url}")
        print(response.text)
    else:
        print(f"[-] No robots.txt found at {robots_url}")

def get_ip_address(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(domain)
        print(f"[+] IP address of {url} is {ip_address}")
    except Exception as e:
        print(f"[-] Could not retrieve IP address for {url}: {e}")

def scan_website(url):
    print(f"Scanning {url} for vulnerabilities...")
    get_ip_address(url)
    check_robots_txt(url)
    check_xss(url)
    check_sql_injection(url)
    print("Scan completed.")

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    scan_website(target_url)
Updated README.md
markdown
Copy code
# Basic Web Security Scanner Tool

This is a basic web security scanner tool developed in Python. It can detect basic vulnerabilities such as XSS and SQL Injection, check for the existence of `robots.txt`, and retrieve the IP address of the website.

## Requirements

- Python 3.x
- Requests
- BeautifulSoup4

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/web_security_scanner.git
Navigate to the project directory:
sh
Copy code
cd web_security_scanner
Install the dependencies:
sh
Copy code
pip install -r requirements.txt


Usage

Run the tool by executing:
python web_scanner.py


Enter the target URL when prompted.

Features
XSS Vulnerability Detection: Checks for Cross-Site Scripting vulnerabilities.
SQL Injection Vulnerability Detection: Checks for SQL Injection vulnerabilities.
robots.txt Check: Checks for the existence of robots.txt and displays its contents.
IP Address Retrieval: Retrieves and displays the IP address of the target website.



Note
This tool is for educational purposes only. Always obtain proper authorization before scanning any website.
   

