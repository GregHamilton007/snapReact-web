#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def get_untracked_files():
    # Get list of untracked files
    result = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], 
                          capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def get_modified_files():
    # Get list of modified files
    result = subprocess.run(['git', 'ls-files', '--modified'], 
                          capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def get_map_name(file_path):
    # Extract map name from the filename
    filename = os.path.basename(file_path)
    # Remove the 'travel_time_heatmap_' prefix and '.html' suffix
    map_name = filename.replace('travel_time_heatmap_', '').replace('.html', '')
    return map_name

def commit_file(file_path):
    map_name = get_map_name(file_path)
    commit_message = f"new map: {map_name}"
    
    # Add the file
    subprocess.run(['git', 'add', file_path])
    
    # Commit the file
    subprocess.run(['git', 'commit', '-m', commit_message])
    print(f"Committed {file_path} with message: {commit_message}")

def push_changes():
    # Push the changes to the remote repository
    subprocess.run(['git', 'push'])
    print("Pushed changes to remote repository")

def main():
    maps_dir = "/Users/ryanhamilton/pythonenv/tfdemo/snapReact-web/maps"
    
    # Get all untracked and modified files
    untracked_files = get_untracked_files()
    modified_files = get_modified_files()
    
    # Filter for HTML files in the maps directory
    html_files = [f for f in untracked_files + modified_files 
                 if f.endswith('.html') and f.startswith('maps/')]
    
    if not html_files:
        print("No untracked or modified HTML files found in maps directory")
        return
    
    # Commit each file
    for file_path in html_files:
        commit_file(file_path)
    
    # Push all changes
    push_changes()

if __name__ == "__main__":
    main()
