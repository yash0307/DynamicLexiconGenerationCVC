import sys
sys.path.insert(0, '/home/yash/git_CVC/Dataset_APIs/COCO-Text')
import coco_text

coco_txt = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')
im_ids_txt = coco_txt.getImgIds(imgIds = coco_txt.val)
str_ids_txt = [str(i) for i in im_ids_txt]
while(1):
    input_id = raw_input('Enter Image ID\n')
    if str(input_id) in str_ids_txt:
        print "Given ID is present in Val set of COCO-Text"
    else:
        print "Given ID is not present in Val set of COCO-Text"
