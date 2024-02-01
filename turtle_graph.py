# Final Project - Machine Learning for Prediction
# Authors: Sahil Chand, Devin Dang
# Dec 6, 2020
# Using Machine Learning and Artificial Intelligence to make predictions

# Used turtle methods from: 
# https://docs.python.org/3/library/turtle.html

import second_extension as e
import turtle

def text(title,value,y):
    """
    Input:  title - the interval name as a string
            value - the count of percentage errors as a string
            y - the number of pixels to move along the y-axis
    Output: None     
    """
    david.penup()
    david.right(90)
    # using the y param. to place the label
    david.forward(y)
    # using write method of turtle to place label
    david.write(title.strip()+": \n"+value.strip(),False,align="left")
    david.backward(y)
    david.left(90)
    david.pendown()
    
def bar(height):
    """
    Input: height - the count of percentage errors as an integer
    Output: None
    """
    # adding color using fillcolor method
    david.fillcolor("blue")
    david.begin_fill()
    david.left(90)
    # using modified height to visualize the percentage errors
    david.forward(height)
    david.right(90)
    david.forward(40)
    david.right(90)
    david.forward(height)
    david.left(90)
    david.end_fill()

david = turtle.Turtle()
screen = turtle.Screen()
# dictionary data for percentage errors from second extension
data = e.prediction_percentage_count
# preparing labels and values for turtle graph
label_list = list(data.keys())
value_list = list(data.values())

# making the drawing fast
david.speed(9)
# resizing the turtle graph screen
screen.setup(width=750,height=800,startx=None,starty=-10)
# next 6 lines: creating the border for the graph
david.penup()
david.goto(-300,-300)
david.pendown()
for i in range(4):
    david.forward(600)
    david.left(90)
# used to center the bars
david.forward(30)
# counter used to stagger the labels
label_counter = 0

# iterating through each label of label_list
for label in label_list:
  label_counter += 1
  # getting the correlating value to label
  value = value_list[label_counter-1]
  # checking if the label_counter is even
  if label_counter % 2 == 0:
      # calling the text function with a larger y value to stagger labels,
      # value and label as strings
      text(label,str(value), 80)
  else:
      text(label,str(value), 40)
  
  if (value != 0):
      bar(value)
  # else to move forward using the bar width
  else:
      david.forward(40)
  # spacing in between each bar
  david.forward(10)
# making the turtle invisible to not distract away from graph
david.hideturtle()