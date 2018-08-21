import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde

def contour(data, color):
    
    nbins = 20
#    num_class = len(combo)
    
#    for i in range(num_class):
#    data =  train["tr" + str(i)]
    x = np.array(data[:,0])
    y = np.array(data[:,1])
    
    
    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    k = kde.gaussian_kde(data.T)
#    print(k)
    xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    
    plt.contour(xi, yi, zi.reshape(xi.shape), colors = color)
 