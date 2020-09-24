import csv

# Path of the csv files
path = "Datasets/Genotoxic Datasets"
fileName = "Genotoxicity OASIS"
fullPath = path + "/" + fileName

with open(fullPath + ".csv", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    organizeFile = open(fullPath + ".smi", 'w')
    for row in reader:
        print(row)
        organizeFile.write(row['SMILES'] + " " + row['CAS Number'] + "\n")
    organizeFile.close()