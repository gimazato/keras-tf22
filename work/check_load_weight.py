####
import tensorflow as tf
mnist = tf.keras.datasets.mnist

train_mode = False
#train_mode = False

if train_mode:
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
 
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  #tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(256, activation=tf.nn.relu),
  #tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.summary()
#model.layers[1]._name = model.layers[1].name + "_new"
#model.layers[2]._name = model.layers[2].name + "_new"
#model.layers[3]._name = model.layers[3].name + "_new"
model.load_weights('param_model1-256.hdf5', by_name=True)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
for layer in model.layers:
  layer._name = layer.name + "_renew"


print("\n\n-----------------")
model.summary()
#model.summary()

if train_mode: 
    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test, y_test)
    #model.save('param_model1-256.hdf5')