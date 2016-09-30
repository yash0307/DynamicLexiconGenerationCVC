from __future__ import division

### git @ yash0307 ###
import json
import gensim
### labels_train_baseline = {}
### labels_val_baseline = {}
### Key = Image_name
### value = [38*1]
all_annotations = ["animals", "baby_r1", "baby", "bird_r1", "bird", "car_r1", "car", "clouds_r1", "clouds", "dog_r1", "dog", "female_r1", "female", "flower_r1", "flower", "food", "indoor", "lake", "male_r1", "male", "night_r1", "night", "people_r1", "people", "plant_life", "portrait_r1", "portrait", "river_r1", "river", "sea_r1", "sea", "sky", "structures", "sunset", "transport", "tree_r1", "tree", "water"]

fp = open("/home/yash/Data/flickr/data.json")
data = json.load(fp)
counter = 0
TRAIN_LABEL = {}
VAL_LABEL = {}
for ind in data.keys():
	counter += 1
	print "Total 25K : " + str(counter)
	url = "im" + str(ind) + ".jpg"
	value = data[ind]
	gen_labels = [0] * len(all_annotations)
	num_of_labels = len(value)
	for j in value:
		gen_labels[all_annotations.index(j)] = (1/num_of_labels)
	if int(ind)%2==1:
		TRAIN_LABEL[url] = gen_labels
	elif int(ind)%2==0:
		VAL_LABEL[url] = gen_labels

fp_train = open("./train.json","w")
json.dump(TRAIN_LABEL,fp_train)
fp_val = open("./val.json", "w")
json.dump(VAL_LABEL, fp_val)
print str(len(TRAIN_LABEL.keys()))
print str(len(VAL_LABEL.keys()))
		
