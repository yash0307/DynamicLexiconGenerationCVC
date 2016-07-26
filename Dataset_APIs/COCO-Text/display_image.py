import coco_text
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

ct = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')
imgs = ct.getImgIds(imgIds=ct.val)
anns = ct.getAnnIds(imgIds=ct.val)
dataDir = '/media/DADES/yash/MS-COCO/inceptionImages'
dataType='validation'
img = ct.loadImgs(460168)[0]
I = io.imread('%s/%s/%s'%(dataDir,dataType,img['file_name']))
print '/images/%s/%s'%(dataType,img['file_name'])
plt.figure()
plt.show(I)
#annIds = ct.getAnnIds(imgIds=img['id'])
#anns = ct.loadAnns(annIds)
#ct.showAnns(anns)
