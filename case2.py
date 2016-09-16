#coding=utf-8
import sys, time

def init_acgt():
    count_acgt = {"AA":0, "AC":0, "AG":0, "AT":0, "CC":0, "CG":0, "CT":0, "GG":0, "GT":0, "TT":0, }
    return count_acgt

def read_genotype(file_name):
    print 'start read file:' + file_name + '...'
    matrix = []
    cur_no = 1
    fopr = open(file_name)
    for line in open(file_name):
        line = fopr.readline()
        if cur_no == 1:
            cur_no += 1
            continue
        if line != "" or line is not None:
            line = line.strip().split(' ')
            print 'line['+str(cur_no)+']'
            cur_no += 1
            matrix.append(line)
    print 'finish read file:' + file_name + '...'
    print 'matrix size = ' + str(len(matrix))
    #time.sleep(5)
    return matrix

def read_phenotype(file_name):
    print 'start read file:' + file_name + '...'
    matrix = []
    cur_no = 1
    fopr = open(file_name)
    for line in open(file_name):
        line = fopr.readline()
        if line != "" or line is not None:
            line = line.strip()
            print 'line['+str(cur_no)+']'
            cur_no += 1
            matrix.append(line)
    print 'finish read file:' + file_name + '...'
    print 'matrix size = ' + str(len(matrix))
    #time.sleep(5)
    return matrix

if __name__ == "__main__":

    count = []
    rows = 1000
    cols = 9445
    for i in range(rows):
        count.append([])
        for j in range(cols):
            count[i].append(0)

    genotype = read_genotype('genotype.dat')
    phenotype = read_phenotype('phenotype.txt')

    for i in range(cols):
        print 'solving: ' + str(i)
        count_cols1 = init_acgt()
        count_cols0 = init_acgt()
        for j in range(rows):
            cur = genotype[j][i]
            if phenotype[j] == '1':
                if cur in count_cols1:
                    count_cols1[cur] += 1
                elif cur[::-1] in count_cols1:
                    cur = cur[::-1]
                    count_cols1[cur] += 1
                else:
                    print 'col:'+str(i)+' row:'+str(j)+' error...'
                    sys.exit(0)
            elif phenotype[j] == '0':
                if cur in count_cols0:
                    count_cols0[cur] += 1
                elif cur[::-1] in count_cols0:
                    cur = cur[::-1]
                    count_cols0[cur] += 1
                else:
                    print 'col:'+str(i)+' row:'+str(j)+' error...'
                    sys.exit(0)
            else:
                print 'col:' + str(i)
                sys.exit(0)
        #put
        #print count_cols0
        #print count_cols1
        for j in range(rows):
            cur = genotype[j][i]
            if phenotype[j] == '1':
                if cur in count_cols1:
                    count[j][i] = count_cols1[cur]
                elif cur[::-1] in count_cols1:
                    cur = cur[::-1]
                    count[j][i] = count_cols1[cur]
            elif phenotype[j] == '0':
                if cur in count_cols0:
                    count[j][i] = count_cols0[cur]
                elif cur[::-1] in count_cols0:
                    cur = cur[::-1]
                    count[j][i] = count_cols0[cur]

    fopw = open('count_genotype.txt', 'wb')
    print 'start write file:' + 'count_genotype.txt' + '...'
    for i in range(rows):
        for j in range(cols):
            fopw.write(str(count[i][j]))
            fopw.write(' ')
        fopw.write('\n')
    fopw.close
    print 'finish write file:' + 'count_genotype.txt' + '...'
