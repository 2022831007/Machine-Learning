
from sklearn.linear_model import LogisticRegression
X = [[1],[2],[3],[4],[5]]#per hour studied
y = [0,0,1,1,1] #result 0->F,1->T
model = LogisticRegression()
model.fit(X,y)
hours = float((input("Enter How many Hours you have studied= ")))
result = model.predict([[hours]])[0]
if result == 1:
    print(f"Based on hours {hours},you are likely to Pass")

else:
    print(f"Based on hours {hours},you are likely to Pass")

  