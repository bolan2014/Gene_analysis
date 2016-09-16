import sys
import pandas as pd

geneDict = {'AA': '00000000001',\
			'TT': '0000000010',\
			'CC': '0000000100',\
			'GG': '0000001000',\
			'AT': '0000010000',	'TA': '0000010000',\
			'AC': '0000100000',	'CA': '0000100000',\
			'AG': '0001000000',	'GA': '0001000000',\
			'TC': '0010000000',	'CT': '0010000000',\
			'TG': '0100000000',	'GT': '0100000000',\
			'CG': '1000000000', 'GC': '1000000000'\
}

fname = sys.argv[1]
#df = pd.read_csv(fname, sep=' ')

#print len(df)
#print df.head()
#a = df.index[1]
#b = df.columns[1]
#print df[b][0]

def encode_gene(fname):
	fr, i = open(fname), 0
	fw = open('encoded_' + fname, 'w')
	for line in fr:
		if i > 0:
			tmp = line.strip().split(' ')
			for j in range(len(tmp)):
				if tmp[j] in geneDict:
					tmp[j] = geneDict[tmp[j]]
			fw.write(' '.join(tmp) + '\n')
		else:
			fw.write(line)
		i += 1

encode_gene(fname)

print 'complete'
#df.to_csv('encoded_' + fname)
