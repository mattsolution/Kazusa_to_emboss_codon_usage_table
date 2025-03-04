#!/bin/python3

import argparse
import re

def convert_codon_table(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write("#Codon AA Fraction Frequency Number\n")

        for line in infile:
            # Ignore header lines or empty lines
            if line.startswith("fields") or not line.strip():
                continue

            # Use regex to extract groups of (triplet, amino acid, fraction, frequency, number)
            matches = re.findall(r'(\w{3})\s+(\S)\s+([\d.]+)\s+([\d.]+)\s+\(\s*(\d+)\)', line)
            
            for codon, amino_acid, fraction, frequency, number in matches:
                codon = codon.replace('U', 'T')  # Convert RNA to DNA by replacing 'U' with 'T'
                outfile.write(f"{codon}    {amino_acid}    {fraction}    {frequency}    {number}\n")

def main():
    parser = argparse.ArgumentParser(description="Convert codon table to a formatted output.")
    parser.add_argument('input_file', type=str, help="Path to the input codon table file.")
    parser.add_argument('output_file', type=str, help="Path to save the converted output file.")

    args = parser.parse_args()

    convert_codon_table(args.input_file, args.output_file)
    print(f"Conversion complete. Output saved to {args.output_file}")

if __name__ == "__main__":
    main()
