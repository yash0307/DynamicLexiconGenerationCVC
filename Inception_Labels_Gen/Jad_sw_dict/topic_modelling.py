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
    num_topics = 30
    zero_constant = 0
    TARGET_LABEL = {}
    ##########################################################################################
    ########################## Pre-processing documents ######################################
    ##########################################################################################
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    ##########################################################################################
    ############################## Training Models ###########################################
    ##########################################################################################
    id2word = gensim.corpora.Dictionary.load_from_text('/media/DADES/yash/Wikipedia/jad_sw_gensim_dict.txt')
    lda_model = gensim.models.ldamodel.LdaModel.load('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Jad_sw_dict/lda_model_train_30.lda', mmap='r')
    ###########################################################################################
    ############################# Read and Parse Input File ###################################
    ###########################################################################################
    with open('/media/DADES/yash/newInceptionLabels/im_cap_val.json') as data_file:
        data = json.load(data_file)
    
    for ind in data.keys():
        counter = counter + 1
        value = data[ind]
        url = value['url']
        captions = value['caption']
        temp_doc = ''
        for i in captions:
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
        TARGET_LABEL[url] = labels
        print "TOTAL = 100K something :  " + str(counter)
    with open('/media/DADES/yash/newInceptionLabels/Jad_sw_dict/validation_label.json','w') as fp:
        json.dump(TARGET_LABEL, fp)
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
