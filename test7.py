import matplotlib.pyplot as plt

values = [40, 30, 15, 15, 22, 23, 67, 55, 46, 34]

plt.hist(values, bins=10, color='red', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My First Histogram')

plt.show()