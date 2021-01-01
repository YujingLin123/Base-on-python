###读取文件
import pandas as pd
import numpy as np
import glob

def read_file():
	for peak in glob.glob('*.bed'):
		dt = pd.read_table(peak,sep='\t',header=None)
		dt[4] = dt[2] - dt[1]
		dt.columns = ['chr','start','end','length']
	return dt

###构建函数
def PeakNumLen(dt):
	df = pd.DataFrame(dt)
	d0 = df[(df['length'] < 200)&(df['length'] >= 0)].count()['length']
	d1 = df[(df['length'] < 400)&(df['length'] >= 200)].count()['length']
	d2 = df[(df['length'] < 600)&(df['length'] >= 400)].count()['length']	
	d3 = df[(df['length'] < 800)&(df['length'] >= 600)].count()['length']
	d4 = df[(df['length'] < 1000)&(df['length'] >= 800)].count()['length']
	d5 = df[(df['length'] < 1200)&(df['length'] >= 1000)].count()['length']
	d6 = df[(df['length'] < 1400)&(df['length'] >= 1200)].count()['length']
	d7 = df[(df['length'] < 1600)&(df['length'] >= 1400)].count()['length']
	d8 = df[(df['length'] < 1800)&(df['length'] >= 1600)].count()['length']
	d9 = df[(df['length'] < 2000)&(df['length'] >= 1800)].count()['length']
	d10 = df[df['length'] >= 2000].count()['length']
	dict = {}
	dict = [{'[0-200]':d0,'[200-400]':d1,'[400-600]':d2,'[600-800]':d3,'[800-1000]':d4,'[1000-1200]':d5,'[1200-1400]':d6,'[1400-1600]':d7,'[1600-1800]':d8,'[1800-2000]':d9,'[>2000]':d10}]
	return dict

###保存文件
def save_file(dict):
	Peak = pd.DataFrame(dict)
	data = Peak.values
	index1 = list(Peak.keys())
	data = list(map(list,zip(*data)))
	data = pd.DataFrame(data,index=index1)
	data.columns=['Peak Number']
	data.to_csv('PeakNumLen.txt',sep='\t')

def main():
	dt = read_file()
	dict = PeakNumLen(dt)
	save_file(dict)

main()

"""
Input:
Chr00	78214	78354
Chr00	102902	103058
Chr00	103338	103727
Chr00	103338	103727
Chr00	107819	107985
Chr00	108634	108847
Chr00	175745	176174
Chr00	182837	182990
Chr00	419067	419250
Chr00	544550	544863

Result:
        Peak Number
[0-200] 11306
[200-400]       13501
[400-600]       1302
[600-800]       194
[800-1000]      20
[1000-1200]     9
[1200-1400]     2
[1400-1600]     0
[1600-1800]     0
[1800-2000]     0
[>2000] 0

"""
