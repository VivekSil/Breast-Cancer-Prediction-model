import numpy as np
def get_data():
    x_train=np.load("X.npy")
    y_train=np.load("Y.npy")
    x_return = x_train[0:5000]
    y_return = y_train[0:5000]
    return x_return,y_return

