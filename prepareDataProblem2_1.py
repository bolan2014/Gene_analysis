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
    phenotype = read_phenotype('phenotype_2.txt')

    #每一行表示源文件每一列中的每个碱基对的数量总数
    fopw = open('third_copy_genotype.txt', 'w')

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
        #write back
        for k, v in count_cols0.items():
            fopw.write(str(k) + " " + str(v) + " ")
        for k, v in count_cols1.items():
            fopw.write(str(k) + " " + str(v) + " ")
        fopw.write('\n')

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
    fopw.close()

    count_genotype_file_name = 'secode_copy_genotype.txt'
    fopw = open(count_genotype_file_name, 'w')
    print 'start write file:' + count_genotype_file_name + '...'
    for i in range(rows):
        for j in range(cols):
            fopw.write(str(count[i][j]))
            fopw.write(' ')
        fopw.write('\n')
    fopw.close
    print 'finish write file:' + count_genotype_file_name + '...'
