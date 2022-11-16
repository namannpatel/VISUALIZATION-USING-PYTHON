import matplotlib.pyplot as plt
subject=['English Core','Mathematics', 'Physics', 'Chemistry', 'I.P.']
percentage=[83,95,70, 89, 100]
plt.bar(subject,percentage, align='center', color='black')
plt.xlabel('Subject Name')
plt.ylabel('Student Name')
plt.title('Result Analysis Bar Graph ')
plt.show()
