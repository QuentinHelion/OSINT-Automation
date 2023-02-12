cd OSINT-Automation/lib
git clone git@github.com:laramies/theHarvester.git
git clone git@github.com:rbsec/dnscan.git
cd ../..

python3 -m pip install -r OSINT-Automation/lib/theHarvester/requirements/base.txt
# echo "install completed"
# cd OSINT-Automation/lib/theHarvester
# python3 theHarvester.py -h
