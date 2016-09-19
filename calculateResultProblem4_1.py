#coding=utf-8
import os, sys
import prepareDataProblem2_1

def get_multiphenos(file_path):
    matrix = []
    with open(file_path) as fopr:
        for line in fopr:
            line = line.strip().split(' ')
            if line is not None and line != "":
                matrix.append(line)
    return matrix


def save_phenotype_2(phenotype_file_path, multiphenos_file_path):
    phenotype = prepareDataProblem2_1.read_phenotype(phenotype_file_path)
    multiphenos = get_multiphenos(multiphenos_file_path)
    fopw = open('phenotype_2.txt', 'w')
    for i in range(len(phenotype)):
        if int(phenotype[i]) == 1:
            m = multiphenos[i]
            flag = 1
            for j in m:
                if int(j) == 0:
                    flag = 0
                    break
            fopw.write(str(flag) + '\n')
        else:
            fopw.write("0\n")
    fopw.close()


if __name__ == "__main__":
    phenotype_file_path = 'phenotype.txt'
    multiphenos_file_path = 'multi_phenos.txt'
    save_phenotype_2(phenotype_file_path, multiphenos_file_path)
