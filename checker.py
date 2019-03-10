# Yuhong Zhang
# CS4793 hw1 
# A simple spell checker

import argparse
import string
from spellchecker import SpellChecker

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "Input file location")
    parser.add_argument("-m", "--mode", 
        help = "\"Error\" mode printing out the lines with misspelled words, \
        \"Correct\" mode writing out the corrected text to a new file (./corrected.txt by default)", \
        default = "Correct")
    parser.add_argument("-o", "--output", help = "Output file location", default = "./corrected.txt")
    args = parser.parse_args()
    return args

def main():
    args = args_parse()
    spell = SpellChecker()

    try:
        input_file = open(args.input, "r")
    except:
        print("Can't open", args.input)
        return

    if args.mode == "Error":
        for line in input_file:
            words = line.split()
            for word in words:
                if word[-1] not in string.punctuation\
                and spell.correction(word) != word:
                    print(line)
                    break
    elif args.mode == "Correct":
        output_file = open(args.output, "w")
        for line in input_file:
            words = line.split()
            for word in words:
                if word[-1] not in string.punctuation:
                    output_file.write(spell.correction(word))
                else:
                    output_file.write(word)
                output_file.write(" ")
            output_file.write("\n")

if __name__ == "__main__":
    main()