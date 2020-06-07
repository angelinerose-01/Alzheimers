import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import plot_roc_curve
import pickle 

data = pd.read_csv("C:/Users/Angel/Desktop/JUPYTER/oasis_longitudinal.csv")

data['Group'].replace(['Nondemented','Demented','Converted'] , [0,1,1],inplace = True)
data['M/F'].replace(['M','F'],[1,0],inplace = True)

start,stop,step = 5,9,1
data['Subject ID'] = data['Subject ID'].str.slice(start,stop,step)

data.drop( ['MRI ID' , 'Hand' ] ,axis = 1, inplace = True)

data["SES"].fillna(data.groupby("EDUC")["SES"].transform("median"), inplace=True)
data["MMSE"].fillna(data['MMSE'].mean(),inplace = True)

x = data.drop('Group',axis = 1)
y = data['Group']


np.random.seed(200)
from sklearn.ensemble import RandomForestClassifier
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2)
model = RandomForestClassifier()
model.fit(xtrain, ytrain)
pickle.dump(model,open('model.pkl','wb'))
ypreds = pickle.load(open('model.pkl','rb'))

print(ypreds.predict([[0,1,0,1,87,14,2,27,0,1987,0.696,0.883]]))
print(x)
# print(ypreds.score(xtest, ytest))


# ypreds = model.predict(xtest)


# print("Classifier metrics on the test set")
# print(f"Accuracy: {accuracy_score(ytest, ypreds)*100:.2f}%")
# print(f"Precision: {precision_score(ytest, ypreds)}")
# print(f"Recall: {recall_score(ytest, ypreds)}")
# print(f"F1: {f1_score(ytest, ypreds)}")