### git @ yash0307 ###
import gensim
import json
import sys
import logging
sys.path.insert(0, '/home/yash/coco-text')
import coco_evaluation
import coco_text

coco_text = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')

im_ids = coco_text.getImgIds(imgIds=coco_text.val)
ann_ids = coco_text.getAnnIds(imgIds=coco_text.val)

result_base_url = '/media/DADES/yash/TextProposals-results-COCO-Text_val/res/'

our_results = coco_text.loadRes('./legibleEnglish/our_results.json')
our_detections = coco_evaluation.getDetections(coco_text, our_results, detection_threshold = 0.5)
our_endToEnd_results = coco_evaluation.evaluateEndToEnd(coco_text, our_results, detection_threshold = 0.5)
coco_evaluation.printDetailedResults(coco_text, our_detections, our_endToEnd_results, 'BASELINE : Text Proposal + Word-recog.')
#(x1,y1)----------(x2,y2)
#|                  |
#|                  |
#|                  |
#|                  |
#|                  |
#|                  |
#(x3,y3)----------(x4,y4)
