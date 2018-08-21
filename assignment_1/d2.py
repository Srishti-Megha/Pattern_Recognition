import numpy as np
import matplotlib.pyplot as plt
import cases
import random
import confusion_matrix
import class_region
from itertools import combinations


#C_1 = open('C://Users//vicky//Desktop//pattern//assgn 1//rd_group19//Class1.txt','r')
#C_2 = open('C://Users//vicky//Desktop//pattern//assgn 1//rd_group19//Class2.txt','r')

#f = open('C://Users//vicky//Desktop//pattern//assgn 1//datasheet2.txt','r')
f = open('data2.txt','r')

#variables = [C_1, C_2, C_3]
train = {}          #empty training dictonary
test  = {}           #empty test dictonary


mean       = {}          # empty class mean dictonary 
covariance = {}          # empty class covariance dictonary
probability = {}         # empty class probability dictionary


item = 1                #used for increasing the no. of lines in for loop
f = f.readlines()     
for i  in range (0,3):
   
    train["tr" + str(i)] = []

    test["te" + str(i)]  = []

i = 0    
for lines in f:
    p = lines.split()
    p = np.array(p).astype(np.float)
    if i == 0:
        if item <= (0.75 * 300):
            train["tr" + str(i)].append(p)
            
            
    
        elif (0.75 * 300) < item <= 300 :
            test["te" + str(i)].append(p)
            
        
        item = item + 1
        
   
    elif i == 1:
    
        if 300 < item <= (300 + 0.75 * 500):
            train["tr" + str(i)].append(p)
            
    
        elif (300 + 0.75 * 500) < item <= 800 :
            test["te" + str(i)].append(p)
                   
        item = item + 1
        
    elif i == 2:
   
        if 800 < item <= (800 + 0.75 * 1000):
            train["tr" + str(i)].append(p)
            
    
        elif (800 + 0.75 * 1000) < item <= 1800 :
            test["te" + str(i)].append(p)
            
        item = item + 1
    if item == 301 or item == 801 :
        i = i+1
        
        
#change list items to array
for i in range(3):    
    train["tr" + str(i)] = np.array(train["tr" + str(i)])
    test["te" + str(i)] = np.array(test["te" + str(i)]) 
    

#calculating mean of the classes
#mean = {}
for i in range(3):    
    mean["m" + str(i)] = np.mean(train["tr" + str(i)], axis = 0)   # mean defined as mi in mean dictonary
    
#calculating covariance matrix of classes

for i in range(3):
    covariance["cov" + str(i)] = np.cov(train["tr" + str(i)].T)
    
    
# calculating the probability of classes

Total_train_points          = 0
for i_11 in range(3):
        Total_train_points = Total_train_points + len(train['tr'+str(i_11)])

for i in range(3):
    probability['prob' + str(i)] = len(train['tr'+str(i)]) / Total_train_points 
    

    
case = input("enter the case number(1,2,3,4): ")
print()


#while (case != '1') or (case != '2') or (case != '3') or (case != '4'):
#    case = input("enter the case number(1,2,3,4): ")
#    print("check the case & case number" )
    


    
if case == '1':
    Sigma = cases.case_1(covariance)
    
elif case == '2':
    Sigma = cases.case_2(covariance)
    
elif case == '3':
    Sigma = cases.case_3(covariance)
    
elif case == '4':
    Sigma = cases.case_4(covariance)
    
else:
    print("check the case & case number" )
    
    
    
    
    
    

pairs = list(combinations([0,1,2], 2))  
  

for combo in pairs:
    class_region.class_region(combo, train, mean, Sigma, probability)
    
    
#plt.show()   
    
# Class region plot
al_combo = [0, 1, 2]
class_region.class_region(al_combo, train, mean, Sigma, probability)
        
# Confusion matrix 
confusion_matrix.confusion_matrix(mean, Sigma, probability, test)


