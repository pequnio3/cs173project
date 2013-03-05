print __doc__

import numpy as np
import pylab as pl
from sklearn import svm 
import cPickle
import scipy as sp
import sys

def makeA(d, default=0):
    """Converts a dictionary to a list. Pads with a default element

    Examples:

    >>> makeA({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})
    [1, 0, 1, 0, 2, 0, 1, 0, 0, 1]

    >>> makeA({3: 'kos'},'')
    ['', '', '', 'kos']

    """
    maxElem = max(d)
    return [d.get(x, default) for x in range(maxElem)]





def numberOfDimensions(start_kmer=6, end_kmer=6):
    # size of feature vector
    m = 0
    for k in range(start_kmer,end_kmer+1):
        m += pow(4,k)
    return m


#dimenions = number of dimensions of each vector
#allVectors = a list of vectors, expressed in the libsvm format
def convertSparseVectorsToArray(allVectors, dimensions):
    A = sp.sparse.dok_matrix((len(allVectors), dimensions), dtype=np.int16)   #be careful with the int16
        
    for current, vector in enumerate(allVectors):
        for coord in vector.keys():
            A[current, coord] = vector[coord]
    
    return A




#Y = cPickle.load(open("y","r"))
#X = cPickle.load(open("x","r"))
#print 'loaded'

#A = convertSparseVectorsToArray(X, numberOfDimensions() )

#cPickle.dump(A, open("A","w"))



Y = cPickle.load(open("y","r"))
A = cPickle.load(open("A","r"))



clf = svm.SVC()

#clf.fit(A, Y) 



#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
#gamma=0.0, kernel='rbf', max_iter=-1, probability=False, shrinking=True,
#tol=0.001, verbose=False)
#>>> dec = clf.decision_function([[1]])
#>>> dec.shape[1] # 4 classes: 4*3/2 = 6
#6
#
#
## import some data to play with
#iris = datasets.load_iris()
#X = iris.data[:, :2]  # we only take the first two features. We could
#                      # avoid this ugly slicing by using a two-dim dataset
#Y = iris.target
#
#h = .02  # step size in the mesh
#
## we create an instance of SVM and fit out data. We do not scale our
## data since we want to plot the support vectors
#C = 1.0  # SVM regularization parameter
#svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
#rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, Y)
#poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
#lin_svc = svm.LinearSVC(C=C).fit(X, Y)
#
## create a mesh to plot in
#x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
#y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
#xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                     np.arange(y_min, y_max, h))
#
## title for the plots
#titles = ['SVC with linear kernel',
#          'SVC with RBF kernel',
#          'SVC with polynomial (degree 3) kernel',
#          'LinearSVC (linear kernel)']
#
#
#for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
#    # Plot the decision boundary. For that, we will asign a color to each
#    # point in the mesh [x_min, m_max]x[y_min, y_max].
#    pl.subplot(2, 2, i + 1)
#    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#
#    # Put the result into a color plot
#    Z = Z.reshape(xx.shape)
#    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
#    pl.axis('off')
#
#    # Plot also the training points
#    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
#
#    pl.title(titles[i])
#
#pl.show()