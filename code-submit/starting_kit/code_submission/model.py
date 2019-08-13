from lenet import Lenet
from PIL import Image

import tensorflow.examples.tutorials.mnist.input_data as input_data
import tensorflow as tf
import numpy as np
import csv
import os

lenet = Lenet()
sess = tf.Session()
saver = tf.train.Saver()

def trainLenet(data_path,parameter_path):


    for task in range(len(data_path)):
        mnist = input_data.read_data_sets(data_path[task], one_hot=True)
        batch_size = 50
        max_iter = 100

        if task==0:
            sess.run(tf.initialize_all_variables())
        
        max_accuracy=0
        for i in range(max_iter):
            batch = mnist.train.next_batch(batch_size)
            if i % 10 == 0:
                train_accuracy = sess.run(lenet.train_accuracy,feed_dict={
                    lenet.raw_input_image: batch[0],lenet.raw_input_label: batch[1]
                })
                print("step %d, training accuracy %g" % (i, train_accuracy))
                if max_accuracy<train_accuracy:
                    save_path = saver.save(sess, parameter_path[task])
            sess.run(lenet.train_op,feed_dict={lenet.raw_input_image: batch[0],lenet.raw_input_label: batch[1]})


class inference:

    def __init__(self):pass


    def predict(self,image):
        img = image.convert('L')
        img = img.resize([28, 28], Image.ANTIALIAS)
        image_input = np.array(img, dtype="float32") / 255
        image_input = np.reshape(image_input, [-1, 784])

        predition = sess.run(lenet.prediction, feed_dict={lenet.raw_input_image: image_input})[0]
        return predition

def predictLenet(test_path,para_path,result_path):
    infer = inference()
    for i in range(len(test_path)):
        with open(result_path[i],'w') as file:
            writer=csv.writer(file)
            for j in range(i+1):
                img_path=os.listdir(test_path[j])
                img_path.sort()
                saver.restore(sess,para_path[j])
                result=[]
                for path in img_path:
                    img=Image.open(os.path.join(test_path[j],path))
                    result.append(infer.predict(img))
                writer.writerow(result)

def Model(train,para,test,result):
    trainLenet(train,para)
    predictLenet(test,para,result)
    
