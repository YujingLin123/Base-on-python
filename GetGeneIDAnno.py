import time
start = time.time()
import pandas as pd
import numpy as np
import glob

def read_Anno():
	for Anno in glob.glob("*_peaks_anno.PeakAnno"):
		f1 = pd.read_table(Anno,sep="\t",header='infer')
		df1 = pd.DataFrame(f1)
	return df1

def GeneId(df1):
	df1_gene = df1['geneId']
	return df1_gene
	
def save_file(df1_gene):
	df1_gene = pd.DataFrame(df1_gene)
	df1_gene.to_csv('Gene.txt',sep='\t',index=None)
	
def main():
	df1 = read_Anno()
	df1_gene = GeneId(df1)
	save_file(df1_gene)
	
main()
