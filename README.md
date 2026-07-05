# VulnDB-Explorer

Vulnerability database search and analysis tool with CVE tracking.

## Features
- Search CVE database by keyword, type, or score
- CVSS score filtering
- Real-time CVE feed integration
- Export reports to JSON/CSV
- Trend analysis and statistics

## Usage
```bash
python vulndb.py --search "RCE" --min-score 7.0 -o critical_vulns.json
```
