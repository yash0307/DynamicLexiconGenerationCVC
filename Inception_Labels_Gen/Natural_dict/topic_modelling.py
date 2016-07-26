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
    num_topics = 10
    num_words = 30
    
    analysis_type = 'lda'

    num_topics = 400
    zero_constant = 0
    TARGET_LABEL = {}
    ##########################################################################################
    ########################## Pre-processing documents ######################################
    ##########################################################################################

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    ## Making corpus from wikipedia dump.
    if ((os.path.isfile("/media/DADES/yash/Wikipedia/jad_gensim_dict.txt")) and (os.path.isfile("/media/DADES/yash/Wikipedia/wiki_corpus.mm"))):
	    pass
    else :
	    wiki_dump_path = "/media/DADES/yash/Wiki/enWiki-pages-articles.xml.bz2"
	    wiki_corpus = gensim.corpora.WikiCorpus(wiki_dump_path)
	    wiki_corpus.save("/media/DADES/yash/Wiki/wiki_dict.dict")

    # Dictionary, tfidf location at 'media/DADES/yash'
    id2word = gensim.corpora.Dictionary.load_from_text('/media/DADES/yash/Wiki/wiki_en_wordids.txt')
    mm = gensim.corpora.MmCorpus('/media/DADES/yash/Wiki/wiki_en_bow.mm')

    ##########################################################################################
    ############################## Training Models ###########################################
    ##########################################################################################

    if ((analysis_type.lower() == "lda") and not (os.path.isfile("/media/DADES/yash/Wikipedia/jad_lda_model.lda"))):
	    lda_model = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 400, workers=2)
	    lda_model.save('/media/DADES/yash/Wikipedia/jad_lda_model.lda')
	    lda_model.print_topics(10)
    elif (analysis_type.lower() == "lda") :
	    lda_model = gensim.models.ldamodel.LdaModel.load('/media/DADES/yash/Wiki/lda_model.lda', mmap='r')

    if ((analysis_type.lower() == "lsa") and not (os.path.isfile("/media/DADES/yash/Wiki/lsa_model.lsi"))):
	    lsa_model = gensim.models.lsimodel.LsiModel(corpus = mm, id2word=id2word ,num_topics = 400)
	    lsa_model.save('/media/DADES/yash/Wiki/lsa_model.lsi')
	    lsa_model.print_topics(10)
    elif (analysis_type.lower() == "lsa") :
	    lsa_model = gensim.models.LsiModel.load('/media/DADES/yash/Wiki/lsa_model.lsi')

    ###########################################################################################
    ############################# Read and Parse Input File ###################################
    ###########################################################################################
    with open('./im_cap_train.json') as data_file:
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
        print "TOTAL = 80K something :  " + str(counter)
    with open('./training_label.json','w') as fp:
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
