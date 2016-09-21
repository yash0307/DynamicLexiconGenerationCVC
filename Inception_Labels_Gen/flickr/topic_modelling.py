###########################################################################################
############################ git@yash0307 #################################################
###########################################################################################
import logging
import sys
import pprint
import gensim
import bz2
import os
import json
############################################################################################
############################# Global Variables #############################################
############################################################################################
global analysis_type
global wiki_dump_path
global wiki_corpus
global id2word
global mm
global lda_model
global lsa_model
global num_tpics
global num_words
global counter
#############################################################################################
############################ Main function ##################################################
#############################################################################################
def main():
    global analysis_type
    global wiki_dump_path
    global wiki_corpus
    global id2word
    global mm
    global lda_model
    global lsa_model
    global num_topics
    global num_words
    global counter

    counter = 0
    analysis_type = 'lda'
    num_topics = 10
    zero_constant = 0
    TARGET_LABEL_TRAIN = {}
    TARGET_LABEL_VAL = {}
    ##########################################################################################
    ########################## Pre-processing documents ######################################
    ##########################################################################################
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    ##########################################################################################
    ############################## Training Models ###########################################
    ##########################################################################################
    id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')
    lda_model_url = "/home/yash/Data/flickr/LDA_MODELS/lda_model_train_" + str(num_topics) + ".lda"
    lda_model = gensim.models.ldamodel.LdaModel.load(lda_model_url, mmap='r')
    ###########################################################################################
    ############################# Read and Parse Input File ###################################
    ###########################################################################################
    with open('/home/yash/Data/flickr/data.json') as data_file:
        data = json.load(data_file)
    
    for ind in data.keys():
        counter = counter + 1
        value = data[ind]
        url = "im" + str(ind) + ".jpg"
        temp_doc = ''
        for i in value:
            temp_doc = temp_doc + " " + str(i)

        # NOTE : Following is the structure for 
        # the target labels.
        # key = url
        # value = list(p1,p2,...p400)
        query_out = make_query(temp_doc)
        topic_prob = {}
        for instance in query_out:
            topic_prob[instance[0]] = instance[1]
        
        labels = []
        for topic_num in range(0,num_topics):
            if topic_num in topic_prob.keys():
                labels.append(topic_prob[topic_num])
            else:
                labels.append(zero_constant)
        if ((int(ind)%5 == 1) (int(ind)%5==2) and (int(ind)%5==3)):
            TARGET_LABEL_TRAIN[url] = labels
        elif((int(ind)%5 == 0) and (int(ind)%5 == 4))
            TARGET_LABEL_VAL[url] = labels
        print "TOTAL = 25K something :  " + str(counter)
    train_label_url = "/home/yash/Data/flickr/Inception_labels/label_train_" + str(num_topics) + ".json"
    with open(train_label_url,'w') as fp_train:
        json.dump(TARGET_LABEL_TRAIN, fp_train)
    val_label_url = '/home/yash/Data/flickr/Inception_labels/label_val_' + str(num_topics) + ".json"
    with open(val_label_url, 'w') as fp_val:
        json.dump(TARGET_LABEL_VAL, fp_val)

def make_query(query):

    global analysis_type
    global wiki_dump_path
    global wiki_corpus
    global id2word
    global mm
    global lda_model
    global lsa_model
    global num_topics
    global num_words

    ###########################################################################################
    ############################# Making query ################################################
    ###########################################################################################
    vec_bow = id2word.doc2bow(query.lower().split())    
    if (analysis_type.lower() == "lda") :
        query_out = lda_model[vec_bow]
        return query_out
    elif (analysis_type.lower() == "lsa") :
        query_out = lsa_model[vec_bow]
        return query_out
###############################################################################################
main()
