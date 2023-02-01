import json

class equations:
    def writeEq(file, data):
        with open(file, 'w') as file:
            json.dump(data, file)
            
    def readEq(file):
        with open(file, 'r') as file:
            data = json.load(file)
             
        return data