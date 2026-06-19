#!/usr/bin/env python3
"""
README Analyzer — Analyze GitHub README files for key metrics.
Usage: python readme_analyzer.py <readme_file>
"""
import sys, re

def analyze(filepath):
    with open(filepath) as f:
        text = f.read()
    
    lines = text.split('\n')
    words = len(text.split())
    headers = len(re.findall(r'^#+\s', text, re.MULTILINE))
    code_blocks = len(re.findall(r'```', text)) // 2
    links = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text))
    emojis = len(re.findall(r'[\U0001F300-\U0001FAFF]', text))
    
    print(f"📄 README Analysis: {filepath}")
    print(f"{'='*40}")
    print(f"Lines:      {len(lines)}")
    print(f"Words:      {words}")
    print(f"Headers:    {headers}")
    print(f"Code blocks: {code_blocks}")
    print(f"Links:      {links}")
    print(f"Emojis:     {emojis}")
    
    readability = "Great" if headers > 3 and code_blocks > 0 and links > 3 else "Needs work"
    print(f"\n📊 Readability: {readability}")
    print(f"💡 Tip: Projects with 3+ headers and code examples get 4x more engagement")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python readme_analyzer.py <readme_file>")
        sys.exit(1)
    analyze(sys.argv[1])
