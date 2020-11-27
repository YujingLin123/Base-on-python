#get sequence that is a special seq length seq

import re
import pandas as pd
import numpy as np
#input file
def file_input():
	fi = input("请输入文件的名称:")
	f = open(fi,"r",encoding="utf-8").read()
	return f

#get sequence id and base 
def get_len(f):
	id = []
	seq = []
	re_s = r'[^>]'
	line = f.split('\n')
	while '' in line:
		line.remove('')
		for t in line:
			n = re.match(re_s,t)
			if n:
				seq.append(t)
		for t in line:
			if '>' in t:
				id.append(t)
		return id,seq

#create dict, including sequence id and base
def list_dict(id,seq):
	dict_seq = dict(map(lambda x,y:[x,y], id,seq))
	return dict_seq

#get length >= 10 sequence in test sequece.fa, u could change the parameter
def dic_seq(dict_seq):
	keys = []
	values = []
	for key, value in dict_seq.items():
		if len(value) >= 10:
			keys.append(key)
			values.append(value)
	return keys,values

#create new dict
def list_dict_seq(keys,values):
	dict_data = dict(map(lambda x,y:[x,y], keys,values))
	ln_seq = [dict_data]
	return ln_seq

#output file
def read_csv(ln_seq):
	df = pd.DataFrame(ln_seq)
	data = df.values
	index1 = list(df.keys())
	data = list(map(list,zip(*data)))
	data = pd.DataFrame(data,index = index1)
	data.to_csv('seq.fa',header = 0,sep='\n')


def main():
	f = file_input()
	id,seq = get_len(f)
	dic = list_dict(id,seq)
	keys,values = dic_seq(dic)
	ln_seq = list_dict_seq(keys,values)
	read_csv(ln_seq)
	
main()
