import os

class TheHarvester:
    def __init__(self, target, source="yahoo"):
        self.target = target
        self.source = source

    def run(self):
        command = "python3 lib/theHarvester/theHarvester.py -d " + self.target + " -b " + self.source + " -f results/theHarvester/" + self.target + ".txt"
        os.system(command)
