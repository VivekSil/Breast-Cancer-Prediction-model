import numpy as np
def get_data():
    x_test=np.load("X.npy")
    y_test=np.load("Y.npy")
    x_return = x_test[5000:5547]
    y_return = y_test[5000:5547]
    return x_return,y_return
