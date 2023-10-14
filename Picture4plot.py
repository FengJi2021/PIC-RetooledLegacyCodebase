# _*_ coding:utf-8 _*_
# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 9 - regression example
"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import theano
import theano.tensor as T
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Layer(object):
    def __init__(self, inputs, in_size, out_size, activation_function=None):
        self.W = theano.shared(np.random.normal(0, 1, (in_size, out_size)))
        self.b = theano.shared(np.zeros((out_size, )) + 0.1)
        self.Wx_plus_b = T.dot(inputs, self.W) + self.b
        self.activation_function = activation_function
        if activation_function is None:
            self.outputs = self.Wx_plus_b
        else:
            self.outputs = self.activation_function(self.Wx_plus_b)


# Make up some fake data
x1_data = np.linspace(0, 100, 300)
print(x1_data)
x2_data = np.linspace(0, 0.01, 300)
print(x2_data)
x1_data,x2_data = np.meshgrid(x1_data,x2_data)
noise = np.random.normal(0, 10, x1_data.shape)
y_data = np.exp(np.log(248.945) + 0.135*np.log(x1_data) + 0.147*np.log(x2_data) + 0.62*np.log(2) ) +noise      # y = x^2 - 0.5

# show the fake data
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x1_data, x2_data,y_data,rstride=1, cstride=1, cmap='rainbow')
plt.show()
