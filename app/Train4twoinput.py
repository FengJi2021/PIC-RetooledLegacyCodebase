# _*_ coding:utf-8 _*_
import numpy as np
import tensorflow as tf


def add_Layer(inputs, in_size, out_size, activation_function):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]) * 1)
    biases = tf.Variable(tf.random_normal([1, out_size]) * 1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


xs = tf.placeholder(tf.float32, [None, 2])
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_Layer(xs, 2, 50, tf.nn.sigmoid)
l2 = add_Layer(l1, 50, 60, tf.nn.sigmoid)
l3 = add_Layer(l2, 60, 70, tf.nn.sigmoid)
prediction = add_Layer(l3, 70, 1, None)
loss = tf.reduce_mean(
    tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1])
)
LR = 0.005
train_step = tf.train.AdamOptimizer(LR).minimize(loss)

samplesize = 10
x1_data0 = np.linspace(0, 100, samplesize)
x2_data0 = np.linspace(0, 10, samplesize)
x1_data, x2_data = np.meshgrid(x1_data0, x2_data0)
x1_data1D = x1_data.flatten()
x2_data1D = x2_data.flatten()
x1_data = x1_data1D[:, np.newaxis]
x2_data = x2_data1D[:, np.newaxis]
x_data = np.concatenate((x1_data, x2_data), axis=1)
noise = np.random.normal(0, 10, x1_data.shape)
y_data = np.exp(
    np.log(248.945)
    + 0.135 * np.log(x1_data)
    + 0.147 * (np.log(x2_data) + np.log(0.001))
    + 0.62 * np.log(2)
)
print("第一特征参数矩阵", x1_data)
print("第二特征参数矩阵", x2_data)
x_data = np.concatenate((x1_data, x2_data), axis=1)
print("特征参数矩阵", x_data)


print("输出矩阵", y_data)
loss = tf.reduce_mean(
    tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1])
)
saver = tf.train.Saver()
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
for i in range(20000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    mse = sess.run(loss, feed_dict={xs: x_data, ys: y_data})
    if mse <= 1:
        print("Wir haben Ergebnis gefunden!!!")
        # save_path = Saver.save(
        #     sess,
        #     "C:\\Users\\admin\\Desktop\\
        # abschlussproject\\Neuralnew\\save2inputnetBEST.ckpt",
        # )
        break
    elif i == 0 or i % 1000 == 0:
        print(mse)
