##### git @ yash0307 #####
##### bit @ yash0307 #####

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json

dataDir='/home/yash/Data/MS-COCO/Annotations'
dataType='val2014'
annFile_instances='%s/annotations/instances_%s.json'%(dataDir,dataType)
annFile_captions ='%s/annotations/captions_%s.json'%(dataDir,dataType)
coco_instances=COCO(annFile_instances)
coco_captions=COCO(annFile_captions)

cats = coco_instances.loadCats(coco_instances.getCatIds())
nms=[str(cat['name']) for cat in cats]
catIds_all = coco_instances.getCatIds(catNms=nms)
imgIds = coco_instances.getImgIds()
print "Number of images : " + str(len(imgIds))

CAT_IMAGE = {}
counter = 0
for catname in nms:
	catId = coco_instances.getCatIds(catNms = [catname])
	catImgIds = coco_instances.getImgIds(catIds=catId)
	CAT_IMAGE[catname] = catImgIds

DATA = {}

for ind in imgIds:
	counter += 1
	print "Total 83K" + str(counter)
	dict_index = str(ind)
	val = {}
	ann_ids_coco = coco_captions.getAnnIds(imgIds = ind)
	ann_coco = coco_captions.loadAnns(ann_ids_coco)
	caption = []
	for j in ann_coco:
	        try:
        		if j['caption'] != '':
        			caption.append(str(j['caption']))
   		except KeyError:
        		pass
	annotation = []
	for j in CAT_IMAGE.keys():
		if ind in CAT_IMAGE[j]:
			annotation.append(str(j))
	val['captions'] = caption
	val['annotation'] = annotation
	DATA[dict_index] = val
fp = open('/home/yash/Data/MS-COCO/data_val.json','w')
json.dump(DATA,fp)
