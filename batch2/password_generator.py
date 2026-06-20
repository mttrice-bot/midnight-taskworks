#!/usr/bin/env python3
"""Generate secure random passwords."""
import random, string, sys

def generate(length=16, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special: chars += "!@#$%^&*()_+-="
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    special = "--no-special" not in sys.argv
    print(f"🔐 Generated password ({length} chars):")
    print(generate(length, special))
