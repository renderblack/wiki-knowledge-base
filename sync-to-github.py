#!/usr/bin/env python3
"""Sync wiki to GitHub - pushes all local .md files to wiki-knowledge-base repo."""

import base64, os, requests, json
from pathlib import Path

TOKEN = os.environ.get("WIKI_GITHUB_TOKEN", "")
REPO = "renderblack/wiki-knowledge-base"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
base_url = f"https://api.github.com/repos/{REPO}"
WIKI_DIR = Path.home() / "wiki"

def get_sha(path):
    """Get SHA of existing file on GitHub."""
    r = requests.get(f"{base_url}/contents/{path}", headers=HEADERS)
    if r.status_code == 200:
        return r.json()["sha"]
    return None

def push_file(rel_path, content):
    """Upload/update a single file."""
    sha = get_sha(rel_path)
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    payload = {
        "message": f"feat: {rel_path}",
        "content": encoded
    }
    if sha:
        payload["sha"] = sha
    r = requests.put(f"{base_url}/contents/{rel_path}", headers=HEADERS, json=payload)
    return r.status_code in (200, 201), r.status_code

def main():
    pushed = 0
    skipped = 0
    errors = []
    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = Path(root) / fname
            rel = str(fpath.relative_to(WIKI_DIR))
            try:
                content = fpath.read_text(encoding="utf-8")
                ok, code = push_file(rel, content)
                if ok:
                    pushed += 1
                else:
                    errors.append(f"{rel}: HTTP {code}")
            except Exception as e:
                errors.append(f"{rel}: {e}")
    
    print(f"Synced: {pushed} files")
    if errors:
        print(f"Errors: {errors[:5]}")
    return len(errors) == 0

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
