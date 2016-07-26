###########################################################################################
############################ git@yash0307 #################################################
###########################################################################################
import json

# Open data file containing : Text, Caption.
with open('./Data_Caption_Text/evalValSet.json') as data_file:
    data = json.load(data_file)

# Take input from user.
analysis_type = raw_input("CHOOSE DICTIONARY. 'our' or 'jad' or 'dataset or jad_sw'\n")

# Load the Ranked dictionary. Which is made according to frequency.
if analysis_type.lower() == "our":
    with open('./Ranked_dict/our_dict.json') as our_dict:
        ranked_dict = json.load(our_dict)
elif analysis_type.lower() == "jad":
    with open('./Ranked_dict/jad_dict.json') as jad_dict:
        ranked_dict = json.load(jad_dict)
elif analysis_type.lower() == "dataset":
    with open('./Ranked_dict/all_gensim_dict.json') as dataset_dict:
        ranked_dict = json.load(dataset_dict)
elif analysis_type.lower() == "jad_sw":
    with open('./Ranked_dict/jad_sw_gensim_dict.json') as dataset_dict:
        ranked_dict = json.load(dataset_dict)

# Make final ranked list of words.
final_ranks = []
for i in ranked_dict:
    final_ranks.append(str(i[0].lower()))
print str(final_ranks[0:5])
# For each text image. Generate ranking.
f = open("results_jad_sw.txt", 'w')
counter = 0
for ind in data.keys():
    counter = counter + 1
    value = data[ind]
    texts = value['text']
    text_ranks = []
    for text in texts:
        try:
            text_ranks.append(str(text) + " : " + str(final_ranks.index(str(text.lower()))))
        except ValueError:
            try:
                text_ranks.append(str(text) + " : NA")
            except:
                text_ranks.append("Unicode error")
    f.write(str(text_ranks) + "\n")
    f.write("Total words : " + str(len(final_ranks)) + "\n")
    f.write("---------------------------------------\n")
    print str(counter)
f.close()
