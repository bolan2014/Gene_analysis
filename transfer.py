import sys
import pandas as pd

geneDict = {'AA': '0000',\
			'TT': '0001',\
			'CC': '0010',\
			'GG': '0011',\
			'AT': '0100', 'TA': '0100',\
			'AC': '0101', 'CA': '0101',\
			'AG': '0110', 'GA': '0110',\
			'TC': '0111', 'CT': '0111',\
			'TG': '1000', 'GT': '1000',\
			'CG': '1001', 'GC': '1001'\
}

fname = sys.argv[1]
rows, cols = 1000, 9445
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
				else:
					tmp[j] = '1111'
			fw.write(' '.join(tmp) + '\n')
		else:
			fw.write(line)
		i += 1

def recover(fname):
	fr = open(fname)
	gList, i = [[] for i in range(cols)], 0 # cols * rows
	for line in fr:
		if i > 0:
			tmp = line.strip().split(' ')
			for j in range(len(tmp)):
				if tmp[j] in geneDict.values():
					gList[j].append(int(tmp[j], 2) + 1)
				else:
					gList[j].append(15)
		i += 1
	return gList

def dispersion(gList):
	avg, std = [], []
	for i in range(cols):
		tmp, temp = 0, 0
		for j in range(rows):
			tmp += gList[i][j]
			temp += gList[i][j] ** 2
		average = float(tmp) / rows
		avg.append(average)
		std.append(abs(temp / rows - average ** 2) ** 0.5)
	fw = open('rst.txt', 'w')
	for i in range(len(avg)):
		cv = std[i] / avg[i] * 100
		fw.write(repr(cv)[:4] + '%\n')
		#if cv < 100:
		#	print cv


		 
if __name__ == '__main__':
	#encode_gene(fname)
	gList = recover(fname)
	dispersion(gList)

	print 'complete'
#df.to_csv('encoded_' + fname)
