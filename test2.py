import matplotlib.pyplot as plt
'''
plt.xlabel('x axis value')
plt.ylabel('y axis value')
plt.title('my first graph')
'''
subjects=['os','python','java','networks','data analysis']
scores=[88,89,78,79,97]
plt.xlabel('subjects')
plt.ylabel('score')
plt.title('College Semester')
plt.bar(subjects,scores,color=['pink','purple'])
plt.show()