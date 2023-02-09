import os

class TheHarvester:
    def __init__(self, target, limit=500, source="google"):
        self.target = target
        self.limit = limit
        self.source = source

    def run(self):
        os.system(f"theharvester -d {self.target} -l {self.limit} -b {self.source}")
