### git @ yash0307 ###

# Get all the image_file name and corresponding ID
# For validation images of coco_text dataset.

# Once We have all the file name and IDs.
# Take these out of train images of MS-COCO.

import sys
sys.path.insert(0, '/home/yash/git_CVC/Dataset_APIs/COCO-Text')
import coco_text
import json
ct = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')
imgs = ct.getImgIds(imgIds=ct.val)
id_url_dict = {}
counter = 0
for i in imgs:
    counter +=1
    file_name = ct.loadImgs(i)[0]['file_name']
    id_url_dict[str(i)] = file_name
print str(counter)
fp = open('id_url.json','w')
json.dump(id_url_dict,fp)
