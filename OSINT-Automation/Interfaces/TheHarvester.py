import os

class TheHarvester:
    def __init__(self, target, source="yahoo"):
        self.target = target
        self.source = source

    def run(self):
        command = "python3 OSINT-Automation/lib/theHarvester/theHarvester.py -d " + self.target + " -b " + self.source + " -f OSINT-Automation/results/theHarvester/" + self.target + ".txt"
        os.system(command)
