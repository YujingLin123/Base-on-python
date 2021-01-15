import time
start = time.time()
import scipy.stats as stats
import pandas as pd
import glob 

def read_Enrichment():
	for enrich in glob.glob("GO.txt"):
		f = pd.read_table(enrich,sep="\t",header='infer')
		df = pd.DataFrame(f)
		df.columns = ["GO_term","study","all_study","pop","all_pop"]
	return df

"""
	GO1	not in GO1
a	study	pop-study
b	all_study-study	all_pop-all_study-(pop-study)

	GO1 	not in GO1
	a	b
	c	d
stats.fisher_exact([[a,b],[c,d]])
"""

def fisher_Enrichment(df):
	df['a'] = df['study']
	df['b'] = df['pop'] - df['study']
	df['c'] = df['all_study']-df['study']
	df['d'] = df['all_pop']-df['all_study']-df['pop']+df['study']
	pvalues =[]
	for i in range(0,len(df)):
		oddsration,pvalue = stats.fisher_exact([[df['a'][i],df['b'][i]],[df['c'][i],df['d'][i]]])
		pvalues.append(pvalue)
		f1 = pd.DataFrame(pvalues)
	return f1

def save_file(f1,df):
	formater="{0:.10f}".format
	f1 = f1.applymap(formater)
	df["pvalue"] = f1
	p_uncorrected = pd.DataFrame(df)
	p_uncorrected.to_csv('Enrichment_Pvalue.txt',sep='\t',index=None)
	
def main():
	df = read_Enrichment()
	f1 = fisher_Enrichment(df)
	save_file(f1,df)
	
main()
	
end = time.time()
print("used %s s" % str(end-start))

"""
#input
localization    1097    10929   2447    26715
establishment of localization   1082    10929   2415    26715
transport       1077    10929   2407    26715
transmembrane transport 507     10929   1088    26715
potassium ion transport 45      10929   72      26715
ion transport   358     10929   760     26715
lipid metabolic process 346     10929   733     26715
protein N-linked glycosylation  10      10929   11      26715
phospholipid dephosphorylation  16      10929   21      26715
phosphatidylinositol dephosphorylation  16      10929   21      26715
intracellular signal transduction       137     10929   273     26715
phosphorelay signal transduction system 48      10929   83      26715
regulation of catalytic activity        97      10929   187     26715
cellular lipid metabolic process        185     10929   382     26715

#Result
GO_term study   all_study       pop     all_pop a       b       c       d       pvalue
establishment of localization   1082    10929   2415    26715   1082    1333    9847    14453   0.0000492815
transport       1077    10929   2407    26715   1077    1330    9852    14456   0.0000693814
transmembrane transport 507     10929   1088    26715   507     581     10422   15205   0.0001068882
potassium ion transport 45      10929   72      26715   45      27      10884   15759   0.0002651792
ion transport   358     10929   760     26715   358     402     10571   15384   0.0004932536
lipid metabolic process 346     10929   733     26715   346     387     10583   15399   0.0005201841
protein N-linked glycosylation  10      10929   11      26715   10      1       10919   15785   0.0009052159
phospholipid dephosphorylation  16      10929   21      26715   16      5       10913   15781   0.0013593364
phosphatidylinositol dephosphorylation  16      10929   21      26715   16      5       10913   15781   0.0013593364
intracellular signal transduction       137     10929   273     26715   137     136     10792   15650   0.0019471613
phosphorelay signal transduction system 48      10929   83      26715   48      35      10881   15751   0.0023387259
regulation of catalytic activity        97      10929   187     26715   97      90      10832   15696   0.0027439553
cellular lipid metabolic process        185     10929   382     26715   185     197     10744   15589   0.0027973568


"""
