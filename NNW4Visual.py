# _*_ coding:utf-8 _*_
"""
Know more, visit my Python tutorial page: https://morvanzhou.github.io/tutorials/
My Youtube Channel: https://www.youtube.com/user/MorvanZhou
Dependencies:
tensorflow: 1.1.0
matplotlib
numpy
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

LR = 0.005
REAL_PARAMS = [0.135, 0.147]
INIT_PARAMS = [[0.3,0.3],
               [0.2,0.2],
               [10,-10]][2]

x1_data = np.linspace(1, 60, 20, dtype=np.float32)   # x data
x2_data = np.linspace(0.001,0.01,20,dtype=np.float32)

print(np.exp(np.log(248.945) + 0.135*np.log(x1_data) + 0.147*np.log(x2_data) + 0.62*np.log(2)))
y_fun = lambda a, b: (np.log(248.945) + a*np.log(x1_data) + b*np.log(x2_data) + 0.62*np.log(2.)) #c的值默认是0.62
tf_y_fun = lambda a, b: (tf.log(248.945) + a*tf.log(x1_data) + b*tf.log(x2_data) + 0.62*tf.log(2.))

noise = np.random.randn(20)/10
print(noise)
y = y_fun(*REAL_PARAMS)    +noise   # target
print("用于接近的值",y_fun(*REAL_PARAMS))

# tensorflow graph
a, b = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
pred = tf_y_fun(a, b)
mse = tf.reduce_mean(tf.square(y-pred))
train_op = tf.train.GradientDescentOptimizer(LR).minimize(mse)

a_list, b_list, cost_list = [], [], []
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for t in range(400):
        a_, b_, mse_ = sess.run([a, b, mse])
        a_list.append(a_); b_list.append(b_); cost_list.append(mse_)
        print(mse_)    # record parameter changes
        result, _ = sess.run([pred, train_op])  
                               # training


# visualization codes:
print('a=', a_, 'b=', b_)
# plt.figure(1)
# plt.scatter(x, y, c='b')    # plot data
# plt.plot(x, result, 'r-', lw=2)   # plot line fitting
# 3D cost figure
fig = plt.figure(2); ax = Axes3D(fig)
a3D, b3D = np.meshgrid(np.linspace(-10, 10, 30), np.linspace(-10,2, 30))  # parameter space
cost3D = np.array([np.mean(np.square(y_fun(a_, b_) - y)) for a_, b_ in zip(a3D.flatten(), b3D.flatten())]).reshape(a3D.shape)
ax.plot_surface(a3D, b3D, cost3D, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'), alpha=0.5)
ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='r')  # initial parameter place
ax.set_xlabel('a'); ax.set_ylabel('b')
ax.plot(a_list, b_list, zs=cost_list, zdir='z', c='r', lw=3)    # plot 3D gradient descent
plt.show()
