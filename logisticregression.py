import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
data=load_iris()
X=data.data
y=data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
log_reg=LogisticRegression(max_iter=200)
log_reg.fit(X_train_scaled,y_train)
y_pred=log_reg.predict(X_test_scaled)
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy of the Logistic Regression model: {accuracy:.2f}") 
print("\nConfusion Matrix:") 
print(confusion_matrix(y_test, y_pred)) 
print("\nClassification Report:") 
print(classification_report(y_test, y_pred)) 