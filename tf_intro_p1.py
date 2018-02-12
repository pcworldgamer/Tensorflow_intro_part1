# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:19:16 2018

@author: pjcfe
"""

import tensorflow as tf

node1 = tf.constant(3.0)
node2 = tf.constant(4.0, dtype=tf.float32)

sess = tf.Session()
tf.reset_default_graph()

print(node1,node2)
print(sess.run([node1,node2]))

sumnodes = tf.add(node1,node2)
print(sess.run(sumnodes))