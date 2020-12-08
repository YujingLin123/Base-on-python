import time
start = time.time()
import gzip
import glob

for i in glob.glob('*.fastq.gz'):
	with gzip.open(i,'rt') as fq:
		output_fasta = open("%s.fa"%i[:-9],'w')
		i = 0
		for line in fq:
			i += 1
			if i % 4 ==1:
				line_new = line[1:]
				output_fasta.write('>' + line_new)
			elif i % 4 == 2:
				output_fasta.write(line)
		output_fasta.close()
end = time.time()
print("used %s s" % str(end-start))
