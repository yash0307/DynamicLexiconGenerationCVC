## git@yash0307 ###

# Compare ids of all the images in the MS-COCO
# and COCO-Text datasets and make sure that
# they completely overlap.

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json
import sys
sys.path.insert(0, '/home/yash/git_CVC/Dataset_APIs/COCO-Text')
import coco_text

data_dir_ms = '/media/DADES/yash/MS-COCO'
data_type_ms = 'val2014'

#data_dir_txt = '/media/DADES/yash/COCO-Text'
#data_type_txt = 'train2014'

coco_txt = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')

annFile='%s/annotations/captions_%s.json'%(data_dir_ms,data_type_ms)
coco_ms = COCO(annFile)

im_ids_txt = coco_txt.getImgIds(imgIds = coco_txt.train)
im_ids_ms = coco_ms.getImgIds()

str_ids_txt = [str(i) for i in im_ids_txt]
str_ids_ms = [str(i) for i in im_ids_ms]

common_ids = set(str_ids_txt) & set(str_ids_ms)
print "COCO-Text ids (size): " + str(len(im_ids_txt))
print "MS-COCO ids (size): " + str(len(im_ids_ms))
print "Common ids in two sets (size): " + str(len(common_ids))
