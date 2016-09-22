import json
import gensim

f_result = open("/home/yash/Data/flickr/Results/result_30.json")
load_res = json.load(f_result)

f_gt = open("/home/yash/Data/flickr/data.json")
load_gt = json.load(f_gt)


counter_image = 0
instance_counter = 0
instance_suggested = 0
instance_matched = 0
for ind in load_gt.keys():
	if ((int(ind)%5 == 0) or (int(ind)%5==4)):
		if ((int(ind)==924) or (int(ind)==705)):
			continue
		counter_image += 1
		val = load_gt[ind]
		url = "im" + str(ind) + ".jpg"
		val_out = load_res[url][:5]
		instance_counter += len(val)
		instance_suggested += len(val_out)
		instance_matched += len(set(val).intersection(val_out))

print str(counter_image)
print str(instance_counter)
print str(instance_matched)
print str(instance_suggested)
