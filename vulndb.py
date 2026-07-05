#!/usr/bin/env python3
"""VulnDB-Explorer — Vulnerability database search and analysis tool"""
import argparse, json, sys
from typing import List, Dict

class VulnerabilityDB:
    def __init__(self):
        self.database = [
            {"id": "CVE-2024-3094", "score": 10.0, "desc": "Critical XZ Utils backdoor", "type": "Supply Chain"},
            {"id": "CVE-2024-1708", "score": 9.8, "desc": "ConnectWise ScreenConnect auth bypass", "type": "RCE"},
            {"id": "CVE-2024-21626", "score": 8.6, "desc": "runc container escape", "type": "Privilege Escalation"},
            {"id": "CVE-2024-27198", "score": 9.8, "desc": "JetBrains TeamCity auth bypass", "type": "Authentication"},
            {"id": "CVE-2024-2379", "score": 7.5, "desc": "CURL QUIC cert verification", "type": "Cryptographic"},
        ]
    
    def search(self, query: str) -> List[Dict]:
        results = []
        q = query.lower()
        for vuln in self.database:
            if q in vuln["id"].lower() or q in vuln["type"].lower() or q in vuln["desc"].lower():
                results.append(vuln)
        return results
    
    def filter_by_score(self, min_score: float) -> List[Dict]:
        return [v for v in self.database if v["score"] >= min_score]

def main():
    parser = argparse.ArgumentParser(description="VulnDB-Explorer")
    parser.add_argument("--search", help="Search vulnerability database")
    parser.add_argument("--min-score", type=float, help="Minimum CVSS score filter")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()
    
    db = VulnerabilityDB()
    results = []
    
    if args.search:
        results = db.search(args.search)
    elif args.min_score:
        results = db.filter_by_score(args.min_score)
    else:
        results = db.database
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
    
    print(f"Found {len(results)} vulnerabilities:")
    for r in results:
        print(f"  [{r['score']}] {r['id']} - {r['desc']}")

if __name__ == "__main__":
    main()
