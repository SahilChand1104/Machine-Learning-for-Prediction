# Final Project - Machine Learning for Prediction
# Authors: Sahil Chand, Devin Dang
# Nov 19, 2020
# Using Machine Learning and Artificial Intelligence to make predictions

# Part 1 Steps 1&2

import random

def generate_input_list():
  """
  Input: no input
  Output: a list of lists
    Output will be a list with 100 sublists
    Each sublist has 3 random integers between 0 and 1000
  """
  
  main_list = []

  for i in range(100):
    sub_list = []
    for j in range(3):
      # calculate randint - parameters: 0 and 1000
      random_integer = random.randint(0,1000)
      sub_list += [random_integer]
    main_list += [sub_list]
    
  return main_list

def generate_output_list(list_of_lists):
  """
  Input: list_of_lists - a list containing some amount of sublists
    Assuming each sublist has 3 random integers between 0 and 1000
  Output: List of 100 integers
  """

  main_list = []

  for sublist in list_of_lists:
    total = 0 
    for num in sublist:
      # if - position of current int is 1
      if sublist[1] == num:
        # add current int times 2 to total
        total += num*2
      # elif - position of current int is 2
      elif sublist[2] == num:
        # add current int times 3 to total
        total += num*3
      # else - position of current int is 0
      else:
        # add current int to total
        total += num
    main_list += [total]

  return main_list

#test_list = generate_input_list()
#print(test_list)
#print(generate_output_list(test_list))

# Other functions

# function for Part 2 to split up input list and output list
def split_80_20(list_to_split):
  """
  Input: list_to_split - a list to be split into 2 lists
  Output: a tuple containing two lists
    1. 80% of list_to_split
    2. 20% of list_to split
  """

  list1 = []
  list2 = []

  # figuring out approx. 80% and 20% of list_to_split
  length_list = len(list_to_split)
  eighty_percent = length_list * (0.8)
  eighty_percent_index = int(eighty_percent)
  # 80% of list_to_split
  list1 += list_to_split[:eighty_percent_index]
  # 20% of list_to split
  list2 += list_to_split[eighty_percent_index:]

  return (list1,list2)