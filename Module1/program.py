"""
Allison Valdez
Warmup-1 Diff21 using CodingBat
https://codingbat.com/prob/p197466
"""

from sys import stderr
from typing import TextIO


def difference(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


def read_input(infile: TextIO, outfile: TextIO, self=None) -> None:
    """
       This function is in charge of reading from the input file and writing
       the generated output to the designated output file

       :param infile: Text file set to read mode
       :param outfile: Text file set to write mode
       """

    next_line = infile.readline()

    while next_line is not None and next_line != "":
        try:

        except ValueError:
            print(f'Error parsing "{next_line} for character string',
                  file=stderr)
            continue
        finally:
            next_line = infile.readline()

    outfile.write('\n')
    for i in range(len(next_line)):
        outfile.write(" "+ next_line + " " + "\n")
    outfile.write('\n')
