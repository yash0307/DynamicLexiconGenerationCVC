from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


### git @ yash0307 ###
# This script does the following :
# 1). Loads Deep CNN model
# 2). Generates output for each image.
# 3). Outputs and saves annotation for each image

import gensim
import json
import os
import sys
import logging


# Include Tensorflow deploy script in this
# script only.
#################################################################################################
##################################### Tensorflow imports ########################################
#################################################################################################

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

from tensorflow.python.framework import graph_util
from tensorflow.python.framework import tensor_shape
from tensorflow.python.platform import gfile
##################################################################################################
################################# Tensorflow global variables ####################################
##################################################################################################

OUTPUT_TENSOR_NAME = 'final_result:0'
MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3
JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'
global graph
global final_tensor
global jpeg_data_tensor
global resized_image_tensor
global sess
global num_topics
###################################################################################################
#################################### Tensorflow functions #########################################
###################################################################################################
def create_inception_graph():
    """"Creates a graph from saved GraphDef file and returns a Graph object.
    Returns:
    Graph holding the trained Inception network, and various tensors we'll be
    manipulating.
    """
    with tf.Session() as sess:
        model_filename = '/home/yash/Data/flickr/Inception_models/output_graph_train_500.pb'
        with gfile.FastGFile(model_filename, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            final_tensor, jpeg_data_tensor, resized_input_tensor = (
                tf.import_graph_def(graph_def, name='', return_elements=[
                    OUTPUT_TENSOR_NAME, JPEG_DATA_TENSOR_NAME,
                    RESIZED_INPUT_TENSOR_NAME]))
    return sess.graph, final_tensor, jpeg_data_tensor, resized_input_tensor

def run_graph_on_image(sess, image_data, image_data_tensor,bottleneck_tensor):
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

def make_cnn_query(image_url):
    global graph
    global final_tensor
    global jpeg_data_tensor
    global resized_image_tensor
    global sess
    image_data = gfile.FastGFile(image_url, 'rb').read()
    final_values = run_graph_on_image(sess, image_data, jpeg_data_tensor, final_tensor)
    return (final_values)


###################################################################################################
############################## Tensorflow Initialize / main function ##############################
###################################################################################################
def tensorflow_init():
    global final_tensor
    global jpeg_data_tensor
    global resized_image_tensor
    global sess
    graph, final_tensor, jpeg_data_tensor, resized_image_tensor = (
        create_inception_graph())
    sess = tf.Session()

###################################################################################################
##################################### End Tensorflow ##############################################
###################################################################################################
global id2word
global lda_model

def main():
    global id2word
    global lda_model
    global num_topics

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # Open result file
    RESULTS_JSON_SUM = {}
    RESULTS_JSON_MAX = {}
    # Initialize tensorflow params.
    tensorflow_init()
    
    # First, read the dictionary and make a dictionary.
    id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')
    
    # Specify the number of topics present in the LDA_model.
    num_topics = 500

    # Image base_url.
    base_url_image = '/home/yash/Data/flickr/mirflickr/val/'

    # Parse the dictionary and Pre-process.
    iterator = id2word.iteritems()
    keys = id2word.keys()
    dict_natural = {}
    for i in range(0,len(keys)):
        temp_item = iterator.next()
        try:
            dict_natural[str(temp_item[1]).lower()] = []
        except:
            pass
    
    # Now, read the LDA model built on Natural dictionary.
    lda_model = gensim.models.ldamodel.LdaModel.load('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_500.lda', mmap='r')
    
    # Read, all the Validation set captions.
    # Combine each of them and make a document
    # Project the document on the LDA model.
    # Please verify with the CNN validation labels.
    
    # NOTE :The validation set of CNN is used here as 
    # Evaluation set for word-ranking.
    eval_file = open('/home/yash/Data/flickr/data.json','r')
    eval_json = json.load(eval_file)
    
    # Get all the topics only once.
    # YOU FETCH ONLY ONCE B-).
    # I'm bond! James Bond B-).

    # Iterate over each instance of eval set.
    counter_image = 0
    counter_word_instance = 0
    for ind in eval_json.keys():
        # Keep printing the counter values.
        counter_image += 1
        print ("Total 25K : " + str(counter_image))
        
        # Do this only for validation/testing images.
        if ((int(ind)%5 == 4) or (int(ind)%5 == 0)):
	    if ((int(ind)==924) or (int(ind)==705)):
		continue
            url = "im" + str(ind) + ".jpg"
            final_url = base_url_image + str(url)

            # For a given image now we have prob distribution
            # and words_present in the image. Now, we need to
            # make all ranked dictionary and make inference 
            # for each and everyword.
            # REST ALL THE SHIT GOES HERE.
            query_out = make_query(final_url)

            for topic in query_out:
                topic_words = [x for x in lda_model.show_topic(topic[0], topn=len(dict_natural.keys()))]
                for word in topic_words:
                    try:
                        p_topic = topic[1]
                        p_word = word[1]
                        p_final = p_topic*p_word
                        dict_natural[str(word[0])].append(p_final)
                    except:
                        pass
            # Choose the highest values for each of the words.
            topic_word_ranks_sum = []
	    topic_word_ranks_max = []
            for j in dict_natural.keys():
                try:
                    topic_word_ranks_sum.append((str(j),sum(dict_natural[str(j)])))
		    topic_word_ranks_max.append((str(j),max(dict_natural[str(j)])))
                except:
                    pass
            # Sort the dictionary and make final ranking prediction.
            final_ranking_sum = sorted(topic_word_ranks_sum, key=lambda x:x[1],reverse=True)
	    final_ranking_max = sorted(topic_word_ranks_max, key=lambda x:x[1],reverse=True)
            final_ranks_sum = []
	    final_ranks_max = []
            for i in final_ranking_sum:
                final_ranks_sum.append(i[0].lower())
            RESULTS_JSON_SUM[url] = final_ranks_sum
	    for i in final_ranking_max:
		final_ranks_max.append(i[0].lower())
	    RESULTS_JSON_MAX[url] = final_ranks_max
        # At the end make sure to make each word probs zero.
        # For next iteration.
        for i in dict_natural.keys():
            dict_natural[i] = []
    with open("/home/yash/Data/flickr/Results/result_train_500_sum.json", "w") as fp:
        json.dump(RESULTS_JSON_SUM, fp)
    with open("/home/yash/Data/flickr/Results/result_train_500_max.json", "w") as fp:
	json.dump(RESULTS_JSON_MAX, fp)
def make_query(image_url):
    global id2word
    global lda_model
    global num_topics
    # In make_query, get the output from the CNN.
    script_query = make_cnn_query(image_url)
    #script_query = os.system("python " + str(script_url) + " " + str(image_url))
    query_out = []
    for ind in range(0,num_topics):
        temp = (ind, script_query[ind])
        query_out.append(temp)
    top_vals = sorted(query_out, key=lambda x:x[1], reverse=True)
    return top_vals

# Call the main function.
main()
