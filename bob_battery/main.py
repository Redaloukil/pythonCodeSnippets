import matplotlib



matplotlib.use("TkAgg")
import tkinter as Tkinter

import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split 
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
 # Load CSV and columns
df = pd.read_csv("data.csv")
 
print(df.shape)

df.plot(x="Battery_time" , y="Autonomy" , style="o")

# Plot outputs
# plt.scatter(X_test, Y_test,  color='black')
plt.title('BoB Battery')
plt.xlabel('Battery_time')
plt.ylabel('Autonomy')
# plt.xticks(())
# plt.yticks(())

# plt.show()

X = df.iloc[:, :-1].values  
y = df.iloc[:, 1].values 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create linear regression object
regr = linear_model.LinearRegression()
 
# Train the model using the training sets
regr.fit( X_train, y_train )
 
# Plot outputs
plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
 
plt.show()