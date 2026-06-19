#!/usr/bin/env python3
"""Turn a blog post into social media content."""
import sys, re

def repurpose(text):
    # Extract key sentences
    sentences = re.split(r'[.!?]+', text)
    key_points = [s.strip() for s in sentences if len(s.strip()) > 30][:5]
    
    print("📝 LINKEDIN POST")
    print("="*40)
    print(f"💡 Key insight:\n{key_points[0] if key_points else text[:100]}...\n")
    print(f"👇 Read more: [your-link-here]\n")
    
    print("\n🐦 TWITTER THREAD")
    print("="*40)
    for i, p in enumerate(key_points, 1):
        print(f"{i}. {p[:200]}")
    
    print("\n📧 NEWSLETTER BLURB")
    print("="*40)
    print(f"📌 {key_points[0][:100] if key_points else text[:100]}...")
    print(f"\nIn this post: {' | '.join(p[:50] for p in key_points[:3])}")

if __name__ == "__main__":
    text = sys.stdin.read() if not sys.argv[1:] else open(sys.argv[1]).read()
    repurpose(text)
