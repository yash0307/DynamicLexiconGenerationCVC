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


# Valitaion set = validation set of only coco_text dataset.
# dict[image_id] = {"url" : image_file_name,
#                   "caption" : image_caption}
#
# image_caption : list(all_captions)
# image_file_name : String

data_dir = '/media/DADES/yash/MS-COCO'
data_type = 'train2014'

annFile_ms = '%s/annotations/captions_%s.json'%(data_dir,data_type)
coco_ms = COCO(annFile_ms)

coco_txt = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')
G_CAP = {}
im_ids_val = coco_txt.getImgIds(imgIds=coco_txt.val)
counter = 0
for i in im_ids_val:
    counter += 1
    print str(counter)
    captions = []
    ann_ids_coco = coco_ms.getAnnIds(imgIds = i)
    ann_coco = coco_ms.loadAnns(ann_ids_coco)
    for j in ann_coco:
        captions.append(j['caption'])
    im = coco_ms.loadImgs(i)
    temp_dict = {}
    temp_dict['caption'] = captions
    temp_dict['url'] = im[0]['file_name']
    G_CAP[i] = temp_dict

with open('validation_label.json','w') as fp:
    json.dump(G_CAP,fp)
