#Neural Net in tensorflow 

###first define the graph  
import tensorflow as tf 
import numpy as np 

#parameters 
N,D,H=64,1000,100

#define the input and output 

x=tf.placeholder(tf.float32, shape=(N,D))
y=tf.placeholder (tf.float32,shape=(N,D))

#define the variable 
w1 =tf.Variable(tf.random_normal((D,H)))
w2 =tf.Variable(tf.random_normal((H,D)))

#feed foward network 
h=tf.maximum(tf.matmul(x,w1),0)
#relu function 
y_pred=tf.matmul(h,w2)
#define the loss function 
loss=tf.losses.mean_squared_error(y_pred,y)
#calculate the gradient 
optimizer=tf.train.GradientDescentOptimizer(1e-3)
#optimize the loss 
updates=optimizer.minimize(loss)


###run the graph many time 
with tf.Session() as sess: 
		sess.run(tf.global_variables_initializer())
		values={x:np.random.randn(N,D), y:np.random.randn(N,D)}
		for t in range (10): 
			 loss_val,_=sess.run([loss, updates],feed_dict=values)

print(loss_val)









