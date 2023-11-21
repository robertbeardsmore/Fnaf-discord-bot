import json

class FileHandler:
    def __init__(self):
        self.name = "data.json"

    def write(self, dictionary):
        with open(self.name, "w") as file:
            json.dump(dictionary, file)

    def read(self):
        with open(self.name) as file:
            dictionary = json.load(file)
            print(dictionary)