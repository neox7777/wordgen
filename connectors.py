#!/usr/bin/python

# SNAKES AHEAD!!!
# Created by ogator on 1/14/2017.
import os
from pymongo import MongoClient


class FileOutput:
    def __init__(self, config):
        if not config["name"]:
            raise ValueError("File name is not present in the config")
        self.file_base = config["name"]
        return

    def save(self, doc_array):
        file_name = ""
        if "application" in doc_array[0]:
            filename, file_extension = os.path.splitext(self.file_base)
            file_name += filename + "_" + doc_array[0]["application"] + file_extension
        else:
            file_name = self.file_base
        print("Saving: ", len(doc_array), " documents")
        with open(file_name, "a") as out_file:
            for line in doc_array:
                out_file.write(line["username"] + line["delimiter"] + line["password"] + "\n")
            out_file.close()
        return


class MongoOutput:
    def __init__(self, config):
        if not config["host"]:
            raise AttributeError("Host is not present in the config")
        if not config["port"]:
            raise ValueError("Port is not present in the config")
        if not config["username"]:
            raise ValueError("Username is not present in the config")
        if not config["password"]:
            raise ValueError("Password is not present in the config")
        if not config["database"]:
            raise ValueError("Database name is not present in the config")
        if not config["collection"]:
            raise ValueError("Collection name is not present in the config")
        self.config = config
        self.client = MongoClient("mongodb://" + config["username"] + ":" + config["password"] + "@" + config["host"]
                                  + ":" + str(config["port"]) + "/")
        return

    def save(self, doc_array):
        print("Saving: ", len(doc_array), " documents")
        db = self.client[self.config["database"]]
        col = db[self.config["collection"]]
        col.insert_many(doc_array)
        return
