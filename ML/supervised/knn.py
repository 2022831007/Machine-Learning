from sklearn.neighbors import KNeighborsClassifier
X = [
    [100,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]
#0 = Apple, 1=Orange
y = [0,0,0,1,1,1]
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
weight = float(input("Enter the weight in grams: "))
size = float(input("Enter the size in grams: "))
prediction = model.predict([[weight,size]])[0]
if prediction==0:
    print("This is likely an Apple")

else:
    print("This is likely Orange")    


