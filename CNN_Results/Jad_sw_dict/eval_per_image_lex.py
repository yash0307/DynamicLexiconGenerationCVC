### git @ yash0307 ###
import json
import sys
import os
sys.path.insert(0, '/home/yash/git_CVC/Dataset_APIs/COCO-Text')
import coco_text

base_url = "/media/DADES/yash/per_image_lexicon"
targer_url = "."

coco_txt = coco_text.COCO_Text('/media/DADES/yash/COCO-Text/COCO_Text.json')
im_ids_txt = coco_txt.getImgIds(imgIds=coco_txt.val)

eval_file = open('/media/DADES/yash/newInceptionLabels/im_cap_val.json','r')
eval_json = json.load(eval_file)

counter_image = 0
counter_word_instance = 0
f = open("fail_results.txt","w")
for ind in im_ids_txt:
    counter_image += 1
    print "Total 20K : " + str(counter_image)
    words_present = []
    value = eval_json[str(ind)]
    ann_ids_txt = coco_txt.getAnnIds(imgIds = ind)
    ann_txt = coco_txt.loadAnns(ann_ids_txt)
    for j in ann_txt:
        try:
            if j['utf8_string'] != '':
                counter_word_instance += 1
                words_present.append(j['utf8_string'])
        except KeyError:
            pass
    if not words_present:
        pass
    else:
        # Get Image's lexicon.
        img = coco_txt.loadImgs(ind)[0]
        image_file_name = img['file_name']
        input_file_url = base_url + "/" + image_file_name + ".txt"
        final_ranks = []
        fp = open(input_file_url, "r")
        lines = fp.readlines()
        for i in lines:
            final_ranks.append(str(i).split("\n")[0])
        text_ranks = []
        for text in words_present:
            try:
                text_ranks.append(str(text) + " : " + str(final_ranks.index(str(text.lower()))))
            except ValueError:
                try:
                    text_ranks.append(str(text) + " : NA")
                except:
                    text_ranks.append("Unicode error")
        f.write(str(text_ranks) + "\n")
        f.write("Total words : " + str(len(final_ranks)) + "\n")
        f.write(str(image_file_name) + "\n")
        f.write("---------------------------------------\n")
        print str(text_ranks)
        print "Total words : " + str(len(final_ranks))
        print str(image_file_name)
        print "---------------------------------------"
        fp.close()

print "counter_word_instances : " + str(counter_word_instance)
f.close()
