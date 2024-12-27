from sklearn import tree
import random

x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
y = ["male", "female", "female", "female", "male", "male", "male", "female", "male", "female", "male"]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)

#prediction = clf.predict([[150, 60, 40]])

for i in range(5):
	dp = [random.randint(150, 200), random.randint(50, 90), random.randint(35, 50)]
	val = clf.predict([dp])
	print("The values for height, weight, and foot size are as follows: ", dp[0], ",", dp[1], ",", dp[2])
	print("The gender for this value is: " + val[0])