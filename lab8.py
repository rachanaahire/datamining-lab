#K MEANS

import matplotlib.pyplot as plt

k = 2
data = [[185, 72],[170,56],[168,60],[179,68],
        [182, 72],[188,77],[173,61],[180,70],
        [183, 84],[171,59],[180,75],[177,76]]

c1 = data[0]
c2 = data[1]
k1 = [data[0]]
k2 = [data[1]]

def distance(c,p):
    X = (p[0]-c[0])**2
    Y = (p[1]-c[1])**2
    res = (X + Y)**0.5
    return res

def centroid(c, p):
    x = (p[0] + c[0])/2
    y = (p[1] + c[1])/2
    return [x,y]


def opr(c1, c2, data):
    one = distance(c1, data)
    two = distance(c2, data)
    print("k1=>",c1)
    print("k2=>",c2)
    if (one < two):
        k1.append(data)
        c1 = centroid(c1, data)
    else:
        k2.append(data)
        c2 = centroid(c2, data)
    
    return [c1,c2]

for x in range(2, len(data)):
    c1 , c2 = opr(c1, c2, data[x])

k1x = [a[0] for a in k1]
k1y = [a[1] for a in k1]
k2x = [a[0] for a in k2]
k2y = [a[1] for a in k2]

print("K1===> ", k1)
print("K2===>", k2)

plt.scatter(k1x, k1y, c='blue')
plt.scatter(k2x, k2y, c='red')
plt.show()

