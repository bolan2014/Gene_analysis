#coding=utf-8
import sys, time
import prepareData

def output_cols(target1, target2):
    rows = 1000
    cols = 9445

    fopr = open('../third_copy_genotype.txt')

    line_no = 0
    cnt_to_analyse = 0
    line_nos = []

    for line in open('../third_copy_genotype.txt'):
        count_1 = prepareData.init_acgt()
        count_0 = prepareData.init_acgt()
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
                # print line_no
                line_nos.append(str(line_no))
                cnt_to_analyse += 1
                break
        line_no += 1

# print "all the columns can be used to analysed [ " + str(cnt_to_analyse) + " ]"
# print ",".join(line_nos)
    fopr.close()
    return ",".join(line_nos)

# print 'analyse over...'
