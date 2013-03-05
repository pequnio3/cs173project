'''
Created on Mar 4, 2013

@author: Panagiotis Achlioptas
@contact: pachlioptas@gmail.com
@copyright: You are free to use, change, or redistribute this code in any way you want 
for non-commercial purposes. 

'''


from featureExtraction import *
from simpleStatistics import *
import cPickle
from svmutil import *
import numpy



#countSizeOfClasses("Human", vistaData)
#countSizeOfClasses("Mouse", vistaData)



#vistaData = cPickle.load( open("../data/vista_data.data", "r") )
#
#
#species     = ["Human", "Mouse"]
#body_parts  = ["limb", "neural tube", "cranial nerve", "hindbrain (rhombencephalon)", "midbrain (mesencephalon)", "forebrain", "heart"]
#
#
#

## extract feature vectors



##for s in species:
##    for b in body_parts:
##        out = "../data/paper_data"+s+"_"+b.replace(" ","_")+".txt"
##        extractFeatures(vd, "human", "neural tube", "../data/human_neural_tube.txt")



#y, x = svm_read_problem('../data/human_neural_tube.txt')
#
#cPickle.dump(y, open("y","w"))
#cPickle.dump(x, open("x","w"))


y = cPickle.load(open("y","r"))
x = cPickle.load(open("x","r"))

#        -v n: n-fold cross validation mode

model = svm_train(y[:100], x[:100], '-c 4')


#w = (model.sv_coef' * full(model.SVs));


#svm_type = model.get_svm_type()
#nr_class = model.get_nr_class()
#svr_probability = model.get_svr_probability()
#class_labels = model.get_labels()
#sv_indices = model.get_sv_indices()
#nr_sv = model.get_nr_sv()
#is_prob_model = model.is_probability_model()
#support_vector_coefficients = model.get_sv_coef()


support_vector_coefficients = model.get_sv_coef()
support_vectors = model.get_SV()  # Dictionary with indices 1, 2 corresponding to i-th dim on support vector

for i in support_vectors:
    print i
    raw_input()
    


print len(support_vectors)
print len(support_vector_coefficients)


weights = numpy.dot(support_vectors, support_vector_coefficients)
b = -model.rho[0]


#svm_save_model('libsvm.model', m)
#m = svm_load_model('libsvm.model')


#b = -model.rho;

#if model.Label(1) == -1
#  w = -w;
#  b = -b;
#end


#predict_label, predict_accuracy, dec_p_val = svm_predict(y[200:], x[200:], m)


#
#for i,z in zip(p_acc, p_val):
#    print i
#    print z
#    raw_input()