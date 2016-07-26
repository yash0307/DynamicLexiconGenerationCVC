############################################################################
########################## git@yash0307 ####################################
############################################################################

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json
import sys

sys.path.insert(0, '/home/yash/git_CVC/Dataset_APIs/COCO-Text')
import coco_text


# Train set = Train(MS_COCO) + Val(MS_COCO) - Val(COCO_Text)
# dict[image_id] = {"url" : image_file_name,
#                   "caption" : image_caption}
#
# image_caption : list(all_captions)
# image_file_name : String

data_dir_train = '/media/DADES/yash/MS-COCO'
data_type_train = 'train2014'

annFile_ms_train = '%s/annotations/captions_%s.json'%(data_dir_train,data_type_train)
coco_ms_train = COCO(annFile_ms_train)

data_dir_val = '/media/DADES/yash/MS-COCO'
data_type_val = 'val2014'

annFile_ms_val = '%s/annotations/captions_%s.json'%(data_dir_val,data_type_val)
coco_ms_val = COCO(annFile_ms_val)

coco_txt = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')

# Get all the three set of Ids and get the set of Ids corresponding to training images.
ids_coco_ms_train = coco_ms_train.getImgIds()
ids_coco_ms_val = coco_ms_val.getImgIds()
ids_coco_txt_val = coco_txt.getImgIds(imgIds=coco_txt.val)
ids_training = ((set(ids_coco_ms_train) | set(ids_coco_ms_val)) - set(ids_coco_txt_val))
print "MS-COCO train : " + str(len(ids_coco_ms_train))
print "MS-COCO val : " + str(len(ids_coco_ms_val))
print "COCO-Text val : " + str(len(ids_coco_txt_val))
print "Training Images : " + str(len(ids_training))
G_CAP = {}
counter = 0
for i in ids_training:
    counter += 1
    print str(counter)
    captions = []
    try:
        ann_ids_coco = coco_ms_train.getAnnIds(imgIds = i)
        ann_coco = coco_ms_train.loadAnns(ann_ids_coco)
        im = coco_ms_train.loadImgs(i)
    except:
        ann_ids_coco = coco_ms_val.getAnnIds(imgIds = i)
        ann_coco = coco_ms_val.loadAnns(ann_ids_coco)
        im = coco_ms_val.loadImgs(i)
    for j in ann_coco:
        captions.append(j['caption'])
    temp_dict = {}
    temp_dict['caption'] = captions
    temp_dict['url'] = im[0]['file_name']
    G_CAP[i] = temp_dict

with open('training_label.json','w') as fp:
    json.dump(G_CAP,fp)
