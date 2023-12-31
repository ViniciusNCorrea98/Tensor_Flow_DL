import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#That just makes it easier for a network to learn
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
#Because we're going to work with 10 classes
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

#Parametrs to model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)
loss_value, acc_value = model.evaluate(x_test, y_test)
print(loss_value, acc_value)

plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()

model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')

predictions = new_model.predict([x_test])
print(predictions)
print(np.argmax(predictions[1]))

plt.imshow(x_test[1])
plt.show()






#print(x_train[0])