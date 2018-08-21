
import discriminant


def confusion_matrix(mean,covariance,probability,test):
    
    confusion_mat = []
    precision = []
    accuracy = ()
    total_points = 0
    total_true_predict = 0
    
    for i in range(len(test)):
        count_1 = 0
        count_2 = 0
        count_3 = 0
        confusion_mat.append([])
        for j in range(len(test['te' + str(i)])	):
            
            vec = test['te' + str(i)][j]
            g1_x = discriminant.discriminant_function(vec, mean['m0'],covariance['cov0'],probability['prob0'])
            g2_x = discriminant.discriminant_function(vec, mean['m1'],covariance['cov1'],probability['prob1'])
            g3_x = discriminant.discriminant_function(vec, mean['m2'],covariance['cov2'],probability['prob2'])
            
            
            if g1_x > g2_x and g1_x > g3_x:
                count_1 = count_1 + 1
                
            elif g2_x > g1_x and g2_x > g3_x:
                count_2 = count_2 + 1
                
            elif g3_x > g1_x and g3_x > g2_x:
                count_3 = count_3 + 1
                
        confusion_mat[i].append(int(count_1))
        confusion_mat[i].append(int(count_2))
        confusion_mat[i].append(int(count_3))
        
        #total_points = total_points + count_1 + count_2 + count_3
    print ("   confusion_matrix   ")    
    
    for i in range(len(test) + 1):
        true_predict = 0
        false_predict = 0
        precision.append([])
        
        for j in range(len(test) + 1):
            if i == 0:
                if j == 0:
                    print("PC\AC   ", end = "")
                else:
                    print("C_%d    "%j, end = "")
            else: #i!=0
                if j == 0:
                    print("C_%d     "%(i), end = "")
                else: #j!=0
                    print(confusion_mat[i-1][j-1], end = "     ")
                    total_points = total_points + confusion_mat[i-1][j-1]
                    
                    if i == j:
                        true_predict = true_predict + confusion_mat[i-1][j-1]
                    else:
                        false_predict = false_predict + confusion_mat[i-1][j-1]
        if i != 0:
            p = true_predict / (true_predict + false_predict)
            precision[i-1].append(p)
            total_true_predict = total_true_predict + true_predict


        print()
        
    #print precision      
    print ("precision for each class ")
    for i in range(len(test)):
        print("Class{} =  {}" .format((i+1),precision[i]))
    
        
    accuracy = total_true_predict/total_points
    print ("accuracy  ", accuracy)
