import numpy as np
from sklearn.svm import SVC


def read_phenotype(filename):
    types = []
    with open(filename) as f:
        for line in f:
            types.append(int(line.strip()))
    return np.array(types)


def read_qi(filename):
    qi = []
    with open(filename) as f:
        for line in f:
            qi.append(line.strip().split(' '))
    return np.array(qi)


def read_rs(filename):
    rss = []
    with open(filename) as f:
        line = f.readline()
        rss = line.strip().split(' ')
    return rss


if __name__ == '__main__':
    types = read_phenotype('../data/phenotype.txt')
    qis = read_qi('../data/qi.txt')
    rss = read_rs('../data/genotype.dat')

    clf = SVC(kernel='linear',
              verbose=True)
    model = clf.fit(qis, types)
    weights = clf.coef_.tolist()

    weight_dict = {}
    for i in range(len(rss)):
        weight_dict[rss[i]] = abs(weights[0][i])
    items = weight_dict.items()
    items.sort(lambda a, b: -cmp(a[1], b[1]))

    weight_file = open('svm_weight.txt', 'w')
    for item in items:
        weight_file.write(str(item[0]) + '\t' + str(item[1]) + '\n')

