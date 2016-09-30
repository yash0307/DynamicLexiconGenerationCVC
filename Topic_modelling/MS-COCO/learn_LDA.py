### git @ yash0307 ###
import gensim
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')
mm = gensim.corpora.MmCorpus('/home/yash/Data/flickr/corpus_train.mm')

lda_model_400 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 400, workers=3)
lda_model_400.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_400.lda')

lda_model_200 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 200, workers=3)
lda_model_200.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_200.lda')

lda_model_100 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 100, workers=3)
lda_model_100.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_100.lda')

lda_model_2500 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 2500, workers=3)
lda_model_2500.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_2500.lda')

lda_model_1500 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 1500, workers=3)
lda_model_1500.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_1500.lda')

lda_model_1000 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 1000, workers=3)
lda_model_1000.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_1000.lda')

lda_model_1200 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 1200, workers=3)
lda_model_1200.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_1200.lda')

lda_model_800 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 800, workers=3)
lda_model_800.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_800.lda')

lda_model_1300 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 1300, workers=3)
lda_model_1300.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_1300.lda')

lda_model_1100 = gensim.models.ldamulticore.LdaMulticore(corpus = mm, id2word=id2word ,num_topics = 1100, workers=3)
lda_model_1100.save('/home/yash/DynamicLexiconGenerationCVC/flickr_LDA_MODELS/train_corpus/lda_model_train_1100.lda')
