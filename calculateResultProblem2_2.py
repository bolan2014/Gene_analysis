#coding=utf-8
import sys, time
import prepareDataProblem2_1

#有病
target1 = 330
#没病
target2 = 340

rows = 1000
cols = 9445

fopr = open('third_copy_genotype.txt')

line_no = 0
cnt_to_analyse = 0

fopw = open('selectedColumnNumber.txt', 'w')

print 'analyse start...'

for line in open('third_copy_genotype.txt'):
    count_1 = prepareDataProblem2_1.init_acgt()
    count_0 = prepareDataProblem2_1.init_acgt()
    line = fopr.readline()
    line = line.strip().split(' ')
    index = 0
    while index < len(count_0)*2:
        if line[index] in count_0:
            count_0[line[index]] = line[index + 1]
        index += 1
    while index < len(line):
        if line[index] in count_1:
            count_1[line[index]] = line[index + 1]
        index += 1
    for k, v in count_0.items():
        if int(count_0[k]) < target2 and int(count_1[k]) >= target1:
            print "2 bingo [ " + str(line_no) + " ]"
            fopw.write(str(line_no)+'\n')
            cnt_to_analyse += 1
            break
    line_no += 1

print str(cnt_to_analyse) + " columns can be used to analysed." 
fopr.close()
fopw.close()

print 'analyse over...'
