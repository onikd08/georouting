import matplotlib.pyplot as plt
import math


nodes = set()
dis = {}
coordinates = {}
edges = []
pred = {}


with open('test2.txt') as f:
    for line in f:
        data = line.replace("\n", "").split(" ")
        if len(data) == 3:
            nodes.add(data[0])
            coordinates[data[0]] = [float(data[1]), float(data[2])]
        elif len(data) == 2:
            if data[0] == data[1]:
                continue
            if data[0] not in dis:
                dis[data[0]] = {}
            if data[1] not in dis:
                dis[data[1]] = {}
            dis[data[0]][data[1]] = 1

            # dis[data[1]][data[0]] = 1
            edges.append(data)
            plt.plot([coordinates[data[0]][0], coordinates[data[1]][0]], [coordinates[data[0]][1], coordinates[data[1]][1]], 'r-')

f.close()

for nodeI in nodes:
    if nodeI not in dis:
        dis[nodeI] = {}
    dis[nodeI][nodeI] = 0
    pred[nodeI] = {}
    plt.plot([coordinates[nodeI][0]], [coordinates[nodeI][1]], 'bo')
    for nodeJ in nodes:
        if nodeJ not in dis:
            dis[nodeJ] = {}
        if nodeJ not in dis[nodeI]:
            dis[nodeI][nodeJ] = math.inf
        pred[nodeI][nodeJ] = -1

plt.title("Primary Graph")
plt.show()
source = input("Source: ")
destination = input("Destination: ")


# generate path weight for all pair node
for nodeK in nodes:
    for nodeI in nodes:
        for nodeJ in nodes:
            tmp = dis[nodeI][nodeJ]
            dis[nodeI][nodeJ] = min(dis[nodeI][nodeJ], dis[nodeI][nodeK] + dis[nodeK][nodeJ])
            if tmp != dis[nodeI][nodeJ]:
                pred[nodeI][nodeJ] = nodeK


def show_nodes():
    for nodeI in nodes:
        if nodeI == source:
            plt.plot([coordinates[nodeI][0]], [coordinates[nodeI][1]], 'ro', label='Source Node')
        elif nodeI == destination:
            plt.plot([coordinates[nodeI][0]], [coordinates[nodeI][1]], 'go', label='Destination Node')
        else:
            plt.plot([coordinates[nodeI][0]], [coordinates[nodeI][1]], 'ko')



# Path Show Start
show_nodes()
for edge in edges:
    plt.plot([coordinates[edge[0]][0], coordinates[edge[1]][0]], [coordinates[edge[0]][1], coordinates[edge[1]][1]],
             'r-')


def show_optimal_path(u, v):
    if pred[u][v] == -1:
        if dis[u][v] != math.inf:
            plt.plot([coordinates[u][0], coordinates[v][0]], [coordinates[u][1], coordinates[v][1]],
                 'g-')
    else:
        show_optimal_path(u, pred[u][v])
        show_optimal_path(pred[u][v], v)


show_optimal_path(source, destination)
plt.title("Optimal Path")
plt.legend()
plt.show()
# Path Show End

