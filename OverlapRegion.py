import time
start = time.time()
import pandas as pd
import numpy as np
import glob


def read_bed1():
	for peak in glob.glob('*_background.bed'):
		f1 = pd.read_table(peak,sep='\t',header=None)
		df1 = pd.DataFrame(f1)
		df1.columns = ['chr','start','end']
	return df1

def read_bed2():
	for peak in glob.glob('*_input.bed'):
		f2 = pd.read_table(peak,sep='\t',header=None)
		df2 = pd.DataFrame(f2)
		df2.columns = ['chr','start','end']
	return df2

def OverlapRegion(df1,df2):
	d = pd.merge(df1,df2,on="chr")
	d0 = d[(d['start_y'] >= d['start_x']) & (d['start_y'] <= d['end_x']) & (d['end_y'] > d['end_x'])].drop_duplicates()
	d0_overlap = (d0['end_x'] - d0['start_y'])/(d0['end_x']-d0['start_x']+1)
	d0["Overlap"] = d0_overlap
	
	d1 = d[(d['start_y'] >= d['start_x']) & (d['start_y'] <= d['end_x']) & (d['end_y'] >= d['start_x']) & (d['end_y'] <= d['end_x'])].drop_duplicates()
	d1_overlap = (d1['end_y']-d1['start_y'])/(d1['end_x']-d1['start_x']+1)
	d1["Overlap"] = d1_overlap
	
	d2 = d[(d['end_y'] >= d['start_x']) & (d['start_y'] < d['start_x'])].drop_duplicates()
	d2_overlap = (d2['end_y']-d2['start_x'])/(d2['end_x']-d2['start_x']+1)
	d2["Overlap"] = d2_overlap
	
	df = d1.append(d2)
	df = d0.append(df)
	
	df0 = df.groupby(by=['chr','start_x','end_x'])['Overlap'].mean().reset_index()
	return df0
	
def save_file(df0):
	OR = pd.DataFrame(df0)
	OR.to_csv('OverlapRegion.txt',sep='\t',index=None)

def main():
	df1 = read_bed1()
	df2 = read_bed2()
	df0 = OverlapRegion(df1,df2)
	save_file(df0)

main()
	
end = time.time()
print("used %s s" % str(end-start))
