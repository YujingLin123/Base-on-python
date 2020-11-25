import re
#input file
def file_input():
	fi = input("请输入文件的名称:")
	f = open(fi,"r",encoding="utf-8").read()
	return f
	
def get_seq(f):
	m = []
	line = f.split('\n')
	re_s=r'[^>]'
	while '' in line:
		line.remove('')
		for t in line:
			n = re.match(re_s,t)
			if n:
				m.append(len(t))
		return m

def get_id(f):
	id = []
	line = f.split('\n')
	while '' in line:
		line.remove('')
		for t in line:
			if '>' in t:
				id.append(t)
		return id
			
def list_dict(list1,list2):
	dic = dict(map(lambda x,y:[x,y], list1,list2))
	return dic

def file_output(dict):
	with open("seq.txt","w") as fo:
		fo.write(str(dict))
		fo.close()
		
def main():
	f = file_input()
	ID = get_id(f)
	Seq = get_seq(f)
	dic = list_dict(ID,Seq)	
	file_output(dic)

main()
