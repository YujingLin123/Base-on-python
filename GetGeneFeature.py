import time
start = time.time()
import pandas as pd
import numpy as np
import glob

def read_gff3():
	for gff in glob.glob('*.gff3'):
		f1 = pd.read_table(gff,sep='\t',header=None)
		df1 = pd.DataFrame(f1)
		df1.columns = ['chr','Database','feature','start','end','label1','strand','label2','info']
	return df1

def gene_up(df1):
	df_gene = df1[df1['feature'].str.contains('gene')]
	df_gene = df_gene[['chr','start','end','strand']]
	
	#正链基因上游
	df1_UpGene = df_gene[df_gene['strand']=="+"]
	df1_UpGene = df1_UpGene[df1_UpGene['start'] > 2000]
	df1_UpGene['start_new'] = df1_UpGene['start'] - 2000 + 1
	df1_UpGene = df1_UpGene.drop('end',axis=1)
	df1_UpGene = df1_UpGene[['chr','start_new','start']]
	df1_UpGene.columns = ['chr','start','end']

	#负链基因上游
	df2_UpGene = df_gene[df_gene['strand']=="-"]
	df2_UpGene['end_new'] = df2_UpGene['end'] + 2000
	df2_UpGene = df2_UpGene.drop('start',axis=1)
	df2_UpGene = df2_UpGene[['chr','end','end_new']]
	df2_UpGene.columns = ['chr','start','end']
	
	#所有基因上游
	dfup = df1_UpGene.append(df2_UpGene)
	
	return dfup

def gene_down(df1):
	df_gene = df1[df1['feature'].str.contains('gene')]
	df_gene = df_gene[['chr','start','end','strand']]
	
	#正链基因下游
	df1_DownGene = df_gene[df_gene['strand']=="+"]
	df1_DownGene['end_new'] = df1_DownGene['end'] + 2000
	df1_DownGene = df1_DownGene.drop('start',axis=1)
	df1_DownGene = df1_DownGene[['chr','end','end_new']]
	df1_DownGene.columns = ['chr','start','end']
	
	#负链基因下游
	df2_DownGene = df_gene[df_gene['strand']=="-"]
	df2_DownGene = df2_DownGene[df2_DownGene['start'] > 2000]
	df2_DownGene['start_new'] = df2_DownGene['start'] - 2000 + 1
	df2_DownGene = df2_DownGene.drop('end',axis=1)
	df2_DownGene = df2_DownGene[['chr','start_new','start']]
	df2_DownGene.columns = ['chr','start','end']
		
	#所有基因下游
	dfdown = df1_DownGene.append(df2_DownGene)
	
	return dfdown
	
def gene(df1):
	#所有基因区域
	df_gene = df1[df1['feature'].str.contains('gene')]
	dfgene = df_gene[['chr','start','end']]
	return dfgene
	
def save_file(dfup,dfdown,dfgene):
	up = pd.DataFrame(dfup)
	down = pd.DataFrame(dfdown)
	gene = pd.DataFrame(dfgene)
	up.to_csv('UpGeneRegion.txt',sep='\t',index=None)
	down.to_csv('DownGeneRegion.txt',sep='\t',index=None)
	gene.to_csv('GeneRegion.txt',sep='\t',index=None)

def main():
	df1 = read_gff3()
	dfup = gene_up(df1)
	dfdown = gene_down(df1)
	dfgene = gene(df1)
	save_file(dfup,dfdown,dfgene)

main()
	
end = time.time()
print("used %s s" % str(end-start))
