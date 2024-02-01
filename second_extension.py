# Final Project - Machine Learning for Prediction
# Authors: Sahil Chand, Devin Dang
# Dec 5, 2020
# Using Machine Learning and Artificial Intelligence to make predictions

import useful_functions as f

filename = input("Please type in the name of your file: ")
file = open(filename)
#file = open("SeoulBikeData.csv")#Made testing easier
file.readline()
#print(file)

output_index = input("Type in the index for the prediction column: ")
input_index_start = input("Type in the starting index for input columns: ")
input_index_end = input("Type in the last index for the input columns: ")
index_end = int(input_index_end) + 1 #Converts to integer (so we can take index)
index_start = int(input_index_start)#Converts to integer (so we can take index)
output_index_integer = int(output_index)#Converts to integer

#print(index_start)
#print(output_index_integer)
#print(index_end)

output_list = []#List for the prediction outcomes
input_list = []#List of the input values

for line in file:
  # turning line into a list with values from the file
  values_list = line.split(",")

  # adds values of prediction column to output_list
  output_list += [float(values_list[output_index_integer].strip("\n"))]
#print(output_list)

  # used to build the list of lists (input_list)
  list_of_floats = []
  # loop to get values from input columns one line at a time
  for value in values_list[index_start:index_end]:
    list_of_floats += [float(value.strip("\n"))]
  input_list += [list_of_floats]

#print(input_list)

training_input = f.split_80_20(input_list)[0]
test_input = f.split_80_20(input_list)[1]
#print(training_input)
#print(test_input)

training_output = f.split_80_20(output_list)[0]
test_output = f.split_80_20(output_list)[1]
#print(training_output)
#print(test_output)

from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs = -1)
predictor.fit(X = training_input, y = training_output)

test_data = test_input
result = predictor.predict(X=test_data)

#print(result)
#print(test_output)

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