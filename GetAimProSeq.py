import pandas as pd
import numpy as np
import re
from Bio import SeqIO
import glob as glob
import time
start = time.time()

def read_geneid():
	for geneid in glob.glob("*_AnnoGeneid.txt"):
		f1 = open(geneid,"r+").read()
		f1 = f1.split('\n')
		f1 = list(set(f1))
		f1 = ['>' + x for x in f1]
	return f1 
	
def get_id():
	for pro in glob.glob("*.fasta"):
		f2 = open(pro,"r+").read()
		name=f2.split('>')
		df = pd.DataFrame(name)
		df = df.drop(index=0)
		df = ">" + df[0]
		id = df.str.split('\n').str.get(0)
	return id

def get_seq():
	seqs = [str(fa.seq) for fa in SeqIO.parse("GDDH13_1-1_prot.fasta",  "fasta")]
	return seqs
		
def list_dict(id,seqs):
	dict_seq = dict(map(lambda x,y:[x,y], id,seqs))
	return dict_seq

def get_AimSeq(f1,dict_seq):
	Seq = {}	
	for i in dict_seq.keys():
		if i in f1:
			Seq[i] = dict_seq[i]
			df = pd.DataFrame(Seq,index=Seq.keys()).drop_duplicates()
			data = df.values
			index1 = list(df.keys())
			data = list(map(list,zip(*data)))
			data = pd.DataFrame(data,index = index1)
	return data

def read_csv(data):
	data.to_csv('pro.fasta',header = 0,sep='\n')
		
def main():
	f1 = read_geneid()
	id = get_id()
	seqs = get_seq()
	dict_seq = list_dict(id,seqs)
	data = get_AimSeq(f1,dict_seq)
	read_csv(data)
	
main()
	
end = time.time()
print("used %s s" % str(end-start))
