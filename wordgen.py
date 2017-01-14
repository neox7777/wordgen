#!/usr/bin/python
# -*- coding: utf-8 -*-
# SNAKES AHEAD!!!
# Created by ogator on 1/11/2017.
import argparse
import os
import menu
import time
from wordgenoutput import WordGenOutput


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
        parser.add_argument('--app', dest='app_prefix',
                            help='Optional application key')
        parser.add_argument('--buffer', dest='buffer', type=int,
                            help='Buffer size, default 100k')
        args = parser.parse_args()
        self.username = args.username
        self.password_file = args.password_file
        self.delimiter = args.delimiter
        self.app_prefix = args.app_prefix
        self.output_module = WordGenOutput()
        self.buff_size = args.buffer if args.buffer else 100000
        self.buffer = []
        self.show_connectors_menu()

    def show_connectors_menu(self):
        # format the menu
        con_options = []
        for con in self.output_module.get_connector_options():
            con_options.append({"name": con, "function": self.init_connector})
        # Choose the connector menu
        con_menu = menu.Menu("Choose output connector")
        con_menu.addOptions(con_options)
        con_menu.open()

    def init_connector(self, con):
        self.output_module.init_output_connector(con)
        return

    def generate(self):
        print("Starting: ", time.strftime("%H:%M:%S"))
        # check for existence
        if os.access(path=self.password_file, mode=os.R_OK):
            with open(self.password_file, "r", buffering=1) as pass_file:
                for line in pass_file:
                    output = {"username": self.username, "delimiter": self.delimiter, "password": line.rstrip('\n')}
                    if self.app_prefix:
                        output["application"] = self.app_prefix
                    self.buffer.append(output)
                    if line is None:
                        return
                    if len(self.buffer) >= self.buff_size:
                        self.output_module.save(self.buffer)
                        self.buffer.clear()
                pass_file.close()
                # save the remaining buffer if any
                if len(self.buffer) > 0:
                    self.output_module.save(self.buffer)
                print("Done! ", time.strftime("%H:%M:%S"))
        else:
            print("Password file cannot be opened for access!")
            exit(1)


def main():
    print('Well, hello there, Mr. Ogator')
    WordGen().generate()


if __name__ == '__main__':
    main()
