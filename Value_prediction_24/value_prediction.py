# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 7/9/2023 9:39 am

from model import Prediction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction:
    #inputs: A list of input values about years
    #outputs: A list of output values corresponding to the inputs.
    #input_value: A single input value for which the prediction is desired.
    # plot: An optional boolean argument that, when set to True, plots the given data and the linear regression line
    if len(inputs) != len(outputs):
        raise Exception('Length of "inputs" and "outputs" must match...')

    # Create a dataframe for out data:
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})
    # # Here, we're using the pandas library to create a DataFrame (a table-like structure).
    # This makes it easier to manipulate and visualize data.
    # The inputs list becomes a column named 'inputs'.
    # The outputs list becomes a column named 'outputs'.


    # Firstly, we are converting the 'inputs' and 'outputs' series from the DataFrame into numpy arrays.
    # This conversion facilitates mathematical operations, as numpy is optimized for numerical calculations.
    # Sklearn expect the input X to be a two-dimensional array (or matrix)
    # Reshape the data using Numpy (X: inputs, Y: outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    # The inputs and outputs are reshaped to a column vector form using NumPy.
    # such as :[[1]
    #           [5]
    #           [9]]
    # X will store our input values, and y will store our output values.
    # The -1 in reshape means "unknown dimension", which basically allows numpy to automatically infer the correct shape.
    # In the other words, -1 is used as a placeholder that means "whatever is needed", so by using -1,
    # we let numpy to automatically calculate the number of rows that is necessary to maintain the number of elements in the array.
    # The value 1 tells numpy that we want the array to have one column.
    y = np.array(df['outputs']).reshape(-1, 1)

    # Split the data into training data to test our model
    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=.20)
    # random_state=0: always get the same outcome.

    # Initialize the model and test it:
    model = LinearRegression()
    model.fit(train_X, train_y)

    # Prediction
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    # Testing for accuracy
    y_test_prediction = model.predict(test_X)

    # PLot
    if plot:
        display_plot(inputs=X, outputs=y, y_line=y_line)
        # raise NotImplementedError('Plot function has not been created yet.')

    return Prediction(value=y_prediction[0][0],
                      r2_score=r2_score(test_y, y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_y, y_test_prediction))


def display_plot(inputs: list[float], outputs: list[float], y_line):
    # This function is used to visualize the data points and the linear regression line.
    # It takes the inputs, outputs, and the regression line (y_line) as arguments.
    plt.scatter(inputs, outputs, s=12)
    # This line uses plt.scatter to create a scatter plot.
    # inputs are plotted on the x-axis and outputs on the y-axis.
    # s=12 determines the size of each point in the scatter plot.
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.plot(inputs, y_line, color='r')
    # This line uses plt.plot to draw the linear regression line.
    # inputs are on the x-axis and y_line gives the corresponding values on the y-axis for the regression line.
    # color='r' specifies that the line should be red.
    plt.show()


if __name__ == '__main__':
    years: list[int] = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]
    earnings: list[float] = [1000, 300, 1100, 1300, 1400, 1300, 1500, 1550]
    my_input: int = 2040

    prediction: Prediction = make_prediction(inputs=years, outputs=earnings,input_value=my_input, plot=True)
    print('Input:', my_input)
    print(prediction)
    print(prediction.mean_absolute_error)
