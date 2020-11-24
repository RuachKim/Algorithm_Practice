import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


rng = np.random

learning_rate = 0.001
training_steps = 10000
display_step = 50

X = np.array([1.1,2.3,3.1,4.2,5.4,6.3,7.1,8.9,9.4,10.1,12.1,12.9,19.2])
Y = np.array([2,4,6,8,10,12,14,16,18,20,24,26,40])

#pred, loss = 0, 0
n_samples = X.shape[0]
#print(n_samples)

W = tf.Variable(rng.randn(), name = 'weight')
b = tf.Variable(rng.randn(), name = 'bias')

def linear_regression(x):
    return W*x + b

def mean_square(y_pred, y_true):
    return tf.reduce_sum(tf.pow(y_pred-y_true, 2) / (2*n_samples))

optimizer = tf.optimizers.SGD(learning_rate)

def run_optimization():

    with tf.GradientTape() as g:
        pred = linear_regression(X)
        loss = mean_square(pred, Y)

    gradients = g.gradient(loss, [W,b])

    optimizer.apply_gradients(zip(gradients, [W,b]))


for step in range(1, training_steps + 1):

    run_optimization()

    if step % display_step == 0:
        pred = linear_regression(X)
        loss = mean_square(pred, Y)
        print("step: %i, loss: %f, W: %f. b: %f" % (step, loss, W.numpy(), b.numpy()))

inp = 50
print('predicted value: %f --> %f' % (inp, W*inp + b))

plt.plot(X, Y, 'ro', label='Original data')
plt.plot(X, np.array(W*X + b), label ='Fitted line')
plt.legend()
plt.show()


