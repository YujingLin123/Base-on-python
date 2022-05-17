from pathlib import Path
import re


path = Path()
for file in path.glob('*.fasta'):
    print(file)


f = open(file,'r', encoding='UTF-8')
datalist = []
matchPattern = re.compile(r'>')
count = 0
for line in f.readlines():
    if not matchPattern.search(line):
        print(line.strip())
