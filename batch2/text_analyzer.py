#!/usr/bin/env python3
"""Analyze text: word count, reading time, frequency."""
import sys, re

def analyze(text):
    words = re.findall(r'\w+', text)
    sentences = re.split(r'[.!?]+', text)
    chars = len(text)
    avg_word = len(''.join(words))/len(words) if words else 0
    reading_min = len(words) / 200
    
    print(f"📊 Text Analysis")
    print(f"{'='*30}")
    print(f"Characters:   {chars}")
    print(f"Words:        {len(words)}")
    print(f"Sentences:    {len(sentences)-1}")
    print(f"Avg word len: {avg_word:.1f}")
    print(f"Reading time: {reading_min:.1f} min")
    print(f"Reading time: {max(1,int(reading_min*60))} seconds")

if __name__ == "__main__":
    text = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1]).read()
    analyze(text)
