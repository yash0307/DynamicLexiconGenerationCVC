## Making Corpus from Dataset
Use script "make_dataset_corpus.py" located in folder "DynamicLexiconGenerationCVC/Dataset_APIs/MS-COCO/PythonAPI". Corpus is already made and stored in folder DynamicLexiconGenerationCVC/Dataset_corpus.
## Make Dictionary from Dataset
Use script "make_dataset_dictionary.py" located in folder "DynamicLexiconGenerationCVC/Dataset_Dictionary". Dictionary is already made and stored in same folder. "all_dict.json" contains word annotations from both traning and validaion sets of COCO-Text, whereas "train_dict.json" contains word annotations only from Traning set of COCO-Text. NOTE : For the paper we have not used "train_dict.json" anywhere.
## Convert the Dictionary to gensim required format
Use script "make_gensim_dictonary.py" located in folder "/DynamicLexiconGenerationCVC/Dataset_Dictionary". This script is needed to convert the normal json dictionary to gensim's class of dictionary, which is basically assigining an unique id to each word.
## Pre-preocess the corpus text for gensim required format
Use script "topic_modelling.py" located in folder "/DynamicLexiconGenerationCVC/Topic_modelling/Jad_sw_dict/Dataset_corpus". Learning LDA required each document to be represented in BoW representation, this script performs basic text processing (removing stop-words, tokenizing) and convert corpus into gensim-LDA required format. This is an example, for other dictionaries too the corresponding scripts are present in "DynamicLexiconGenerationCVC/Topic_modelling" folder.
## Frequency based Baseline evaluation
Use script "compute_frequency.py" located in folder "DynamicLexiconGenerationCVC/Baseline" to compute frequency for each dictionary word on wikipedia corpus. Jaderberg's dictionary and Dataset dictionary are already stored in sorted order in folder "/DynamicLexiconGenerationCVC/Baseline/Dictionary". Once these frequency-based sorted dictionary are made, use script "language_modelling.py" in folder "DynamicLexiconGenerationCVC/Baseline" to evaluate on COCO-Text validation set.
## Learn the LDA model
Use script "learn_LDA.py" located in folder "DynamicLexiconGenerationCVC/Topic_modelling/Jad_sw_dict/Dataset_corpus" to learn LDA model. This is an example, for other dictionaries too the corresponding scripts are present in "/DynamicLexiconGenerationCVC/Topic_modelling" folder.
## Generate Word-ranking results from LDA model
Use script "lda_10.py" located in folder "DynamicLexiconGenerationCVC/Topic_prob/Jad_sw_dict/Dataset_corpus" to generate word-ranking results using "Jaderberg's dictionary" and "10 topic models", similarly use "lda_30.py" in same folder to generate word-ranking results using "Jaderberg's dictionary" and "30 topic models". For other dictionaries, scripts are located in folder "/DynamicLexiconGenerationCVC/Topic_prob".
## Generate Labels for traning Deep CNN
Use script "topic_modelling.py" located in folder "/DynamicLexiconGenerationCVC/Inception_Labels_Gen/Jad_sw_dict" to generate labels needed to fine-tune the Deep CNN. This is an example, for other dictionaries too the corresponding scripts are present in "DynamicLexiconGenerationCVC/Inception_Labels_Gen" folder.
## Fine-tune Deep CNN
Use script "retrain.py" located in folder "/DynamicLexiconGenerationCVC/CNN_finetuning" to finetune the InceptionNet. The models used to present results in paper are located in folder "/DynamicLexiconGenerationCVC/CNN_finetuning/Jad_sw_dict" and "/DynamicLexiconGenerationCVC/CNN_finetuning/Dataset_dict" as "output_graph_all.pb" for Corpus(1) of paper and "output_graph_train.pb" for Corpus(2) of paper.
## Generate Word-ranking results from Deep CNN
Use script "cnnDatEval.py" located in folder "/DynamicLexiconGenerationCVC/CNN_Results/Jad_sw_dict" to generate word-ranking results from Deep CNN for "Jaderberg's Dictionary". Similarly for "Dataset's Dictionary" use script "cnnDatEval.py" in folder "/DynamicLexiconGenerationCVC/CNN_Results/Dataset_dict". The generated results are already stored in same folders as "results_all.txt"(using Corpus(1)) and "results_train.txt"(using Corpus(2)).
## Generate per-image lexicon

