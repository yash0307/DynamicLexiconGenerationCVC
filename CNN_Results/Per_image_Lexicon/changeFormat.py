### git @ yash ###
# Read each json file
# Convert this to txt

from os import walk
import json
f = []
base_url = "./Ranked_Dictionaries_COCO"
for (dirpath, dirnames, filenames) in walk(base_url):
	f.extend(filenames)
	break

target_url = "./Ranked_Dictionaries_COCO_txt"
counter = 0
for file_name in f:
	counter += 1
	print str(counter)
	file_url = base_url + "/" + str(file_name)
	out_file_name = str(str(file_name).split(".")[0]) + ".jpg.txt"
	out_file_url = target_url + "/" + out_file_name
	read_file = open(file_url,"r")
	load_data = json.load(read_file)
	out_file = open(out_file_url,"w")
	for word in load_data:
		out_file.write(word + "\n")
	out_file.close()
