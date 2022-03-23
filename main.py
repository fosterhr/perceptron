import numpy
import random
import os

learning_rate = 1
training_iterations = 50

clear = lambda: os.system("cls")

bias = 1
weights = [random.random(), random.random(), random.random()]

def perceptron(input_1, input_2, output):
    temp_output = input_1 * weights[0] + input_2 * weights[1] + bias * weights[2]
    if temp_output > 0:
        temp_output = 1
    else:
        temp_output = 0

    error = output - temp_output

    weights[0] += error * input_1 * learning_rate
    weights[1] += error * input_2 * learning_rate
    weights[2] += error * bias * learning_rate

for i in range(training_iterations):
    perceptron(1, 1, 1)
    perceptron(1, 0, 1)
    perceptron(0, 1, 1)
    perceptron(0, 0, 0)

while True:
    clear()

    x = int(input("Enter an 'x' variable: "))
    y = int(input("Enter a 'y' variable: "))

    if (x == 0 or x == 1) and (y == 0 or y == 1):
        output = x * weights[0] + y * weights[1] + bias * weights[2]
        if output > 0:
            output = 1
        else :
            output = 0
        print("")
        print(x, "or", y, "is", output)
    else:
        print("")
        print("Invalid parameters provided.")
    print("")
    input("Press [ENTER] to continue.")
