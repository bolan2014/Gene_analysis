import numpy as np
from sklearn.svm import SVC


def read_phenotype(filename):
    types = []
    with open(filename) as f:
        for line in f:
            types.append(int(line.strip()))
    return types


def read_qi(filename):
    qi = []
    with open(filename) as f:
        first = True
        for line in f:
            qi.append(map(lambda x : float(x), line.strip().split(' ')))
    return qi


def read_rs(filename):
    rss = []
    with open(filename) as f:
        line = f.readline()
        rss = line.strip().split(' ')
    return rss


def random_train_and_test(data, label):
    datas = []
    for i in range(len(data)):
        datas.append(data[i])
        datas[i].append(label[i])

    import random
    random.shuffle(datas)
    count = int(0.9 * len(data))
    return np.array(datas[:count]), np.array(datas[count:])


if __name__ == '__main__':
    types = read_phenotype('../data/phenotype.txt')
    qis = read_qi('../data/qi.txt')
    rss = read_rs('../data/genotype.dat')

    iter = 30
    for x in range(iter):
        print "======== iter " + str(x) + " ========"
        train, test = random_train_and_test(qis, types)
        train_data = train[0 : len(train), 0 : len(train[0]) - 1]
        train_label = train[:, -1]
        test_data = test[0 : len(test), 0 : len(test[0]) - 1]
        test_label = test[:, -1]

        clf = SVC(kernel='sigmoid')
        model = clf.fit(train_data, train_label)
        r = clf.predict(test_data)
        correct = 0
        for j in range(len(r)):
            if r[j] == test_label[j]:
                correct += 1
        print correct * 1.0 / len(test_data)

        # weights = clf.coef_.tolist()
        #
        # weight_dict = {}
        # for i in range(len(rss)):
        #     weight_dict[rss[i]] = abs(weights[0][i])
        # items = weight_dict.items()
        # items.sort(lambda a, b: -cmp(a[1], b[1]))
        #
        # weight_file = open('svm_weight' + str(x) + '.txt', 'w')
        # for item in items:
        #     weight_file.write(str(item[0]) + '\t' + str(item[1]) + '\n')
        # weight_file.close()

