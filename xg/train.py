#! /usr/bin/python
import numpy as np
import xgboost as xgb

# label need to be 0 to num_class -1
data = np.loadtxt('../encoded_myRst.txt', delimiter=' ', skiprows=1)
sz = data.shape

print len(data), len(sz)

types = []
with open('../phenotype.txt') as f:
    for line in f:
        types.append(int(line.strip()))
types = np.array(types)

print len(types)

train_X = data[:int(sz[0] * 0.7), :]
test_X = data[int(sz[0] * 0.7):, :]

#train_X = train[:,0:9445]
train_Y = types[:int(sz[0] * 0.7)]
test_Y = types[int(sz[0] * 0.7):]

#test_Y = test[:, 9446]
#test_Y = 

xg_train = xgb.DMatrix( train_X, label=train_Y)
xg_test = xgb.DMatrix(test_X, label=test_Y)
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 6

watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
num_round = 5
bst = xgb.train(param, xg_train, num_round, watchlist );
# get prediction
pred = bst.predict( xg_test );

print ('predicting, classification error=%f' % (sum( int(pred[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))

# do the same thing again, but output probabilities
param['objective'] = 'multi:softprob'
bst = xgb.train(param, xg_train, num_round, watchlist );
# Note: this convention has been changed since xgboost-unity
# get prediction, this is in 1D array, need reshape to (ndata, nclass)
yprob = bst.predict( xg_test ).reshape( test_Y.shape[0], 6 )
ylabel = np.argmax(yprob, axis=1)

print ('predicting, classification error=%f' % (sum( int(ylabel[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))
