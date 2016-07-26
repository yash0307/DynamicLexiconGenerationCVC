import matplotlib.pyplot as plt

#zoom_type = "in"
zoom_type = "out"
if zoom_type == "in":
    x = [0.01,0.1,0.5,1]
    y_baseline = [0.548049961764, 4.96431302575, 14.4086158552, 20.7749171552]
    y_15 = [1.85444812643, 6.32169258221, 16.7919959215, 25.5544226357]
    y_20 = [1.60591384145, 6.23884782055, 16.8302319653, 24.8406831507]
    y_30 = [1.59954116747, 6.68493499873, 18.5635992863, 25.968646444]
    y_50 = [2.21131786898, 8.59673719093, 20.2778485853, 27.8995666582]
    y_400 = [3.52408870762, 11.1011980627, 21.5842467499, 27.2304358909]
elif zoom_type == "out":
    x = [0.01,0.1,0.5,1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    y_baseline = [0.548049961764, 4.96431302575, 14.4086158552, 20.7749171552, 49.0695895998, 63.5801682386, 72.3872036707, 78.4603619679, 82.3222023961, 85.1070609228, 87.5541677288, 89.3257710936, 90.7596227377, 92.1998470558, 93.4488911547, 94.4494009686, 95.5008921744, 96.3675758348, 97.1004333418, 97.9097629365, 98.5151669641, 99.018608208, 99.5602854958, 100.0]
    y_15 = [1.85444812643, 6.32169258221, 16.7919959215, 25.5544226357, 51.0323731838, 63.1022176905, 70.3734386949, 75.2803976549, 78.7280142748, 81.7614070864, 84.4443028295, 86.6683660464, 88.6948763701, 90.6512872801, 92.397399949, 94.1371399439, 95.8832526128, 97.1131786898, 98.1009431557, 98.7573285751, 99.2990058629, 99.6941116492, 99.9107825644, 100.0]
    y_20 = [1.60591384145, 6.23884782055, 16.8302319653, 24.8406831507, 51.9882742799, 63.7713484578, 70.8577619169, 75.7583482029, 79.3397909763, 82.4624012236, 84.9923527912, 87.254652052, 89.4022431812, 91.5307162886, 93.1238847821, 94.8062707112, 96.1381595718, 97.3298496049, 98.3431047668, 98.8019372929, 99.3627326026, 99.6813663013, 99.9235279123, 100.0]
    y_30 = [1.59954116747, 6.68493499873, 18.5635992863, 25.968646444, 52.3005353046, 64.453224573, 71.2656130512, 76.3127708386, 79.894213612, 82.9339790976, 85.9418812134, 88.6821310222, 90.8615855213, 92.6140708641, 94.3155748152, 95.7940351772, 96.8518990568, 97.8078001529, 98.3112413969, 98.8019372929, 99.1396890135, 99.4392046903, 99.6686209534, 100.0]
    y_50 = [2.21131786898, 8.59673719093, 20.2778485853, 27.8995666582, 52.6574050472, 63.9115472852, 70.1886311496, 75.3313790466, 79.7476421106, 83.4374203416, 86.8276828957, 89.5615600306, 91.7282691817, 93.4361458068, 94.857252103, 95.9342340046, 96.807290339, 97.5274024981, 98.0053530461, 98.4195768544, 98.8019372929, 99.254397145, 99.6176395616, 100.0]
    y_400 = [3.52408870762, 11.1011980627, 21.5842467499, 27.2304358909, 43.7101707877, 54.2187101708, 66.1929645679, 76.1916900331, 81.7868977823, 85.0114708132, 87.2928880958, 89.0517461127, 90.6640326281, 92.1297476421, 93.0537853683, 94.0479225083, 94.850879429, 95.7175630895, 96.4376752485, 97.1641600816, 97.8842722406, 98.5024216161, 99.2416517971, 100.0]

plt.plot(x,y_baseline,label='baseline')
#plt.plot(x,y_15,label='num = 15')
#plt.plot(x,y_20,label='num = 20')
plt.plot(x,y_30, label='num = 30')
plt.plot(x,y_50, label='num = 50')
#plt.plot(x,y_400, label = 'num = 400')

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=5, mode="expand", borderaxespad=0.)
plt.show()
