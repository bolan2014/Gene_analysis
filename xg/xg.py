import numpy as np
import xgboost as xgb


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
        datas.append(data[i][:])
        datas[i].append(label[i])

    import random
    random.shuffle(datas)
    count = int(0.9 * len(datas))
    return np.array(datas[:count]), np.array(datas[count:])


def train_iter(iter, qis, types):
    print "======== iter " + str(iter) + " ========"
    train, test = random_train_and_test(qis, types)
    train_data = train[0: len(train), 0: len(train[0]) - 1]
    train_label = train[:, -1]
    test_data = test[0: len(test), 0: len(test[0]) - 1]
    test_label = test[:, -1]
    #
    # clf = SVC(kernel='linear')
    # model = clf.fit(train_data, train_label)
    # r = clf.predict(test_data)
    # correct = 0
    # for j in range(len(r)):
    #     if r[j] == test_label[j]:
    #         correct += 1
    # print correct * 1.0 / len(test_data)

    dtrain = xgb.DMatrix(train_data, label=train_label)
    dtest = xgb.DMatrix(test_data)
    param = {'max_depth': 10, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
    num_round = 20
    bst = xgb.train(param, dtrain, num_round)
    preds = bst.predict(dtest)
    correct = 0
    for j in range(len(preds)):
        r = 0
        if preds[j] >= 0.5:
            r = 1
        if r == test_label[j]:
            correct += 1
    print correct * 1.0 / len(test_data)


def main():
    types = read_phenotype('../data/phenotype.txt')
    qis = read_qi('../data/qi.txt')
    # rss = read_rs('../data/genotype.dat')

    iter = 30
    for x in range(iter):
        train_iter(x, qis, types)


main()

