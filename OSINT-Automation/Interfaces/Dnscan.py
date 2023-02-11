import subprocess
import os

class Dnscan:
    def __init__(self, domain):
        self.domain = domain
        file = domain + '.txt'
        path = "Results/Dnscan"
        self.output_file = os.path.join(path,file)
        self.py_path = "lib/dnscan/dnscan.py"
    
    def run(self):
        subprocess.call(['python3', self.py_path, '-d', self.domain, '-o', self.output_file ])