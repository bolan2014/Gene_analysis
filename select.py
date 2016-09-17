import sys


a = {}

fr, cnt = open(sys.argv[1]), 0

for num in fr:
	tmp = num.strip()
	a[repr(cnt)] = float(tmp[:-1])
	cnt += 1

b = sorted(a.iteritems(), key=lambda d:d[1], reverse = True)

print b[:10], len(b)


desList = []

for i in range(500):
	desList.append(int(b[i][0]))

print desList[:11]

rows, cols = 1001, 9445

fr = open('myRst.txt')
gList = [[] for i in range(cols)]
for line in fr:
	tmp = line.strip().split(' ')
	for j in range(cols):
		gList[j].append(tmp[j])

gMat = [[] for i in range(rows)]
for des in desList:
	for i in range(rows):
		gMat[i].append(gList[des][i])
print len(gMat[0])
fw = open('raw_top500.txt', 'w')
for i in range(rows):
	tmp = ' '.join(gMat[i])
	fw.write(tmp + '\n')

print 'complete.'
	




