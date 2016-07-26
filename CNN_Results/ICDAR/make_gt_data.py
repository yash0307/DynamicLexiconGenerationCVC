### git @ yash0307 ###

# This script reads ground truth data
# for each image and store correspondin
# transcription into a json file.
# GT_DATA = {}
#   key="image_name"
#   value = [] //List of transcriptions.

import json

GT_DATA = {}
base_data_url = "/media/DADES/yash/ICDAR_per_image_lexicon/gt_train/gt_img_"
output_file_url = "/media/DADES/yash/ICDAR_per_image_lexicon/gt_train/GT_DATA.json"
for ind in range(1,1001):
    image_file_name = "img_" + str(ind)
    input_file_name = base_data_url + str(ind) + ".txt"
    input_file = open(input_file_name, "r")
    input_file_lines = input_file.readlines()
    words_present = []
    for line in input_file_lines :
        word = line.split(",")[8].split("\n")[0].lower()
        if word != "###":
            words_present.append(word)
        else:
            pass
    GT_DATA[image_file_name] = words_present
fp = open(output_file_url,"w")
json.dump(GT_DATA, fp)

