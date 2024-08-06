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
