### git @ yash0307 ###

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json
import sys
sys.path.insert(0, '/home/yash/git_CVC/Dataset_APIs/COCO-Text')
import coco_text
import cross_api_modular

data_dir_c = '/media/DADES/yash/MS-COCO'
data_type_c = 'train2014'

coco_txt = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')
annFile='%s/annotations/captions_%s.json'%(data_dir_c,data_type_c)
coco_ms = COCO(annFile)
crossAPI = cross_api_modular(coco_ms, coco_txt, "val", "./")
