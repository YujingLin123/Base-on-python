###get the number of A(G C T) in sequence fasta

import re
import pandas as pd
import numpy as np
#input file
def file_input():
	fi = input("File name:")
	f = open(fi,"r",encoding="utf-8").read()
	return f

def get_id(f):
	id = []
	line = f.split('\n')
	while '' in line:
		line.remove('')
		for t in line:
			if '>' in t:
				id.append(t)
		return id
		
def get_seq(f):
	seq = []
	re_s = r'[^>]'
	line = f.split('\n')
	while '' in line:
		line.remove('')
		for t in line:
			n = re.match(re_s,t)
			if n:
				seq.append(t)
		return seq
				
def base(x):
	dic = {}
	for c in x:
		dic[c] = dic.get(c,0) + 1
	return dic

def base_num(seq):
	num = list(map(base,seq))
	return num
	
def save_file(num,id):
	df = pd.DataFrame(num,index=id)
	df.to_csv('seq_base.csv',sep='\t')
	
def main():
	f = file_input()
	id = get_id(f)
	seq = get_seq(f)
	num = base_num(seq)
	save_file(num,id)
	
main()
