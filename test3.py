import matplotlib.pyplot as plt
'''
plt.xlabel('x axis value')
plt.ylabel('y axis value')
plt.title('my first graph')
'''
days=['mon','tue','wed','thur','fri','sat','sun']
visits=[200,233,201,234,345,456,900]
plt.xlabel('days in a week')
plt.ylabel('newspaper visit color')
plt.title('newspaper reading survey')
plt.plot(days,visits,color='orange',linestyle='-',linewidth=5)
plt.show()