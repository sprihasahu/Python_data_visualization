import matplotlib.pyplot as plt
'''
plt.xlabel('x axis value')
plt.ylabel('y axis value')
plt.title('my first graph')
'''
values=[40,30,15,15]
expenses=['rent','groceries','transport','savings']
ex=[0.1,0,0,0]
plt.pie(values, labels=expenses,autopct='%.1f%%',explode=ex)
plt.title('monthly budget')
plt.show()