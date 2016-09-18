import sys

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

def fre_trans(fname):
	fr, cnt = open(fname), 0
	gList, gMat = [[] for i in range(cols)], []
	fw = open('encoded_myRst.txt', 'w')
	for line in fr:
		if cnt > 0:
			tmp = line.strip().split(' ')
			gMat.append(tmp)
			for j in range(len(tmp)):
				gList[j].append(tmp[j])
		else:
			fw.write(line)
		cnt += 1
	for i in range(cols):
		dick = {}
		for j in range(rows):
			if gList[i][j] not in dick:
				#dick[gList[i][j]] = 1
				dick[gList[i][j]] = len(dick) + 1
			#else:
			#	dick[gList[i][j]] += 1
		for k in range(rows):
			#gMat[k][i] = repr(float(dick[gMat[k][i]]) / rows)[:4]
			gMat[k][i] = repr(dick[gMat[k][i]])
	
	for i in range(rows):
		tmp = ' '.join(gMat[i])
		fw.write(tmp + '\n')

def recover(fname):
	fr = open(fname)
	gList, cnt = [[] for i in range(cols)], 0 # cols * rows
	for line in fr:
		if cnt > 0:
			tmp = line.strip().split(' ')
			for j in range(len(tmp)):
				#if tmp[j] in geneDict.values():
					#gList[j].append(int(tmp[j], 2) + 1)
				#else:
				#	gList[j].append(15)
				gList[j].append(float(tmp[j]))
		cnt += 1
	return gList

def dispersion(gList):
	avg, std = [], []
	print len(gList), len(gList[0])
	for i in range(cols):
		average, tmp = sum(gList[i]) / rows, 0
		for j in range(rows):
			tmp += (gList[i][j] - average) ** 2
		avg.append(average)
		std.append((tmp / rows) ** 0.5)
	fw = open('rst.txt', 'w')
	for i in range(len(avg)):
		cv = std[i] / avg[i] * 100
		fw.write(repr(cv)[:4] + '%\n')
		#if cv < 100:
		#	print cv


		 
if __name__ == '__main__':
	#encode_gene(fname)
	#gList = recover(fname)
	#dispersion(gList)
	fre_trans(fname)

	print 'complete'
#df.to_csv('encoded_' + fname)
