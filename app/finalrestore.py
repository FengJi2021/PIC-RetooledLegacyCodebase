# _*_ coding:utf-8 _*_
import tensorflow as tf
import numpy as np

###########################�ָ�����ṹ##########################################
def add_Layer(inputs,in_size,out_size,activation_function):
    Weights = tf.Variable(tf.random_normal([in_size,out_size])*1)
    biases = tf.Variable(tf.random_normal([1,out_size])*1)
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

xs = tf.placeholder(tf.float32,[None,3])
ys = tf.placeholder(tf.float32,[None,3])
l1 = add_Layer(xs, 3, 50, tf.nn.sigmoid)
l2 = add_Layer(l1, 50, 60, tf.nn.sigmoid)
l3 = add_Layer(l2, 60, 70, tf.nn.sigmoid)
prediction = add_Layer(l3, 70, 3, None)
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices = [1]))
LR = 0.005
train_step = tf.train.AdamOptimizer(LR).minimize(loss)

##############恢复输入量##########################
x_data = [[18.85,5,2],[18.85,6,2.5],[18.85,7,3],[18.85,8,3.5],[37.7,5,2.5],[37.7,6,2],[37.7,7,3.5],[37.7,8,3],[56.55,5,3],[56.55,6,3.5],[56.55,7,2],[56.55,8,2.5],[75.4,5,3.5],[75.4,6,3],[75.4,7,2.5],[75.4,8,2]]
y_data = [[261.1,289.04,458.87],[307.88,329.83,458.87],[352.62,367.82,761.88],[395.68,403.59,924.41],[329.14,379.26,788.18],[294.40,359.46,620.64],[426.05,468.97,1207.99],[389.27,452.65,1025.01],[389.27,454.27,1148.53],[439.94,503.71,1400.99],[318.09,412.55,744.40],[372.53,465.86,978.46],[445.31,521.67,1544.02],[415.71,508.82,1317.12],[379.79,487.55,1084.11],[337.27,457.27,849.14]]
a1=80;b1=4;c1=3
FX = np.exp(np.log(248.945) + 0.135*np.log(a1) + 0.147*(np.log(b1)+np.log(0.001)) + 0.62*np.log(c1))
FY = np.exp(np.log(317.26) + 0.258*np.log(a1) + 0.215*(np.log(b1)+np.log(0.001)) + 0.416*np.log(c1))
FZ = np.exp(np.log(110.728) + 0.407*np.log(a1) + 0.109*(np.log(b1)+np.log(0.001)) + 1.16*np.log(c1))
y_dataOR = [[FX,FY,FZ],]

print("特征参数矩阵",len(x_data))
print("输出矩阵",len(y_data))    
saver = tf.train.Saver()


with tf.Session() as sess:
    saver.restore(sess,"C:\\Users\\admin\\Desktop\\abschlussproject\\3input\\save3inputnetBEST.ckpt")
    prediction_value = sess.run(prediction,feed_dict={xs:x_data})
    los = sess.run(loss,feed_dict={xs:x_data,ys:y_data})
#     print(prediction_value)
    print("均方误差：",los)
    print("网络结果：",prediction_value)
    prediction_value1 = sess.run(prediction,feed_dict={xs:[[a1,b1,c1],]})
    los1 = y_dataOR -prediction_value1
    print("预测结果：",prediction_value1)
    print("实际结果：",y_dataOR)
    print("预测误差：",los1)
    
    
    
    
    
    
    
    