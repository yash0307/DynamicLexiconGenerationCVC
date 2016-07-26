from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import datetime
import glob
import hashlib
import os.path
import random
import re
import sys
import tarfile
import json

import numpy as np
from six.moves import urllib
import tensorflow as tf

from tensorflow.python.client import graph_util
from tensorflow.python.framework import tensor_shape
from tensorflow.python.platform import gfile

OUTPUT_TENSOR_NAME = 'final_result:0'
MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3
JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'


def create_inception_graph():
  """"Creates a graph from saved GraphDef file and returns a Graph object.

  Returns:
    Graph holding the trained Inception network, and various tensors we'll be
    manipulating.
  """
  with tf.Session() as sess:
    model_filename = './Dataset_dict/output_graph.pb'
    with gfile.FastGFile(model_filename, 'rb') as f:
      graph_def = tf.GraphDef()
      graph_def.ParseFromString(f.read())
      final_tensor, jpeg_data_tensor, resized_input_tensor = (
          tf.import_graph_def(graph_def, name='', return_elements=[
              OUTPUT_TENSOR_NAME, JPEG_DATA_TENSOR_NAME,
              RESIZED_INPUT_TENSOR_NAME]))
  return sess.graph, final_tensor, jpeg_data_tensor, resized_input_tensor


def run_graph_on_image(sess, image_data, image_data_tensor,
                            bottleneck_tensor):
  """Runs inference on an image to extract the final layer.

  Args:
    sess: Current active TensorFlow Session.
    image_data: Numpy array of image data.
    image_data_tensor: Input data layer in the graph.
    bottleneck_tensor: Layer before the final softmax.

  Returns:
    Numpy array of bottleneck values.
  """
  bottleneck_values = sess.run(
      bottleneck_tensor,
      {image_data_tensor: image_data})
  bottleneck_values = np.squeeze(bottleneck_values)
  return bottleneck_values




def main(_):
  # Set up the pre-trained graph.
  graph, final_tensor, jpeg_data_tensor, resized_image_tensor = (
      create_inception_graph())

  sess = tf.Session()

  image_path = '/media/DADES/yash/MS-COCO/inceptionImages/validation/COCO_train2014_000000369653.jpg'
  if (len(sys.argv) > 1):
    image_path = sys.argv[1];

  image_data = gfile.FastGFile(image_path, 'rb').read()
  final_values = run_graph_on_image(sess, image_data,
                                                jpeg_data_tensor,
                                                final_tensor)

  print(final_values)

if __name__ == '__main__':
  tf.app.run()
