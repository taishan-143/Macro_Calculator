import json


class Persistence:
    def __init__(self):
        self.filepath = ""

    def save_data(self, database, filepath, name, data_type, data):
        database[name][data_type] = data
        with open(filepath, 'w') as outfile:
            json.dump(database, outfile, indent=2)

    def load_data(self, filepath):
        with open(filepath, 'r') as infile:
            return json.load(infile)




