import tensorflow as tf

def analyze():
	hello = tf.constant('Hello, TensorFlow!')
	sess = tf.Session()
	return sess.run(hello)

def anomaly_detection():
	pass
