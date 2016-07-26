from __future__ import division
### git @ yash0307 ###

import ast
import operator

line_counter = 0
instance_counter = 0


log_count_1 = 0
log_count_10 = 0
log_count_100 = 0
log_count_1000 = 0
log_count_10000 = 0
log_count_100000 = 0

with open('../Dataset_dict/results_train_1000.txt') as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    word_list = []
    total_words = 1
    for i in content :
        if (line_counter == 0):
            line_counter += 1
            word_list = ast.literal_eval(i)
        elif (line_counter == 1):
            line_counter += 1
            total_words = int(float(i.split(":")[1]))
        elif (line_counter == 2):
            line_counter = 0
            for j in word_list:
                instance_counter += 1
                try:
                    if j.split(":")[1] != ' NA':
                        try:
                            word_rank = int(float(j.split(":")[1]))
                            rank_percent = float(word_rank/total_words)*100
                            if word_rank < 1:
                                log_count_1 += 1
                            if word_rank < 10:
                                log_count_10 += 1
                            if word_rank < 100:
                                log_count_100 += 1
                            if word_rank < 1000:
                                log_count_1000 += 1
                            if word_rank < 10000:
                                log_count_10000 += 1
                            if word_rank < 100000:
                                log_count_100000 += 1
                        except:
                            pass
                except IndexError:
                    pass
    instance_counter = log_count_100000
    print "LOG-SCALE RESULTS\n\n"
    print str((log_count_1/instance_counter)*100) + ',',
    print str((log_count_10/instance_counter)*100) + ',',
    print str((log_count_100/instance_counter)*100) + ',',
    print str((log_count_1000/instance_counter)*100) + ',',
    print str((log_count_10000/instance_counter)*100) + ',',
    print str((log_count_100000/instance_counter)*100) + ','
    print str(log_count_100000)
    print "Not Ranked at all : " + str(((instance_counter - log_count_100000)/instance_counter)*100)
    print "Number of Instances : " + str(instance_counter)
