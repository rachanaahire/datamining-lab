#KNN with 2 Clusters
import matplotlib.pyplot as plt
from operator import itemgetter

data = [[185, 72, 1], [170, 56, 0], [168, 60, 0], [179, 68, 1],
        [182, 72, 1], [188, 77, 1], [173, 61, 0], [180, 70, 1],
        [183, 84, 1], [171, 59, 0], [180, 75, 1], [177, 76, 1]]

for point in data:
    if(not point[-1]):
        plt.scatter(point[0], point[1], color="red")
    elif(point[-1]):
        plt.scatter(point[0], point[1], color="blue")
plt.show()


# Calculate euclidean distance
def euclidean_distance(test_point, row_point):
    X = (row_point[0]-test_point[0])**2
    Y = (row_point[1]-test_point[1])**2
    res = (X + Y)**0.5
    return res


# Get nearest neighbours
def neighbours(data, test_point, num):
    distances = []
    for row in data:
        dist = euclidean_distance(test_point, row)
        distances.append([row, round(dist, 2)])
    sorted(distances, key=itemgetter(1))
    print("\nDistances from :", test_point)
    for dist in distances:
        print(dist)
    n = []
    for i in range(num):
        n.append(distances[i][0])
    return n


# Classification
def classification(data, test_point, num):
    pred = None
    n = neighbours(data, test_point, num)
    print("\nThe nearest neighbours are: ", n)
    output_values = [row[-1] for row in n]
    zero = output_values.count(0)
    one = output_values.count(1)
    print
    if(zero > one):
        pred = 0
    elif(one > zero):
        pred = 1
    return pred


test_point = [175, 60]
print("Data point to classify: ", test_point)
prediction = classification(data, test_point, 3)
test_point.append(prediction)
plt.scatter(test_point[0], test_point[1], s=80, color="green")
for point in data:
    if(not point[-1]):
        plt.scatter(point[0], point[1], color="red")
    elif(point[-1]):
        plt.scatter(point[0], point[1], color="blue")
plt.show()

data.append(test_point)
print("\nTest data point falls under cluster",prediction,"(", "BLUE" if prediction else "RED",")")
for point in data:
    if(not point[-1]):
        plt.scatter(point[0], point[1], s=80, color="red")
    elif(point[-1]):
        plt.scatter(point[0], point[1], color="blue")
plt.show()
