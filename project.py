import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

data = pd.read_csv('diabetes.csv')
#Include the features only
X = data.drop(columns=['Outcome'])
#Include the target variable
Y = data['Outcome']

#Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

model1 = GaussianNB()

#Train model
model1.fit(X_train,y_train)

y_pred1 = model1.predict(X_test)

accuracy1 = accuracy_score(y_test,y_pred1)

