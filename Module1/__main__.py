"""
Allison Valdez
Warmup-1 Diff21 using CodingBat
https://codingbat.com/prob/p197466
"""


"""
This file is the entry point into this program when the module is executed as a
standalone program (i.e. 'python -m Module1'). This file is NOT run during 
imports. This whole file is basically the java equivalent of: public static 
void main(string args[]), or C's int main();
"""


# Generally used to process command line arguments and 'launch' the program
import argparse
from pathlib import Path
from Module1.program import read_input

# Argparser component
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("infile", type=str, help="Input file for program")
arg_parser.add_argument("outfile", type=str, help="Output file for program")
args = arg_parser.parse_args()

# Path Library component
in_path = Path(args.infile)
out_path = Path(args.outfile)

with in_path.open('r') as infile, out_path.open('w') as outfile:
    read_input(infile, outfile)
