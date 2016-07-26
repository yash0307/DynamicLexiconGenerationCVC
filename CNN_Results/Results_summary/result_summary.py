from __future__ import division
### git @ yash0307 ###

import ast
import operator

count_na = 0
count_p_01 = 0
count_p_1 = 0
count_p_5 = 0
count_1 = 0
count_5 = 0
count_10 = 0
count_15 = 0
count_20 = 0
count_25 = 0
count_30 = 0
count_35 = 0
count_40 = 0
count_45 = 0
count_50 = 0
count_100 = 0

line_counter = 0
instance_counter = 0

with open('../.txt') as f:
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
                            if rank_percent <= 0.01:
                                count_p_01 +=1
                            if rank_percent <= 0.1:
                                count_p_1 +=1
                            if rank_percent <= 0.5:
                                count_p_5 +=1
                            if rank_percent <= 1:
                                count_1 +=1
                            if rank_percent <= 5:
                                count_5 +=1
                            if rank_percent <= 10:
                                count_10 +=1
                            if rank_percent <= 15:
                                count_15 +=1
                            if rank_percent <= 20:
                                count_20 +=1
                            if rank_percent <= 25:
                                count_25 +=1
                            if rank_percent <= 30:
                                count_30 +=1
                            if rank_percent <= 35:
                                count_35 +=1
                            if rank_percent <= 40:
                                count_40 +=1
                            if rank_percent <= 45:
                                count_45 +=1
                            if rank_percent <= 50:
                                count_50 +=1
                            if rank_percent <= 100:
                                count_100 +=1
                        except:
                            pass
                except IndexError:
                    pass
    # Comment the line below when using all the words.
    # Uncomment when looking only for the words present in the dictionary.
    instance_counter = count_100
    print "Within Top 0.01% : " + str((count_p_01/instance_counter)*100)
    print "Within Top 0.1% : " + str((count_p_1/instance_counter)*100)
    print "Within Top 0.5% : " + str((count_p_5/instance_counter)*100)
    print "Within Top 1% : " + str((count_1/instance_counter)*100)
    print "Within Top 5% : " + str((count_5/instance_counter)*100)
    print "Within Top 10% : " + str((count_10/instance_counter)*100)
    print "Within Top 15% : " + str((count_15/instance_counter)*100)
    print "Within Top 20% : " + str((count_20/instance_counter)*100)
    print "Within Top 25% : " + str((count_25/instance_counter)*100)
    print "Within Top 30% : " + str((count_30/instance_counter)*100)
    print "Within Top 35% : " + str((count_35/instance_counter)*100)
    print "Within Top 40% : " + str((count_40/instance_counter)*100)
    print "Within Top 45% : " + str((count_45/instance_counter)*100)
    print "Within Top 50% : " + str((count_50/instance_counter)*100)
    print "Within Top 100% : " + str((count_100/instance_counter)*100)
    print "Not Ranked at all : " + str(((instance_counter - count_100)/instance_counter)*100)
    print "Number of Instances : " + str(instance_counter)
