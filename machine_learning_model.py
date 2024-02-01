# Final Project - Machine Learning for Prediction
# Authors: Sahil Chand, Devin Dang
# Nov 19, 2020
# Using Machine Learning and Artificial Intelligence to make predictions

import useful_functions as f
# creating training set for step 3
train_input = f.generate_input_list()
train_output = f.generate_output_list(train_input)

# Step 3:

# scikit-learn package train model using the training set
# Model is used to predict for the test data
# Send training set to fit() to create model(also trains it)
# After the model is trained, send to predict() function
# training input is in a list called train_input
# training output is called training_output
from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs = -1)
predictor.fit(X = train_input, y = train_output)

# Step 4:

#Using the model predict the outcome of [10,20,30]
# X_test = [10,20,30]
# y should = 140
#coefficients should be [1,2,3]
X_test = [[10,20,30]]#test data
outcome = predictor.predict(X=X_test)
coefficients = predictor.coef_

print(str(outcome))#Prediction
print(str(coefficients))#Coefficient