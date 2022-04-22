#KNN with 3 Clusters
import matplotlib.pyplot as plt

def plot_graph(data):
    for cluster, dataset in data.items():
        if(cluster == 0):
            for points in dataset:
                plt.scatter(points[0], points[1], color="red")
        elif(cluster == 1):
            for points in dataset:
                plt.scatter(points[0], points[1], color="blue")
        elif(cluster == 2):
            for points in dataset:
                plt.scatter(points[0], points[1], color="yellow")
    plt.show()

def euclidean_distance(test_point, row_point):
    return (((row_point[0]-test_point[0])**2) + ((row_point[1]-test_point[1])**2))**0.5


def find_neighbours(data, test_val, num):
    distances = []
    for row in data:
        dist = euclidean_distance(test_val, row)
        distances.append([row, round(dist, 2)])
    distances.sort(key=lambda x: x[1])
    neighbours = []
    for i in range(num):
        neighbours.append(distances[i][0])
    return neighbours


def classify(data, test_point, num):
    pred = None
    n = find_neighbours(data, test_point, num)
    print("\nThe nearest neighbours are: ", n)
    cluster_values = [row[-1] for row in n]
    red = cluster_values.count(0)
    blue = cluster_values.count(1)
    yellow = cluster_values.count(2)
    print
    if(red > blue and red > yellow):
        pred = 0
    elif(blue > red and blue > yellow):
        pred = 1
    elif(yellow > blue and yellow > red):
        pred = 2
    return pred


data = {0: [[170, 56], [168, 60], [171, 59], [173, 61]],
        1: [[185, 72], [179, 68], [182, 72], [188, 77], [180, 70], [183, 84], [180, 75], [177, 76]],
        2: [[170, 85], [169, 83], [167, 80], [166, 85]]}

#first graph (original dataset)
plot_graph(data)

# ask for data point input
test_point = []
test_point.append(int(input("Enter x: ")))
test_point.append(int(input("Enter y: ")))

print("\n\nData point to check: ", test_point)
merged_data = []
for key, val in data.items():
    for val2 in val:
        val2.append(key)
        merged_data.append(val2)

#Second Graph (with test dataset highlighted)
prediction = classify(merged_data, test_point, 3)
test_point.append(prediction)
plt.scatter(test_point[0], test_point[1], s=80, color="green")
plot_graph(data)

# Third Graph (classification output)
data[prediction].append(test_point)
plot_graph(data)
