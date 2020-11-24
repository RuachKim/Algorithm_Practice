#tensorflow 2.0 + Keras version

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_train = [i for i in range(1,10)]
y_train = [i for i in range(1,10)]

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=1))

sgd = tf.keras.optimizers.SGD(lr=0.01)

model.compile(loss='mean_squared_error', optimizer=sgd)
model.fit(x_train, y_train, epochs=1000)



plt.plot(x_train, y_train, 'ro', label='Original data')
plt.plot(x_train, model.predict(np.array(x_train)), label ='Prediction')
plt.legend()
plt.show()

print(model.predict(np.array([10])))