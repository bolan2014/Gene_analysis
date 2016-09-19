#! /usr/bin/python
import numpy as np
import xgboost as xgb
from calculateResult import output_cols

def read_phenotype(filename):
    types = []
    with open(filename) as f:
        for line in f:
            types.append(int(line.strip()))
    return types


def read_qi(filename, filter_lines):
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
    for i in range(len(cols)):
        r.append(ss[int(cols[i])])
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
    count = int(0.95 * len(datas))
    return np.array(datas[:count]), np.array(datas[count:])


def l2int(l):
    li = []
    for ll in l:
        li.append(int(ll))
    return np.array(li)


types = read_phenotype('../data/phenotype.txt')

for target1 in range(300, 350, 10):
    for target2 in range(300, 350, 10):
        filter_cols = output_cols(target1, target2)
        xx = len(filter_cols.split(","))
        # if xx > 100 or xx < 50:
        #     continue
        print "target1: " + str(target1) + " target2: " + str(target2)
        print xx
        if filter_cols == '':
            continue
        data = read_qi('../encoded_myRst.txt', filter_cols)
        if len(data[0]) == 0:
            continue
        iter = 10
        minerr = 100
        for i in range(iter):
            train, test = random_train_and_test(data, types)
            train_X = train[0: len(train), 0: len(train[0]) - 1]
            train_Y = l2int(train[:, -1])
            test_X = test[0: len(test), 0: len(test[0]) - 1]
            test_Y = l2int(test[:, -1])

            xg_train = xgb.DMatrix(train_X, label=train_Y)
            xg_test = xgb.DMatrix(test_X, label=test_Y)

            param = {}
            param['objective'] = 'multi:softmax'
            param['eta'] = 0.8
            param['max_depth'] = 20
            param['silent'] = 1
            param['nthread'] = 4
            param['num_class'] = 2

            num_round = 6
            bst = xgb.train(param, xg_train, num_round)
            # a = xgb.plot_tree(bst)
            # print xgb.plot_tree
            # get prediction
            pred = bst.predict( xg_test )
            # print pred

            err = (sum( int(pred[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) )
            if err < minerr:
                minerr = err

        print minerr

            # print ('predicting, classification error=%f' % (sum( int(pred[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))
            # print minerr
            # do the same thing again, but output probabilities
            # param['objective'] = 'multi:softprob'
            # bst = xgb.train(param, xg_train, num_round, watchlist );
            # Note: this convention has been changed since xgboost-unity
            # get prediction, this is in 1D array, need reshape to (ndata, nclass)
            # yprob = bst.predict( xg_test ).reshape( test_Y.shape[0], 1)
            # ylabel = np.argmax(yprob, axis=1)
            #
            # print ('predicting, classification error=%f' % (sum( int(ylabel[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))
