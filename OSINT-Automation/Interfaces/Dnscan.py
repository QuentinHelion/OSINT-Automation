import subprocess
import os

class Dnscan:
    def __init__(self, domain):
        self.domain = domain
        directory = domain + '.txt'
        path = "OSINT-Automation/Results/Dnscan"
        self.output_file = os.path.join(path,directory)
        self.py_path = "OSINT-Automation/lib/dnscan/dnscan.py"
    
    def run(self):
        subprocess.call(['python3', self.py_path, '-d', self.domain, '-o', self.output_file ])