#dirfootagetime
#by Min-Hsao Chen (w/ ChatGPT-4)
#version 0.0005
# This script calculates the total duration of all video files in a specified directory, 
# including its subdirectories, and displays the results in both seconds and mm:ss format.
# It allows optional filtering to exclude or include files based on specific text in the filenames.
# The script lists the time for each subdirectory as well as the total duration for all video files.
# Required modules: os, sys, subprocess, argparse, pathlib, collections
# ffmpeg is required for this script. Install it using: brew install ffmpeg

import os
import sys
import subprocess
import argparse
from pathlib import Path
from collections import defaultdict

def get_video_duration(file_path):
    """
    Get the duration of a video file using ffprobe.
    
    Args:
        file_path (Path): Path to the video file.
        
    Returns:
        float: Duration of the video in seconds.
    """
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        return float(result.stdout)
    except Exception as e:
        print(f"Error getting duration for {file_path}: {e}")
        return 0.0

def format_duration(seconds):
    """
    Format duration from seconds to mm:ss format.
    
    Args:
        seconds (float): Duration in seconds.
        
    Returns:
        str: Duration in mm:ss format.
    """
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def main():
    """
    Main function to calculate and display the total duration of video files in a directory.
    """
    parser = argparse.ArgumentParser(description="Calculate the total duration of all video files in a directory.")
    parser.add_argument("directory", type=str, help="Path to the directory containing video files.")
    parser.add_argument("--exclude", type=str, help="Text to exclude files containing this text.")
    parser.add_argument("--include", type=str, help="Text to include only files containing this text.")
    args = parser.parse_args()

    total_duration = 0.0
    durations_by_subdir = defaultdict(float)
    video_files = list(Path(args.directory).rglob("*.*"))

    print("Calculating total video duration...")
    for video_file in video_files:
        if args.exclude and args.exclude in video_file.name:
            print(f"Excluded {video_file.name}")
            continue
        if args.include and args.include not in video_file.name:
            print(f"Skipped {video_file.name}")
            continue
        
        duration = get_video_duration(video_file)
        total_duration += duration
        subdir = str(video_file.parent.relative_to(args.directory))
        durations_by_subdir[subdir] += duration
        print(f"Processed {video_file.name}: {duration:.2f} seconds")

    print("\n#dirfootagetime")
    print("#by Min-Hsao Chen (w/ ChatGPT-4)")
    print("#version 0.0005")
    
    for subdir, duration in durations_by_subdir.items():
        formatted_duration = format_duration(duration)
        print(f"Subdirectory '{subdir}': {duration:.2f} seconds ({formatted_duration})")
    
    formatted_total_duration = format_duration(total_duration)
    print(f"Total duration of all video files: {total_duration:.2f} seconds ({formatted_total_duration})")

if __name__ == "__main__":
    main()
