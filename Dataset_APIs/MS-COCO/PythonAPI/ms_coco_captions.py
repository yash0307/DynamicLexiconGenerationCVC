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

# NOTE : COCO-Text APIs are not required here.
# This script generates a dictionary containing
# all the captions for training and validation
# images. Following is the structure used :
#
# dict[image_id] = {"url" : image_file_name,
#                   "caption" : image_caption}
#
# image_caption : list(all_captions)
# image_file_name : String

data_dir = '/media/DADES/yash/MS-COCO'
data_type = 'train2014'
#data_type = 'val2014'

annFile='%s/annotations/captions_%s.json'%(data_dir,data_type)
coco=COCO(annFile)
G_CAP = {}
im_cap_ids = coco.getImgIds()
for i in im_cap_ids:
    captions = []
    ann_coco_id = coco.getAnnIds(imgIds = i)
    ann_coco = coco.loadAnns(ann_coco_id)
    for j in ann_coco:
        captions.append(j['caption'])
    im = coco.loadImgs(i)
    temp_dict = {}
    temp_dict['caption'] = captions
    temp_dict['url'] = im[0]['file_name']
    G_CAP[i] = temp_dict

with open('im_cap.json','w') as fp:
    json.dump(G_CAP,fp)
