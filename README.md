# Practicing Coding Interview Questions With Python

This is a series of practice questions that I am using to familiarize myself 
better with Python. I am using these questions in order to prepare in 
ascending order of difficulty level possible white-boarding interview 
questions. Since we are on winter holiday, I am using this opportunity to 
relearn concepts and skills learned while taking Data Structures at JHU, and 
focus on concepts that caused me the most difficulty.

The specifics of this program are as follows: Given an int n, return the 
absolute difference between n and 21, except return double the absolute 
difference if n is over 21.

## Running The Program
**NOTE: Your IDE may configure the project implicitly as a module. BE SURE TO 
RUN STEP 4 BELOW BEFORE SUBMITTING LABS** 

1. Download and install Python on your computer
2. Navigate to the [PYTHON_PRACTICE]() directory
   1. Run the program as a module: `python -m Module1 -h`. This will print the 
      help message.
3. Run the program as a module (with real inputs test the edge cases for the 
   project): `python -m Lab1 <random input file> <random output file>`
   a. IE: `python -m Module1 input.txt output.txt`

The program's output will be displated in the output.txt file.

### Lab1 Usage:

```commandline
usage: python -m Module1 [-h] infile outfile

positional arguments:
  infile     Input File Pathname
  outfile    Output File Pathname

optional arguments:
  -h, --help  show a help message and exits the program
```

Usage statements are very formalized

| Symbol    | Meaning   |
| ---           | ---       |
| [var]         | variable var is optional. |
| var           | variable var is required. All positional arguments are required.|
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values |
| *             | This argument consumes 0 or more values |

### Project Layout
The following was my project's package layout:

* CodingPractice1_diff21/: `The parent or "root" folder containing 
  all of the projecs files`
    * README.md:
      `The README files that describes my programs and the nuances needed 
      to run the program`
    * Module1/: 
      `The module of my program (per requirement).`
      * __init__.py 
        `This python file details critical functions, variables, and 
        classes that are exposed when scripts import the Lab1 module.`
      * __main__.py 
        `The starting point when the program runs, it handles command line 
        arguments.`
      * *.py 
        `Holds the scripts that perform the code.`
    * Resources/:
      * input.txt
        `The input.txt file is required in order for the program to run as 
        it holds the necessary input.`
      * output.txt
        `The output.txt file will write the generated output after it 
        commences executing.`