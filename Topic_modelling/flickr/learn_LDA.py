### git @ yash0307 ###
import gensim
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('/media/DADES/yash/Wikipedia/jad_gensim_dict.txt')
mm = gensim.corpora.MmCorpus('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Jad_dict/corpus.mm')

lda_model_400 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 400, workers=3)
lda_model_400.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_400.lda')

lda_model_200 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 200, workers=3)
lda_model_200.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_200.lda')

lda_model_100 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 100, workers=3)
lda_model_100.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_100.lda')

lda_model_50 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 50, workers=3)
lda_model_50.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_50.lda')

lda_model_500 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 500, workers=3)
lda_model_500.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_500.lda')

lda_model_1000 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 1000, workers=3)
lda_model_1000.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_1000.lda')

#lda_model_2000 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 2000, workers=3)
#lda_model_2000.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_2000.lda')

lda_model_80 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 80, workers=3)
lda_model_80.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_80.lda')

lda_model_30 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 30, workers=3)
lda_model_30.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_30.lda')

lda_model_10 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 10, workers=3)
lda_model_10.save('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Natural_dict/lda_model_train_10.lda')
