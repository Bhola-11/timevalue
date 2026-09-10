import os
import urllib.request
import json

# Script to automatically open pull requests for pushed branches if a GitHub Token is present
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
REPO = "Bhola-11/timevalue"

if not TOKEN:
    print("GITHUB_TOKEN not found in environment. Branches are pushed and ready for 1-click PR creation.")
    print("To auto-create PRs via API, set GITHUB_TOKEN environment variable and run this script.")
else:
    print(f"Opening PRs on {REPO} using GitHub REST API...")
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "TimeVault-PR-Builder"
    }

    for i in range(1, 101):
        branch = f"feature/domain-{i:03d}"
        url = f"https://api.github.com/repos/{REPO}/pulls"
        data = {
            "title": f"Feature(domain-{i:03d}): Decision Intelligence Knowledge Protocol {i:03d}",
            "head": branch,
            "base": "main",
            "body": f"Automated Pull Request for Decision Domain Protocol #{i:03d}. Integrates empirical benchmarks, stochastic models, and MCDA weights."
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode('utf-8'))
                print(f"[{i:03d}/100] PR #{res_data.get('number')} created for branch {branch}")
        except Exception as e:
            print(f"[{i:03d}/100] Branch {branch} -> Notice: {e}")
