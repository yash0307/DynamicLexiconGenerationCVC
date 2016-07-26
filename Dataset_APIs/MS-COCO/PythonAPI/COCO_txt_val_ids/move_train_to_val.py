### git @ yash0307 ###

import json
import shutil

file_path = '/media/DADES/yash/MS-COCO/allImages/train2014/'
target_path = '/media/DADES/yash/MS-COCO/inceptionImages/validation/'
fp = open('id_url.json','r')
counter = 0
temp_dict = json.load(fp)

for ind in temp_dict.keys():
    counter += 1
    print "Counter : " + str(counter)
    file_name = temp_dict[ind]
    initial_file = file_path + file_name
    final_file = target_path + file_name
    shutil.move(initial_file, final_file)    
