#!/usr/bin/python
# -*- coding: utf-8 -*-
# SNAKES AHEAD!!!
# Created by ogator on 1/11/2017.
import argparse
import os


class WordGen(object):
    def __init__(self):
        self.description = "         _____        _\n" \
                           "       d8888888b.   d888b   ,db\n" \
                           "     d888888888888888888888888.*\n" \
                           "    888888 88888888888 88 8888888o\n" \
                           "   8888888 888888888 8888 8888`~~   - GRIZZLY STEPPE - \n" \
                           "   8888888 888888888 88888\n" \
                           "   888888 8888888888 8888\n" \
                           "  ## 88888  88888 ##  8888\n" \
                           " #### 88888      ###   8888\n" \
                           "###,,, 888,,,    ##,,,  88,,,\n"

        print(self.description)

        parser = argparse.ArgumentParser()
        parser.add_argument('--username', required=True, type=str, dest='username',
                            help='Username')
        parser.add_argument('--passfile', required=True, dest='password_file',
                            help='Input file with passwords')
        parser.add_argument('--delim', required=True, dest='delimiter',
                            help='Delimiter between username and passwords')
        parser.add_argument('--output', required=True, dest='output',
                            help='Output file')
        args = parser.parse_args()
        self.username = args.username
        self.password_file = args.password_file
        self.delimiter = args.delimiter
        self.output = args.output

    def generate(self):
        # check for existence
        if os.access(path=self.password_file, mode=os.R_OK):
            with open(self.password_file, "r") as pass_file, open(self.output, 'w') as output_file:
                for line in pass_file:
                    output_file.write(self.username + self.delimiter + line)
                output_file.close()
                pass_file.close()
        else:
            print("Password file cannot be opened for access!")
            exit(1)


def main():
    print('Well, hello there, Mr. Ogator')
    WordGen().generate()


if __name__ == '__main__':
    main()
