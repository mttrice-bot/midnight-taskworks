#!/usr/bin/env python3
"""
Domain Availability Checker — Check if domain names are available.
Usage: python domain_checker.py domains.txt
"""
import sys, socket, csv

def check_domain(domain):
    try:
        socket.gethostbyname(domain)
        return "Taken"
    except socket.gaierror:
        return "Available"
    except Exception as e:
        return f"Error: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python domain_checker.py domains.txt")
        print("domains.txt: one domain per line (e.g., mybusiness.com)")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        domains = [line.strip() for line in f if line.strip()]
    
    print(f"🔍 Checking {len(domains)} domains...\n")
    results = []
    for d in domains:
        status = check_domain(d)
        icon = "✅" if status == "Available" else "❌"
        print(f"  {icon} {d} - {status}")
        results.append({"domain": d, "status": status})
    
    with open("domain_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["domain", "status"])
        w.writeheader()
        w.writerows(results)
    print(f"\n📁 Saved to domain_results.csv")

if __name__ == "__main__":
    main()
