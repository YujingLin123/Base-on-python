import re
#input file
def file_input():
	fi = input("请输入文件的名称:")
	f = open(fi,"r",encoding="utf-8").read()
	return f
#get sequence length
def get_len(f):
	m = []
	id = []
	dict = {}
	line = f.split('\n')
	re_s = r'[^>]'
	while '' in line:
		line.remove('')
		for t in line:
			n = re.match(re_s,t)
			if n:
				m.append(len(t))
		for t in line:
			if '>' in t:
				id.append(t)		
		for i in range(len(id)):
			dict[id[i]] = m[i]
			for key,value in dict.items():
				return "{}:{}".format(key,value)
#output file
def file_output(dict):
	with open("seq.txt","w") as fo:
		fo.write(str(dict))
		fo.close()
		
def main():
	f = file_input()
	dict = get_len(f)
	file_output(dict)

main()
