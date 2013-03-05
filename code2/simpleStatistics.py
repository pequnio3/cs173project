'''
Created on Mar 5, 2013

@author: Panagiotis Achlioptas
@contact: pachlioptas@gmail.com
@copyright: You are free to use, change, or redistribute this code in any way you want 
for non-commercial purposes. 

'''

def countSizeOfClasses(species, vistaData, verbose=True ):
    total = positiveClass = negativeClass = 0
    for trial in vistaData:        
        if trial['species'] == species:    
            total += 1
            if trial['expression']:
                positiveClass +=1 
            else:
                negativeClass +=1
    if verbose:
        print "There are in total " + str(total) +" " + species + " instances: ",
        print str(positiveClass)+ " are Positive and " + str(negativeClass) + " are Negative."



def countPosBodyExpression(species, bodyPart, vistaData, verbose=True ):
    positiveClass =0
    for trial in vistaData:        
        if trial['species'] == species and trial["expression"] and bodyPart in trial['results']:
                positiveClass +=1 
    
    if verbose:
        print str(positiveClass)+ " are Positive for the " + species + " in " + bodyPart + "."

    
    