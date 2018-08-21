import numpy as np
import random
import matplotlib.pyplot as plt
import discriminant
import contour




def class_region(combo, train, mean, covariance, probability):
    color = ['seagreen', 'darksalmon', 'lightblue']
#    color2 = ['darkgreen',  'r', 'b']
    num_class = len(combo)
    i= 0 
    while i < num_class - 1 :
        if i == 0:
            x_min = min(train["tr" + str(combo[i])][:,0].min(), train["tr" + str(combo[i+1])][:,0].min())
            x_max = max(train["tr" + str(combo[i])][:,0].max(), train["tr" + str(combo[i+1])][:,0].max())
            y_min = min(train["tr" + str(combo[i])][:,1].min(), train["tr" + str(combo[i+1])][:,1].min())
            y_max = max(train["tr" + str(combo[i])][:,1].max(), train["tr" + str(combo[i+1])][:,1].max())
            
        else:
            x_min = min(x_min, train["tr" + str(combo[i+1])][:,0].min())
            x_max = max(x_max, train["tr" + str(combo[i+1])][:,0].max())
            y_min = min(y_min, train["tr" + str(combo[i+1])][:,1].min())
            y_max = max(y_max, train["tr" + str(combo[i+1])][:,1].max())
            
        i += 1
    
#    x_min = min(train["tr0"][:,0].min(), train["tr1"][:,0].min(), train["tr2"][:,0].min())
#    x_max = max(train["tr0"][:,0].max(), train["tr1"][:,0].max(), train["tr2"][:,0].max())
#    y_min = min(train["tr0"][:,1].min(), train["tr1"][:,1].min(), train["tr2"][:,1].min())
#    y_max = max(train["tr0"][:,1].max(), train["tr1"][:,1].max(), train["tr2"][:,1].max())
    
    
    add_x = np.linalg.norm(x_max - x_min)/ 30
    add_y = np.linalg.norm(x_max - x_min)/ 30
    #generate points for class region plot
    x_q = x_min - 1
    z = []
    while x_q <= x_max + 1:
        y_q = y_min - 1
        while y_q <= y_max + 1:
            x_q = round(x_q, 2)
            y_q = round(y_q, 2)
            c = [x_q, y_q]
            z.append(c)
            y_q = y_q + add_y
            
        x_q = x_q + add_x
        
   
    #Calculate discriminant function for points in z
    g = {}
    
    #Print the name of corresponding classes for which decision region is ploted
#    for ii in range(num_class):
#    print("Decision Region of class %d and class %d", combo[ii])
    
    
    for i in range(len(z)):
        for ii in range(num_class):
            g[str(combo[ii]) + "_x"] = discriminant.discriminant_function(z[i], mean['m' + str(combo[ii])],covariance["cov" + str(combo[ii])],probability['prob' + str(combo[ii])])
            
#        g1_x = discriminant.discriminant_function(z[i], mean['m0'],covariance["cov" + str(0)],probability['prob0'])
#        g2_x = discriminant.discriminant_function(z[i], mean['m1'],covariance["cov" + str(1)],probability['prob1'])
#        g3_x = discriminant.discriminant_function(z[i], mean['m2'],covariance["cov" + str(2)],probability['prob2'])
        
        
        
        for ii in range(num_class):
            
            if g[str(combo[ii]) + "_x"] == max(g.values()):
                plt.plot(z[i][0], z[i][1], '.', c = color[combo[ii]])
                
                
                
    

    for i in range(num_class):
        xv = np.array(train["tr" + str(combo[i])][:,0])
        yv = np.array(train["tr" + str(combo[i])][:,1])
        if combo[i] == 0:
            plt.plot(xv, yv, '_y')
        elif combo[i] ==1:
            plt.plot(xv, yv, '_', color = 'red')
        else:
            plt.plot(xv, yv, '_b')
#            
        # plot contour
#        contour.contour(train["tr" + str(combo[i])], color2[combo[i]])
       

    if len(combo) == 2:
        plt.title("Decision Region of class %d and class %d" %(combo[0], combo[1]))
        
    else:
        plt.title("Decision Region of all classes")
    
    plt.show()
        
