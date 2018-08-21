#mat : covariance matrix
import numpy as np
def discriminant_function(x,mean,mat,Prob):
    g_x = -(1/2)* np.inner(x,(np.dot(np.linalg.inv(mat),x))) + np.inner(mean,(np.dot(np.linalg.inv(mat),x))) - (1/2)* np.inner(mean,(np.dot(np.linalg.inv(mat),mean))) - (1/2)*np.log10(np.linalg.det(mat)) + np.log10(Prob)
    
    return (g_x)