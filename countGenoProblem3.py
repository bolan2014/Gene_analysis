#coding=utf-8
import os, sys


def read_genotype_column_name(file_name):
    print 'start read file:' + file_name + '...'
    matrix = None
    cur_no = 1
    fopr = open(file_name)
    for line in open(file_name):
        line = fopr.readline()
        if cur_no == 1:
            cur_no += 1
            if line != "" or line is not None:
                line = line.strip().split(' ')
                cur_no += 1
                matrix = line
                break
    print 'finish read file:' + file_name + '...'
    print 'matrix size = ' + str(len(matrix))
    #time.sleep(5)
    return matrix


def get_selected_column_name(genotype_file_path, selected_column_file_path):
    selected_column_number = []
    with open(selected_column_file_path) as fopr:
        for line in fopr:
            line = line.strip()
            selected_column_number.append(int(line))
    selected_column_name = []
    matrix = read_genotype_column_name(genotype_file_path)
    for index in selected_column_number:
        selected_column_name.append(matrix[index])
    return selected_column_name


def get_all_gene(folder_path):
    matrix = []
    files = os.listdir(folder_path)
    for f in files:
        m = []
        with open(folder_path + "/" + f):
            for cname in f:
                cname = cname.strip()
                if cname != None and cname != "":
                    m.append(cname)
        matrix.append(m)
    return matrix


genotype_file_path = 'genotype.dat'
selected_column_file_path = 'selectedColumnNumber.txt'
selected_column_name = get_selected_column_name(genotype_file_path, selected_column_file_path)
print selected_column_name
folder_path = 'gene_info'
files = os.listdir(folder_path)

#获取含有致病位点的基因
count_gene = 0
for f in files:
    #print 'solving file: ' + str(f)
    with open(folder_path + '/' + f) as fopr:
        for cname in fopr:
            cname = cname.strip()
            if cname != None and cname != "" and cname in selected_column_name:
                print f
                count_gene += 1
                break
print "count gene's number is [ " + str(count_gene) + " ]"

#获取每个基因含有的致病位点的数目
gene_dict = {}
for f in files:
    with open(folder_path + "/" + f) as fopr:
        count = 0
        for cname in fopr:
            cname = cname.strip()
            if cname != None and cname != "" and cname in selected_column_name:
                count += 1
        gene_dict[str(f)] = count

#gene_dict = [v for v in sorted(gene_dict.values())]
fopw = open('filteredGene.arff', 'w')
for k, v in gene_dict.items():
    fopw.write(str(k)+":"+str(v)+'\n')
fopw.close()

#print gene_dict

#验证基因中位点交叉
m1 = get_all_gene(folder_path)
m2 = get_all_gene(folder_path)
flag = 0
for i in range(len(m1)):
    for j in range(i+1, len(m2), 1):
        t1 = m1[i]
        t2 = m2[j]
        for x1 in t1:
            if x1 in t2:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break
if flag == 1:
    print "yes"
else:
    print "no"
