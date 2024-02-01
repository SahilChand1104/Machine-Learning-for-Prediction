# Final Project - Machine Learning for Prediction
# Authors: Sahil Chand, Devin Dang
# Dec 4, 2020
# Using Machine Learning and Artificial Intelligence to make predictions

# Used turtle methods from: 
# https://docs.python.org/3/library/turtle.html

import turtle

def label(title,value,y):
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
    # used to fill more of the graph vertically
    height *= 2

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
file = open("Part_2_graph_data.csv")

# making the drawing fast
david.speed(9)
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
line_counter = 0

# iterating through each line of file
for line in file:
    line_counter += 1
    # changing the line of the file into a list of elements from the line
    line_list = line.split(",")
    # checking if the line_counter is even
    if line_counter % 2 == 0:
        # calling the label function with a larger y value to stagger labels
        # using both columns from the file
        label(line_list[0],line_list[1], 80)
    else:
        label(line_list[0],line_list[1], 40)
    # calling bar function with the 2nd column file data
    bar(int(line_list[1]))
    # spacing in between each bar
    david.forward(10)
# making the turtle invisible to not distract away from graph
david.hideturtle()
