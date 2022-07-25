import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras import Input


# Importing our data and saving it to variables
country_data = pd.read_csv(".\world-happiness-report-2021.csv")

X = country_data.filter(['Logged GDP per capita', 'Social support', 'Healthy life expectancy'])

Y = country_data['Ladder score']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = Sequential()
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_absolute_error')

model.fit(X_train, Y_train, epochs=200, batch_size=32)

Y_hat = model.predict(X_test)

mse = mean_squared_error(Y_test, Y_hat)

print(mse)