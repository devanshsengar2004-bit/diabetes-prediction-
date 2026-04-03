import pandas as pd 


data = pd.read_csv("diabetes.csv")

print(data.shape)
print(data.head())
print(data.info())
print(data.isnull().sum())

x = data.drop("Outcome",axis =1)
y = data["Outcome"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=41)

print("training data:",x_train.shape)
print("testing data:",x_test.shape)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)

print("model train ho gaya!")

from sklearn.metrics import accuracy_score
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)

import numpy as np
meri_values = np.array([[6,148,72,35,0,33.6,0.627,50]])

prediction = model.predict(meri_values)
if prediction[0] ==0:
    print("aapko diabetes nhi hai:")
else:
    print("aapko diabetes hai:")
