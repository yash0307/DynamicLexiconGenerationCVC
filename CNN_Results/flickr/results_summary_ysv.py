from __future__ import division

import gensim
import json

f_result = open("/home/yash/Data/flickr/Results/result_train_500_max.json")
data_result = json.load(f_result)

f_gt = open("/home/yash/Data/flickr/data.json")
data_gt = json.load(f_gt)

counter_images = 0

id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')

iterator = id2word.iteritems()
keys = id2word.keys()
dict_labels_result = {}
dict_labels_gt = {}

for i in range(0,len(keys)):
	temp_item = iterator.next()
	try:
		dict_labels_result[str(temp_item[1]).lower()] = []
		dict_labels_gt[str(temp_item[1]).lower()] = []
	except:
		pass

for ind_data in data_result.keys():
	val = data_result[ind_data][:5]
	for j in val:
		dict_labels_result[j].append(ind_data)

for ind_data in data_gt.keys():
	if ((int(ind_data)%5==4) or (int(ind_data)%5==0)):
		val = data_gt[ind_data]
		if ((int(ind_data)!= 924) and (int(ind_data) != 705)):
			for j in val:
				temp_ind = "im" + str(ind_data) + ".jpg"
				dict_labels_gt[j].append(temp_ind)

sum_results = 0
for i in dict_labels_result.keys():
	print (str(i) + " : " + str(len(dict_labels_result[i])))
	sum_results += len(dict_labels_result[i])
print ("sum : " + str(sum_results))

print ("\n\n")
sum_gt = 0
for i in dict_labels_gt.keys():
	print (str(i) + " : " + str(len(dict_labels_gt[i])))
	sum_gt += len(dict_labels_gt[i])
print ("sum_gt : " + str(sum_gt))
print ("\n\n")
average_precision = 0
average_recall = 0
average_counter = 0
for i in dict_labels_result.keys():
	average_counter += 1
	val_result = dict_labels_result[i]
	val_gt = dict_labels_gt[i]
	m3 = len(set(val_gt).intersection(set(val_result)))
	m1 = len(val_gt)
	m2 = len(val_result)
	average_recall += (m3/m1)
	try:
		average_precision += (m3/m2)
	except:
		pass
	print (str(i) +" : "+str(m3))

MAP = (average_precision/average_counter)
MAR = (average_recall/average_counter)
f_score = 2*((MAP*MAR)/(MAP + MAR))
print ("Average Precision" +  " : " + str(MAP))
print ("Average Recall" + " : " + str(MAR))
print ("F-score : " + str(f_score))
