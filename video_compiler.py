#!/usr/bin/env python3
"""
Video Compiler — Merge multiple video clips into a single compilation.
Usage: python video_compiler.py clip1.mp4 clip2.mp4 clip3.mp4 -o output.mp4
"""

import argparse
import subprocess
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Compile multiple video clips into one file")
    parser.add_argument("files", nargs="+", help="Video files to merge")
    parser.add_argument("-o", "--output", default="compilation.mp4", help="Output filename")
    parser.add_argument("--crossfade", type=float, default=0.5, help="Crossfade duration in seconds")
    
    args = parser.parse_args()
    
    if len(args.files) < 2:
        print("Need at least 2 video files to compile")
        sys.exit(1)
    
    # Create a file list for ffmpeg
    list_path = "/tmp/video_list.txt"
    with open(list_path, "w") as f:
        for video in args.files:
            f.write(f"file '{os.path.abspath(video)}'\n")
    
    print(f"Merging {len(args.files)} videos into {args.output}...")
    
    # Use ffmpeg to concat
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_path,
        "-c:v", "libx264", "-preset", "fast",
        "-c:a", "aac", "-b:a", "128k",
        args.output
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Success! Output: {args.output}")
    else:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    main()
