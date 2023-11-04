# _*_ coding:utf-8 _*_
import numpy as np
import tensorflow as tf


# 恢复网络结构
def add_Layer(inputs, in_size, out_size, activation_function):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]) * 1)
    biases = tf.Variable(tf.random_normal([1, out_size]) * 1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


xs = tf.placeholder(tf.float32, [None, 3])
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_Layer(xs, 3, 50, tf.nn.sigmoid)
l2 = add_Layer(l1, 50, 60, tf.nn.sigmoid)
l3 = add_Layer(l2, 60, 70, tf.nn.sigmoid)
prediction = add_Layer(l3, 70, 1, None)
loss = tf.reduce_mean(
    tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1])
)
LR = 0.05
train_step = tf.train.AdamOptimizer(LR).minimize(loss)

samplesize = 10
# Make up some fake data
x1_data0 = np.linspace(0, 100, samplesize)
# print(x1_data0)
x2_data0 = np.linspace(0, 10, samplesize)
# print(x2_data0)
x3_data0 = np.linspace(2, 4, samplesize)
x1_data, x2_data = np.meshgrid(x1_data0, x2_data0)
x1_data1D = x1_data.flatten()
x2_data1D = x2_data.flatten()
x1_data, ignoreme = np.meshgrid(x1_data1D, x3_data0)
x2_data, x3_data = np.meshgrid(x2_data1D, x3_data0)
noise = np.random.normal(0, 10, x1_data.shape)
x1_data = x1_data.flatten()[:, np.newaxis]
x2_data = x2_data.flatten()[:, np.newaxis]
x3_data = x3_data.flatten()[:, np.newaxis]
y_data = np.exp(
    np.log(248.945)
    + 0.135 * np.log(x1_data)
    + 0.147 * (np.log(x2_data) + np.log(0.001))
    + 0.62 * np.log(x3_data)
)
print("第一特征参数矩阵", x1_data)
print("第二特征参数矩阵", x2_data)
print("第二特征参数矩阵", x3_data)
x_data = np.concatenate((x1_data, x2_data, x3_data), axis=1)
print("特征参数矩阵", x_data)
print("输出矩阵", y_data)

saver = tf.train.Saver()
with tf.Session() as sess:
    # saver.restore(
    #     sess,
    #     "C:\\Users\\admin\\Desktop\\abschlussproject\\
    #     Neuralnew\\save3inputnetBEST1.ckpt",
    # )
    loss = tf.reduce_mean(
        tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1])
    )
    loss_value = sess.run(loss, feed_dict={xs: x_data, ys: y_data})
    predict_value = sess.run(
        prediction,
        feed_dict={
            xs: [
                [75.4, 7, 2.5],
            ]
        },
    )

    print(loss_value)
    print(predict_value)
