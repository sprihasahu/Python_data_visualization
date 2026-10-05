import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.xlabel('x axis value')
plt.ylabel('y axis value')
plt.title('my first graph')
plt.plot(x,y,color='pink',marker='s')
plt.show()
plt.grid()
