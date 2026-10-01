import matplotlib.pyplot as plt
hours_studies = [1,2,3,4,5,6,7]
exam_scores = [50,55,76,77,78,80,85]
plt.scatter(hours_studies,exam_scores,color='green',marker='o',label='Student data')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title("relationship betwen study and exam score")
plt.legend()
plt.grid()
plt.show()