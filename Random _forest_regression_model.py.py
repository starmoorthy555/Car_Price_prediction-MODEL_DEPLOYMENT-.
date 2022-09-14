import pandas as pd

data = pd.read_csv('C:/Users/Makro_1997/car data.csv')

print(data.columns)

df = data[['Year','Selling_Price','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner']]

df['Current_year'] = 2020

df['No_of_Years'] = df['Current_year'] - df['Year']

df.drop('Current_year',axis=1,inplace=True)

df.drop('Year',axis=1,inplace=True)

df = pd.get_dummies(df,drop_first=True)

x =df.iloc[:,1:].values
y =df.iloc[:,0].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.ensemble import RandomForestRegressor
re = RandomForestRegressor()

from sklearn.model_selection import RandomizedSearchCV

import numpy as np

#Number of trees in the Random_Forest
n_estimators = [int(x) for x in np.linspace(start=100,stop=1200,num=12)]
#Numbe rof Feature in every split.
max_features = ['auto','sqrt']
#Max Leaves in the Trees.
max_depth = [int(x) for x in np.linspace(start=5,stop=30,num=6)]
#Minimum number of samples required in a split.
min_samples_split = (2,5,10,15,100)
#Minimum number of leaf required to do a split.
min_samples_leaf = (1,2,5,10)

random_grid ={'n_estimators':n_estimators,
              'max_features':max_features,
              'max_depth':max_depth,
              'min_samples_split':min_samples_split,
              'min_samples_leaf':min_samples_leaf}

rf_random = RandomizedSearchCV(estimator=re,param_distributions=random_grid,scoring='neg_mean_squared_error')

rf_random.fit(x_train,y_train)

predictions = rf_random.predict(x_test)

print(predictions)

from sklearn import metrics
print('MSE',metrics.mean_squared_error(y_test,predictions))
print('MAE',metrics.mean_absolute_error(y_test,predictions))

import pickle
file = open('model.pkl','wb')
pickle.dump(rf_random, file)