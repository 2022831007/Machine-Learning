#%%
import matplotlib.pyplot as plt
# hours_studies = [1,2,3,4,5,6,7]
# exam_scores = [50,55,76,77,78,80,85]
plt.scatter([1,2,3],[50,60,70],color='blue',label='Class A')
plt.scatter([1,2,3],[45,55,52],color='orange',label='Class B')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title("relationship betwen study and exam score")
plt.legend()
plt.grid(True)
plt.show()
# %%
