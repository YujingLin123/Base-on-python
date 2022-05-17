from pathlib import Path
import re


path = Path()
for file in path.glob('*.fasta'):
    print(file)

f = open(file,'r', encoding='UTF-8')
datalist = []
matchPattern = re.compile(r'>')
while 1:
    line = f.readline()
    if not line:
        print("Read file End or Error")
        break
    elif matchPattern.search(line):
        pass
    else:
        datalist.append(line)
print(datalist)

#读取非ID的行

f = open(file,'r', encoding='UTF-8')
datalist = []
matchPattern = re.compile(r'>')
for line in f.readlines():
    if not matchPattern.search(line):
        print(line.strip())

#统计上述每一行的长度

f = open(file,'r', encoding='UTF-8')
datalist = []
matchPattern = re.compile(r'>')
for line in f.readlines():
    if not matchPattern.search(line):
        line = line.strip()
        line_len = len(line)
        print(f'{line}, {line_len}')

#对上述统计添加ID对应的长度
f = open(file,'r', encoding='UTF-8')
datalist = []
matchPattern = re.compile(r'>')
for line in f.readlines():
    line = line.strip()
    if line[0] == ">":
         id = re.split(r' ', line)[0]
         print('{}'.format(id))
    else:
        print('{}'.format(len(line)))

#修改1
#!/usr/bin/env python3
import os
import sys
import re

ms, infile, outfile = sys.argv

with open(outfile, 'w') as o:
    with open(infile) as f:
        for line in f:
            line = line.strip()
            if line[0] == ">":
                id = re.split(r' ', line)[0]
                o.write("{}".format(id))
            else:
                o.write("\t{}\n".format(len(line)))

#python fasta_len.py genome.fasta genoem.len.txt
"""output
>ID1	19
>ID2	22
"""

#修改2
import os,sys,re

ms, infile, outfile = sys.argv
#outfile = "file1.2.txt"

with open(outfile,'w') as o:
    with open(infile) as f:
        for line in f.readlines():
            line = line.strip()
            if line[0] != ">":
                o.write('{}\t{}'.format(len(line), line))
            else:
                o.write('\n{}\t'.format(line))
                
"""output
>ID1	19	AGCTACTATAAAATGCCCG
>ID2	22	ATCGTACTTTTAAACCCCCCCC
"""
