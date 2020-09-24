import os

path = '/Users/welkin/Projects/eToxPred/Dataset/Nephrotoxic'

for root, dirs, files in os.walk(path):
    print("root = ", root, "\ndirs = ", dirs, "\nfiles = ", files)

file_all = open('nephrotoxic.txt', 'w')

for i in files:
    durgPath = root + "/" + i
    file_durg = open(durgPath)
    while True:
        line = file_durg.readline()
        if len(line) == 0:
            break
        content = line + " " + i[0:7] + "\n"
        print(content)
        file_all.write(content)
    file_durg.close()
file_all.close()
