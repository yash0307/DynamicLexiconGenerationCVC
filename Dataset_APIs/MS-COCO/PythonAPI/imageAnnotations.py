##### git @ yash0307 #####
##### bit @ yash0307 #####

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json

dataDir='/home/yash/Data/MS-COCO/Annotations'
dataType='train2014'
annFile_instances='%s/annotations/instances_%s.json'%(dataDir,dataType)
annFile_captions ='%s/annotations/captions_%s.json'%(dataDir,dataType)

cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print str(nms)
catIds = coco.getCatIds()
imgIds = coco.getImgIds(catIds=catIds )
print "Number of images : " + str(imgIds)