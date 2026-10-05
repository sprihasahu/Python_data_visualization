import matplotlib.pyplot as plt
'''
plt.xlabel('x axis value')
plt.ylabel('y axis value')
plt.title('my first graph')
'''
days=['mon','tue','wed','thur','fri','sat','sun']
visits=[200,233,201,234,345,456,900]
visit2=[100,123,134,101,45,156,600]
plt.xlabel('days ')
plt.ylabel('count')
plt.title('website visit count')
plt.scatter(days,visits,color='blue')
plt.show()