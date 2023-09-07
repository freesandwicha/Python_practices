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
    if len(inputs) != len(outputs):
        raise Exception('Length of "inputs" and "outputs" must match...')

    # Create a dataframe for out data:
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    # Reshape the data using Numpy (X: inputs, Y: outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    # The inputs and outputs are reshaped to a column vector form using NumPy.
    # such as :[[1]
    #           [5]
    #           [9]]
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
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.plot(inputs, y_line, color='r')
    plt.show()


if __name__ == '__main__':
    years: list[int] = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]
    earnings: list[float] = [1000, 300, 1100, 1300, 1400, 1300, 1500, 1550]
    my_input: int = 2040

    prediction: Prediction = make_prediction(inputs=years, outputs=earnings,input_value=my_input, plot=True)
    print('Input:', my_input)
    print(prediction)
    print(prediction.mean_absolute_error)
