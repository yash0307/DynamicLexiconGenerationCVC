import matplotlib.pyplot as plt

x = [1,10,100,1000,10000,100000]
y_baseline = [0.169479800775, 1.06876037631, 4.50332042059, 18.8503043719, 56.3848920863, 100.00]
y_1000 = []
y_100 = []
y_10 = []
y_2000 = []
y_200 = []
y_30 =  []
y_400 = []
y_500 = []
y_50 = []
y_80 = []
plt.plot(x,y_baseline,label='Baseline')
plt.plot(x,y_30, label='num_topics = 30')
plt.plot(x,y_50, label='num_topics = 50')
plt.plot(x,y_80, label='num_topics = 80')
plt.plot(x,y_100, label='num_topics = 100')
plt.plot(x,y_200, label='num_topics = 200')
plt.plot(x,y_400, label = 'num_topics = 400')
plt.plot(x,y_500, label = 'num_topics = 500')
plt.plot(x,y_1000, label = 'num_topics = 1000')
plt.plot(x,y_2000, label = 'num_topics = 2000')
plt.xlabel("top x% words of dictionary")
plt.ylabel("Percentage of Instances")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
            ncol=5, mode="expand", borderaxespad=0.)
plt.show()
