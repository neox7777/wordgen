#!/usr/bin/python

# SNAKES AHEAD!!!
# Created by ogator on 1/14/2017.
import os
from pymongo import MongoClient


class FileOutput:
    def __init__(self, config):
        if "name" not in config:
            raise AttributeError("File name is not present in the config")
        self.file_base = config["name"]
        return

    def save(self, doc_array):
        file_name = ""
        if "application" in doc_array[0]:
            filename, file_extension = os.path.splitext(self.file_base)
            file_name += filename + "_" + doc_array[0]["application"] + file_extension
        else:
            file_name = self.file_base
        with open(file_name, "a") as out_file:
            for line in doc_array:
                out_file.write(line["username"] + line["delimiter"] + line["password"] + "\n")
            out_file.close()
        return


class MongoOutput:
    def __init__(self, config):
        if "host" not in config:
            raise AttributeError("Host is not present in the config")
        if "port" not in config:
            raise AttributeError("Port is not present in the config")
        if "username" not in config:
            raise AttributeError("Username is not present in the config")
        if "password" not in config:
            raise AttributeError("Password is not present in the config")
        if "database" not in config:
            raise AttributeError("Database name is not present in the config")
        if "collection" not in config:
            raise AttributeError("Collection name is not present in the config")
        self.config = config
        self.client = MongoClient("mongodb://" + config["username"] + ":" + config["password"] + "@" + config["host"]
                                  + ":" + str(config["port"]) + "/")
        return

    def save(self, doc_array):
        db = self.client[self.config["database"]]
        col = db[self.config["collection"]]
        col.insert_many(doc_array)
        return
