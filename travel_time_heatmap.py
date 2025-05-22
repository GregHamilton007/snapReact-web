#!/usr/bin/env python3

import argparse
import sys

def process_input(input_text):
    # Split the input text into lines
    lines = input_text.strip().split('\n')
    
    # Initialize variables
    address = None
    mode = None
    
    # Process each line
    for line in lines:
        line = line.strip()
        if line.startswith('Address:'):
            address = line.replace('Address:', '').strip()
        elif line.startswith('Travel Mode:'):
            mode = line.replace('Travel Mode:', '').strip()
    
    # Validate input
    if not address or not mode:
        print("Error: Both address and travel mode are required")
        sys.exit(1)
    
    # Generate the command
    command = f'python3 travel_time_heatmap.py --address "{address}" --mode {mode}'
    return command

def main():
    # Read input from stdin
    input_text = sys.stdin.read()
    
    # Process the input and get the command
    command = process_input(input_text)
    
    # Print the command
    print(command)

if __name__ == "__main__":
    main() 