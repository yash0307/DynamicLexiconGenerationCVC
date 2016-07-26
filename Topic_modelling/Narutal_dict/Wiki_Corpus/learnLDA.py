### git @ yash0307 ###
import gensim
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('/media/DADES/yash/Wiki/wiki_en_wordids.txt')
mm = gensim.corpora.MmCorpus('/media/DADES/yash/Wiki/wiki_en_bow.mm')

#lda_model_30 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 30, workers=3)
#lda_model_30.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/lda_model_30.lda')

#lda_model_50 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 50, workers=3)
#lda_model_50.save('/media/DADES/yash/topicModelDataset/Wiki_corpus/lda_model_50.lda')

#lda_model_20 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 20, workers=3)
#lda_model_20.save('/media/DADES/yash/topicModelDataset/Wiki_corpus/lda_model_20.lda')

#lda_model_15 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 15, workers=3)
#lda_model_15.save('/media/DADES/yash/topicModelDataset/Wiki_corpus/lda_model_15.lda')

#lda_model_100 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 100, workers=3)
#lda_model_100.save('/media/DADES/yash/topicModelDataset/Wiki_corpus/lda_model_100.lda')

lda_model_70 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 70, workers=2)
lda_model_70.save('/media/DADES/yash/topicModelDataset/Wiki_corpus/lda_model_70.lda')

lda_model_40 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 40, workers=2)
lda_model_40.save('/media/DADES/yash/topicModelDataset/Wiki_corpus/lda_model_40.lda')
