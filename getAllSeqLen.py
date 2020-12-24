import re
import pandas as pd
#input file
def file_input():
	fi = input("File Name:")
	f = open(fi,"r",encoding="utf-8").read()
	return f

def get_len(f):
	id = []
	m = [] “
	dict = {}
	re_s = r'[^>]'
	line = f.split('\n')
	while '' in line:
		line.remove('')
		for t in line:
			n = re.match(re_s,t)
			if n:
				m.append(len(t))
		for t in line:
			if '>' in t:
				id.append(t)
		return [id,m]
				
def list_dict(list1,list2):
	dic = dict(map(lambda x,y:[x,y], list1,list2))
	dic_data = [dic]
	return dic_data

def read_csv(dict_data):
	df = pd.DataFrame(dict_data)
	data = df.values
	index1 = list(df.keys())
	data = list(map(list,zip(*data)))
	data = pd.DataFrame(data,index = index1)
	data.to_csv('compdata.csv',header = 0)
		
def main():
	f = file_input()
	id,m = get_len(f)
	dic_data = list_dict(id,m)	
	read_csv(dic_data)

main()
