#!/usr/bin/python

# SNAKES AHEAD!!!
# Created by ogator on 1/14/2017.
import json

from connectors import FileOutput, MongoOutput


class WordGenOutput:
    def __init__(self):
        self.output = None
        # parse config
        with open("connectors.json", mode='r', buffering=-1, encoding="utf8") as connectors_json:
            connectors = connectors_json.read()
        try:
            self.connectors = json.loads(connectors)
        except (ValueError, KeyError, TypeError):
            print("connectors.json config not found, aborting")
            exit(1)
        return

    def get_connector_options(self):
        return self.connectors.keys()

    def init_output_connector(self, con_name):
        config = self.connectors[con_name]
        if config["type"] == "file":
            self.output = FileOutput(config)
        elif config["type"] == "mongodb":
            self.output = MongoOutput(config)
        else:
            raise NotImplementedError("Connector not implemented!")

    def save(self, document):
        self.output.save(document)
