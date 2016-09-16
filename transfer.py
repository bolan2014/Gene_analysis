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
			'CG': '1000000000', 'GC': '1000000000' \
}

fname = sys.argv[1]
df = pd.read_csv(fname, sep=' ')

print len(df)
#print df.head()
#a = df.index[1]
#b = df.columns[1]
#print df[b][0]

def encode_gene(data, geneDict):
	for c in data.columns:
		for i in data.index:
			data[c][i] = geneDict[data[c][i]]
	return data

df = encode_gene(df, geneDict)

df.to_csv('encoded_' + fname)
