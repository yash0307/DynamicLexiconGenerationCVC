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
    f = open("results.txt", "w")
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
    ##########################################################################################
    ########################## Pre-processing documents ######################################
    ##########################################################################################

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    ## Making corpus from wikipedia dump.
    if ((os.path.isfile("/media/DADES/yash/Wiki/wiki_en_wordids.txt")) and (os.path.isfile("/media/DADES/yash/Wiki/wiki_en_bow.mm"))):
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

    if ((analysis_type.lower() == "lda") and not (os.path.isfile("/media/DADES/yash/Wiki/lda_model.lda"))):
	    lda_model = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 400, workers=2)
	    lda_model.save('/media/DADES/yash/Wiki/lda_model.lda')
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
    with open('./Data_Caption_Text/legible_machine.json') as data_file:
        data = json.load(data_file)
    
    for ind in data.keys():
        counter = counter + 1
        value = data[ind]
        texts = value['text']
        captions = value['captions']
        temp_doc = ''
        for i in captions:
            temp_doc = temp_doc + " " + str(i)
        query_out = make_query(temp_doc)
        topic_word_ranks = []
        final_word_prob_list = []
        for topic in query_out[0:num_topics]:
            topic_words = [x for x in lda_model.show_topic(topic[0], topn=10000)]
            for j in topic_words:
                p_topic = topic[1]
                p_word = j[1]
                p_final = p_topic*p_word
                final_word_prob_list.append((j[0].lower(), p_final)) 
        topic_word_ranks = sorted(final_word_prob_list, key=lambda x:x[1],reverse=True)

        final_ranks = []
        for i in topic_word_ranks:
            final_ranks.append(i[0])
        text_ranks = []
        for text in texts:
            try:
                text_ranks.append(str(text) + " : " + str(final_ranks.index(str(text.lower()))))
            except ValueError:
                try:
                    text_ranks.append(str(text) + " : NA")
                except:
                    text_ranks.append("Unicode error")

        f.write(str(text_ranks) + "\n")
        f.write("Total words : " + str(len(final_ranks)) + "\n")
        f.write("---------------------------------------\n")
        print str(counter)
        #print str(text_ranks)
        #print "Total words : " + str(len(final_ranks)) 
        #print "---------------------------------------"
    f.close()
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
        query_out = lda_model.get_document_topics(vec_bow, minimum_probability=None)
        s=sorted(query_out,key=lambda x:x[1],reverse=True)
        return s
        #for topic,_ in s[0:num_topics]:
        #    print topic, [x[0] for x in lda_model.show_topic(topic,topn=num_words)]
        #    print "\n"
    elif (analysis_type.lower() == "lsa") :
        query_out = lsa_model[vec_bow]
        s=sorted(query_out,key=lambda x:x[1],reverse=True)
        return s
	    #for topic,_ in s[0:num_topics]:
		#    print topic, [x[0] for x in lsa_model.show_topic(topic,topn=num_words)]
		#    print "\n"
###############################################################################################
main()
