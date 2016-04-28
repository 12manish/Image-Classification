#Jose Gonzalez
#CIFAR-10 classifiers
#CSCI 334 Data Mining


#READ ME!!!!! -- I suggest putting each section (marked by #doesthis) in its own section on jupyter.
#     MUST RUN CLASSIFIERS BEFORE 10-FOLD CROSS VALIDATION CAN BE SUCCESSFUL


#prepare data
import pandas as pd
from sklearn.cross_validation import train_test_split

data = pd.read_csv('train1p_with_header.csv')
X=data.iloc[:,0:data.shape[1]-1].as_matrix()
y=data.iloc[:,data.shape[1]-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    

#pca->lda classifier
import numpy as np
from sklearn.decomposition import PCA
from sklearn.lda import LDA

def pca_lda(X_train,X_test,y_train,y_test):
    pca = PCA(n_components=500)
    lda = LDA()
    pca.fit(X_train)
    scores = np.dot(X_train,np.transpose(pca.components_))
    lda.fit(scores, y_train)
    return lda.score(scores, y_train, sample_weight=None)

pca_lda(X_train,X_test,y_train,y_test)



#pca->rfc classifier
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

def pca_rfc(X_train,X_test,y_train,y_test):
    pca = PCA(n_components=500)
    pca.fit(X_train)
    scores = np.dot(X_train,np.transpose(pca.components_))
    rfc = RandomForestClassifier(n_estimators=500, oob_score=True, random_state = 60)
    rfc.fit(scores,y_train)
    return rfc.oob_score_

pca_rfc(X_train,X_test,y_train,y_test)



#pca->knn classifier
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

def pca_knn(X_train,X_test,y_train,y_test):
    pca = PCA(n_components=500)
    pca.fit(X_train)
    scores = np.dot(X_train,np.transpose(pca.components_))
    knn = KNeighborsClassifier(10)
    knn.fit(scores,y_train)
    return knn.score(scores, y_train)
    
pca_knn(X_train,X_test,y_train,y_test)


#10 fold cross validation
from sklearn.cross_validation import KFold
import numpy as np

tenKFold = KFold(len(X[:,0]), 10)
accuracy = np.zeros(10)
i=0
for train_index, test_index in tenKFold:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    accuracy[i]= pca_rfc(X_train,X_test,y_train,y_test)
    print accuracy[i]
    i+=1
print(sum(accuracy)/10)