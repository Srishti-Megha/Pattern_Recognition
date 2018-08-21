########## Calculate Covariance Matrix according to the given case #########################

import numpy as np
import random
import matplotlib.pyplot as plt
import discriminant


#case_1 sigma^2 I
def case_1(covariance):
    sigma = 0.00
   
    for i_11 in range(3):
        sigma += covariance["cov" + str(i_11)]
        
    sigma = np.average(sigma)/3
    
    covariance_matrix = sigma * np.identity(len(covariance["cov0"]))
    covariance['cov0'] =  covariance_matrix
    covariance['cov1'] =  covariance_matrix
    covariance['cov2'] =  covariance_matrix          
                
    return(covariance)
    
#    minm = min(min(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , min(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
#    maxm = max(max(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , max(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
    
       
        
# case2 

def case_2(covariance):
    
    sigma = 0.00
    for i_11 in range(3):
        sigma += covariance["cov" + str(i_11)]
    
    covariance_matrix = sigma/3
    covariance['cov0'] =  covariance_matrix
    covariance['cov1'] =  covariance_matrix
    covariance['cov2'] =  covariance_matrix

    return(covariance)
    
#    minm = min(min(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , min(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
#    maxm = max(max(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , max(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
    
    
    

# case3 

def case_3(covariance):
    
        
    for i_11 in range(3):
           covariance["cov" + str(i_11)] = np.diag(np.diag(covariance["cov" + str(i_11)]))
           
    return(covariance)
    
#    minm = min(min(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , min(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
#    maxm = max(max(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , max(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
    


# case 4
def case_4(covariance):
    
    #Covariance matrix is same
    return(covariance)
    
       
#    minm = min(min(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , min(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
#    maxm = max(max(train['tr0']['x0'][:int(len(train['tr0']['x0']))],train['tr1']['x1'][:int(len(train['tr1']['x1']))],train['tr2']['x2'][:int(len(train['tr2']['x2']))] , max(train['tr0']['y0'][:int(len(train['tr0']['y0']))],train['tr1']['y1'][:int(len(train['tr1']['y1']))]),train['tr2']['y2'][:int(len(train['tr2']['y2']))]))
    