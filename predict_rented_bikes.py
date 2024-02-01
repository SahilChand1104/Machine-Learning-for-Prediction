# Final Project - Machine Learning for Prediction
# Authors: Sahil Chand, Devin Dang
# Nov 24, 2020
# Using Machine Learning and Artificial Intelligence to make predictions

import useful_functions as f

# Step 1

file = open("SeoulBikeData.csv")
unneeded_header = file.readline()#Remove header
# output: Second column is the rented bike count
# inputs: columns 3-10(positions[2-10]) that are numerical values
output_list = []
input_list = []

# loop for going over each line in SeoulBikeData.csv
for line in file:
  # turning line into a list with values from the file
  values_list = line.split(",")

  output_list += [float(values_list[1])]#adds values of 2nd column to output_list
  #num = float(values_list[1])
  #output_list += [num]

  # used to build the list of lists (input_list)
  list_of_floats = []
  # loop to get values from column 3 to 11
  for value in values_list[2:11]:
    list_of_floats += [float(value)]
  input_list += [list_of_floats]
  #print(list_of_floats)

#print(output_list)
#print(len(output_list))
#print(input_list)

# testing is 20%
# training is 80%

# calling split_80_20 function to split up input_list
training_input = f.split_80_20(input_list)[0]
test_input = f.split_80_20(input_list)[1]
#print(training_input)

# calling split_80_20 function to split up output_list
training_output = f.split_80_20(output_list)[0]
test_output = f.split_80_20(output_list)[1]
#print(training_output)
#print(test_output)

#o = len(training_input)
#print(o)

# Step 2

from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs = -1)
predictor.fit(X = training_input, y = training_output)

# Step 3

test_data = test_input
result = predictor.predict(X=test_data)

#print(str(result))
#print(test_output)

# Step 4

# dictionary for counting predictions' percentage errors
# based off how close each prediction was compared to its actual value
# key names are intervals between those two percentages
prediction_percentage_count = {
  "zero_ten":0,
  "ten_twenty":0,
  "twenty_thirty":0,
  "thirty_forty":0,
  "forty_fifty":0,
  "fifty_sixty":0,
  "sixty_seventy":0,
  "seventy_eighty":0,
  "eighty_ninety":0,
  "ninety_hundred":0,
  "hundred_or_more":0
  }

# looping for the length of the actual values
for i in range(len(result)):
  # ignoring any actual value that is 0.0 to avoid dividing by 0
  if test_output[i] != 0.0:
    # percentage Error formula using values from test_output and result
    percentageError = (abs(test_output[i]-result[i])/test_output[i])*100
    #print(percentageError)

    percentage_interval_found = False
    start_percentage = 0
    end_percentage = 10
    key_index = 0
    keys_list = list(prediction_percentage_count.keys())

    # looping using control variable
    while not(percentage_interval_found):
      # special case to handle percentage errors above 100%
      if percentageError > 100:
        prediction_percentage_count["hundred_or_more"] += 1
        percentage_interval_found = True
      # checking if current percentage error is within the start and end interval
      # also handles percentage errors that are equal to the end interval
      elif percentageError > start_percentage and percentageError <= end_percentage:
        # adding to the value of one key from the dictionary
        prediction_percentage_count[keys_list[key_index]] += 1
        percentage_interval_found = True
      else:
        # changing intervals to see if percentageError is in the next interval
        start_percentage = end_percentage
        end_percentage += 10
        #print(start_percentage)
        #print(end_percentage)
        key_index += 1

print(prediction_percentage_count.items())