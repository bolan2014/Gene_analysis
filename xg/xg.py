import numpy as np
import xgboost as xgb

filter_lines = "51,101,115,319,347,370,448,608,727,731,866,939,1056,1121,1338,1467,1519,1522,1529,1542,1589,1788,1998,2033,2081,2219,2290,2541,2555,2705,2786,2814,2831,2846,2860,3108,3176,3207,3577,3579,3674,3768,3832,4324,4517,4521,4644,4655,4825,4829,4844,4930,4939,4990,5012,5021,5065,5247,5248,5391,5423,5441,5659,5782,5834,5843,5875,5879,5906,5930,6030,6174,6264,6301,6309,6393,6500,6579,6671,6736,6842,6887,6912,6924,7066,7162,7225,7275,7341,7551,7563,7736,7846,7888,7988,7991,8092,8252,8655,8657,8680,8692,8696,8865,8904,8934,9051,9104,9117,9371,9384,9434"


def read_phenotype(filename):
    types = []
    with open(filename) as f:
        for line in f:
            types.append(int(line.strip()))
    return types


def read_qi(filename):
    qi, cnt = [], 0
    filter_nos = filter_lines.split(",")
    with open(filename) as f:
        first = True
        for line in f:
            if cnt > 0:
                qi.append(filter_by_col_no(line.strip().split(' '), filter_nos))
            cnt += 1
    return qi


def filter_by_col_no(ss, cols):
    r = []
    for i in range(len(ss)):
        if str(i) in cols:
            r.append(ss[i])
    return r


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


def l2int(l):
    li = []
    for ll in l:
        li.append(int(ll))
    return np.array(li)


def train_iter(iter, qis, types):
    print "======== iter " + str(iter) + " ========"
    train, test = random_train_and_test(qis, types)
    train_data = train[0: len(train), 0: len(train[0]) - 1]
    train_label = l2int(train[:, -1])
    test_data = test[0: len(test), 0: len(test[0]) - 1]
    test_label = l2int(test[:, -1])
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
    param = {'max_depth': 5, 'eta': 0.3, 'silent': 1, 'objective': 'binary:logistic'}
    num_round = 6
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
    # qis = read_qi('../data/qi.txt')
    qis = read_qi('../encoded_myRst.txt')
    # rss = read_rs('../data/genotype.dat')

    iter = 30
    for x in range(iter):
        train_iter(x, qis, types)


main()

