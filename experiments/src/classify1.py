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


def combineTrials(species, bodyPart, verbose=True):
    #Notice that if you are merging trials from the same species, you will be double counting negative samples
    #This should not affect the  classifier -> but maybe it will affect our statistics in Cross Validation.
    #->If time permits remove duplicates
    
    Y = list()
    X = list()
    
    for s in species:
        for b in bodyPart:
            inputF = "../data/" + s + "_" + b + "_RN" + ".txt"
            y, x = svm_read_problem(inputF)
            Y.extend(y)
            X.extend(x)

    if verbose:
            print "combineTrials -> after combining:"        
            print "Positives: ", str(Y.count(1))
            print "Negative:", str(Y.count(0))
            print "Total ", len(Y)

    return Y, X
            
            

if __name__ == '__main__':    

    species     = ["Human", "Mouse"]    
    body_parts  = ["limb", "neural_tube", "cranial_nerve", "hindbrain", "midbrain", "forebrain", "heart", "any"]

#    species = ["Human", "Mouse"]
#    bodyParts  = ["cranial_nerve"]
#
#    Y, X = combineTrials(species, bodyParts)
#
#    model_radial  = svm_train(Y, X, '-t 2 -c 4 -v 5 -q')
#    

# load files
    for s in species:
        for b in body_parts:
            
            inputF = "../data/" + s + "_" + b + "_RN" + ".txt"

            y, x = svm_read_problem(inputF)
                                
            #-v n: n-fold cross validation mode
            #-c cost : set the parameter C of C-SVC
            #-t kernel_type : set type of kernel function            
            #0 -- linear: u'*v
            #1 -- polynomial: (gamma*u'*v + coef0)^degree
            #2 -- radial basis function: exp(-gamma*|u-v|^2)
            #3 -- sigmoid: tanh(gamma*u'*v + coef0)
            
#            model_linear  = svm_train(y, x, '-t 0 -c 4 -v 5 -q')
#            model_poly    = svm_train(y, x, '-t 1 -c 4 -v 5 -q')
            model_radial  = svm_train(y, x, '-t 2 -c 4 -v 5 -q')
#            svm_save_model('test_model1', model)
#            model_sigmoid = svm_train(y, x, '-t 3 -c 4 -v 5 -q')








## OTHER FUNCTIONS WE NEED TO CONSIDER

##USE TO SAVE/LOAD Model
    #svm_save_model('libsvm.model', m)
    #m = svm_load_model('libsvm.model')


#predict_label, predict_accuracy, dec_p_val = svm_predict(y[200:], x[200:], model)

#svm_type = model.get_svm_type()
#nr_class = model.get_nr_class()
#svr_probability = model.get_svr_probability()
#class_labels = model.get_labels()
#sv_indices = model.get_sv_indices()
#nr_sv = model.get_nr_sv()
#is_prob_model = model.is_probability_model()
#support_vector_coefficients = model.get_sv_coef()


## Trying to find the weights of the support vectors => the important features.

# If we were using matlab we shoudl do:
# w = (model.sv_coef' * full(model.SVs));

#The following is not working
#support_vector_coefficients = model.get_sv_coef()
#support_vectors = model.get_SV()  # Dictionary with indices 1, 2 corresponding to i-th dim on support vector
#weights = numpy.dot(support_vectors, support_vector_coefficients)

#Also I think we need to adjust based on this:
#b = -model.rho;
#if model.Label(1) == -1
#  w = -w;
#  b = -b;
#end
