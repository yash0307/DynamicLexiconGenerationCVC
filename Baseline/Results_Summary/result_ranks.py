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
count_55 = 0
count_60 = 0
count_65 = 0
count_70 = 0
count_75 = 0
count_80 = 0
count_85 = 0
count_90 = 0
count_95 = 0
count_100 = 0

#count_top_1 = 0
#count_top_5 = 0
#count_top_10 = 0
#count_top_50 = 0
#count_top_100 = 0
#count_top_500 = 0
#count_top_1000 = 0
#count_top_2000 = 0
#count_top_5000 = 0

line_counter = 0
instance_counter = 0

with open('../ICDAR/results_eval.txt') as f:
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
#                           if word_rank == 0:
#                               count_top_1 +=1
#                           if word_rank <= 5:
#                               count_top_5 +=1
#                           if word_rank <= 10:
#                                count_top_10 +=1
#                            if word_rank <= 50:
#                                count_top_50 +=1
#                            if word_rank <= 100:
#                                count_top_100 +=1
#                            if word_rank <= 500:
#                                count_top_500 +=1
#                            if word_rank <= 1000:
#                                count_top_1000 +=1
#                            if word_rank <= 2000:
#                                count_top_2000 +=1
#                            if word_rank <= 5000:
#                                count_top_5000 +=1
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
                            if rank_percent <= 55:
                                count_55 +=1
                            if rank_percent <= 60:
                                count_60 +=1
                            if rank_percent <= 65:
                                count_65 +=1
                            if rank_percent <= 70:
                                count_70 +=1
                            if rank_percent <= 75:
                                count_75 +=1
                            if rank_percent <= 80:
                                count_80 +=1
                            if rank_percent <= 85:
                                count_85 +=1
                            if rank_percent <= 90:
                                count_90 +=1
                            if rank_percent <=95:
                                count_95 +=1
                            if rank_percent <= 100:
                                count_100 +=1
                        except:
                            pass
                except IndexError:
                    pass
    instance_counter = count_100
    print str((count_p_01/instance_counter)*100)
    #print "Within Top 0.01% : " + str((count_p_01/instance_counter)*100)
    print str((count_p_1/instance_counter)*100)
    #print "Within Top 0.1% : " + str((count_p_1/instance_counter)*100)
    print str((count_p_5/instance_counter)*100)
    #print "Within Top 0.5% : " + str((count_p_5/instance_counter)*100)
    print str((count_1/instance_counter)*100)
    #print "Within Top 1% : " + str((count_1/instance_counter)*100)
    print str((count_5/instance_counter)*100)
    #print "Within Top 5% : " + str((count_5/instance_counter)*100)
    print str((count_10/instance_counter)*100)
    #print "Within Top 10% : " + str((count_10/instance_counter)*100)
    print str((count_15/instance_counter)*100)
    #print "Within Top 15% : " + str((count_15/instance_counter)*100)
    print str((count_20/instance_counter)*100)
    #print "Within Top 20% : " + str((count_20/instance_counter)*100)
    print str((count_25/instance_counter)*100)
    #print "Within Top 25% : " + str((count_25/instance_counter)*100)
    print str((count_30/instance_counter)*100) 
    #print "Within Top 30% : " + str((count_30/instance_counter)*100)
    print str((count_35/instance_counter)*100)
    #print "Within Top 35% : " + str((count_35/instance_counter)*100)
    print str((count_40/instance_counter)*100)
    #print "Within Top 40% : " + str((count_40/instance_counter)*100)
    print str((count_45/instance_counter)*100)
    #print "Within Top 45% : " + str((count_45/instance_counter)*100)
    print str((count_50/instance_counter)*100)
    print str((count_55/instance_counter)*100)
    print str((count_60/instance_counter)*100)
    print str((count_65/instance_counter)*100)
    print str((count_70/instance_counter)*100)
    print str((count_75/instance_counter)*100)
    print str((count_80/instance_counter)*100)
    print str((count_85/instance_counter)*100)
    print str((count_90/instance_counter)*100)
    print str((count_95/instance_counter)*100)
    #print "Within Top 50% : " + str((count_50/instance_counter)*100)
    #print "\n\n"
    #print "Within Top 1 ranks : " + str((count_top_1/instance_counter)*100)
    #print "Within Top 5 ranks : " + str((count_top_5/instance_counter)*100)
    #print "Within Top 10 ranks : " + str((count_top_10/instance_counter)*100)
    #print "Within Top 50 ranks : " + str((count_top_50/instance_counter)*100)
    #print "Within Top 100 ranks : " + str((count_top_100/instance_counter)*100)
    #print "Within Top 500 ranks : " + str((count_top_500/instance_counter)*100)
    #print "Within Top 1000 ranks : " + str((count_top_1000/instance_counter)*100)
    #print "Within Top 2000 ranks : " + str((count_top_2000/instance_counter)*100)
    #print "Within Top 5000 ranks : " + str((count_top_5000/instance_counter)*100)
    #print "Within Top 100% : " + str((count_100/instance_counter)*100)
    print str((count_100/instance_counter)*100)
    print "Not Ranked at all : " + str(((instance_counter - count_100)/instance_counter)*100)
    print "Number of Instances : " + str(instance_counter)
