import os 
import sys 
import csv
from urllib.request import urlretrieve

#File containing comma-seperated list of PDB IDs
pdb_codes_file = 'pdbcodes.csv'
#Folder to download to 
download_folder = 'PDB/'
compressed = True

#Read the PDB IDs from the input file
with open(pdb_codes_file) as f:
    pdb_codes = f.read().split(',')
    #Alternatively, hard code the PDB IDs:
    #pdb_codes = ['1LS6', '2D06', '3QVU']
print(pdb_codes)

#Ensure download file exists
try:
    os.makedirs(download_folder)
except OSError as e:
    pass

for pdb_code in pdb_codes:
    filename= '%s.pdb' % pdb_code[:4]
    #if compressed:
        #filename = '%s.gz' % filename
    url = 'https://files.rcsb.org/download/%s' % filename
    destination_file = os.path.join(download_folder, filename)
        #download file 
    urlretrieve(url, destination_file)