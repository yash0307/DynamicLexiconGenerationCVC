### git @ yash0307 ###
import gensim
import json
import sys
import logging
sys.path.insert(0, '/home/yash/coco-text')
import coco_evaluation
import coco_text

coco_text = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')

im_ids = coco_text.getImgIds(imgIds=coco_text.val, catIds=[('legibility','legible'),('language','english')])

result_base_url = '/media/DADES/yash/TextProposals-results-COCO-Text_val/res/'

result_list = []

counter = 0
for ind in im_ids:
    counter += 1
    print ("TOTAL 20k : " + str(counter))
    img = coco_text.loadImgs(ind)[0]
    img_file_name = img['file_name'] + '.txt'
    final_url = result_base_url + img_file_name
    fp = open(final_url,'r')
    content = [line.split(',') for line in fp.readlines()]
    for i in content:
        x1 = int(i[0])
        y1 = int(i[1])
        x2 = int(i[2])
        y2 = int(i[3])
        x3 = int(i[4])
        y3 = int(i[5])
        x4 = int(i[6])
        y4 = int(i[7])
        width = x2 - x1
        height = y3 - y1
        word = str(i[8]).split("\n")[0].lower()
        temp_dict = {}
        temp_dict["image_id"] = int(ind)
        temp_dict["bbox"] = [x1, y1, width, height]
        temp_dict["utf8_string"] = str(word)
        result_list.append(temp_dict)

fp_out = open("./legibleMachine/our_results.json","w")
json.dump(result_list, fp_out)
#our_endToEnd_results = coco_evaluation.evaluateEndToEnd(coco_text, result_list, detection_threshold = 0.5)
#coco_evaluation.printDetailedResults(coco_text,our_detections,our_endToEnd_results,'BASELINE : Text Proposal + Word-recog.')
#(x1,y1)----------(x2,y2)
#|                  |
#|                  |
#|                  |
#|                  |
#|                  |
#|                  |
#(x3,y3)----------(x4,y4)
