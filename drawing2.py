import random
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Main:
    def __init__(self):
        self.IdealLength = 35
        self.w = 100
        self.h = 100
        self.delta = 0.975
        self.eplison = 0.1
        self.MaxIter = 1000
        
    class Node:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.dx = 0
            self.dy = 0
        
        def disp(self):
            return self.x, self.y

    class Edge:
        def __init__(self, node1, node2, width):
            self.u = node1
            self.v = node2
            self.width = width

    def draw(self, x, y):
        #self.ax.clear()
        # instanciate a figure and ax object
        # annotate is a method that belongs to axes
        """self.ax.plot(x, y, 'o-', markersize=15)

        ## controls the extent of the plot.
        offset = max(x) * 0.1
        self.ax.set_xlim(0, max(x) + offset)
        self.ax.set_ylim(0, max(y) + offset)"""


        # loop through each x,y pair
        #for i, j in zip(x,y):
        #    ax.annotate(str(j),  xy=(i, j), ha='center', va='center')

    
    def ReturnAxis(self, nodes):
        x = []
        y = []
        for node in nodes:
            x.append(node.x)
            y.append(node.y)
        return (x, y)
    
    def ReturnAxis2(self, nodes):
        axis = []
        for node in nodes:
            axis.append((node.x, node.y))
        return axis
        
    def attr(self, u, v):
        return pow(self.nodedist(u, v), 2) / self.IdealLength # * weight
       
    def rep(self, u, v):
         # Max() to prevent ZeroDivisionError error
        return pow(self.IdealLength, 2) / max(self.nodedist(u, v), 0.01)

    def vecdist(self, x, y):
        return math.sqrt(pow(x, 2) + pow(y, 2))

    def nodedist(self, u, v):
        return self.vecdist(v.x - u.x, v.y - u.y)

    # Find the direction
    def normx(self, u, v):
        if (self.nodedist(u, v) == 0):
            return 0
        return (v.x - u.x) / self.nodedist(u, v)

    def normy(self, u, v):
        if (self.nodedist == 0):
            return 0
        return (v.y - u.y) / self.nodedist(u, v)

    def cool(self, temp):
        return self.delta * temp

    def ApplyTemp(self, dir, force, temp):
        return dir / force * min(force, temp * self.IdealLength * 2)

    def default(self, matrix):
        """n = len(matrix)
        nodes = [self.Node(random.uniform(0, self.w), random.uniform(0, self.h)) 
            for _ in range(n)]
        edges = []

        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i != j:
                    edges.append(self.Edge(node1, node2, matrix[i][j]))"""
        nodes = [
            self.Node(247, 849),
            self.Node(382, 126),
            self.Node(485, 67),
            self.Node(200, 0),
            self.Node(103, 398),
            self.Node(817, 664),
            self.Node(786, 370), 
            self.Node(247, 348),
            self.Node(413, 84),
            self.Node(552, 675),
            self.Node(432, 1119),
            self.Node(140, 274),
            self.Node(78, 721), 
            self.Node(558, 979),
            self.Node(590, 0),
            self.Node(554, 267),
            self.Node(414, 407),
            self.Node(736, 233),
            self.Node(827, 855),
            self.Node(65, 702),
            self.Node(261, 136),
            self.Node(867, 25)
        ]
        edges = [
            self.Edge(nodes[0], nodes[1], 1),
            self.Edge(nodes[0], nodes[2], 1),
            self.Edge(nodes[0], nodes[3], 1),
            self.Edge(nodes[0], nodes[4], 1),
            self.Edge(nodes[1], nodes[4], 1),
            self.Edge(nodes[1], nodes[10], 1),
            self.Edge(nodes[1], nodes[18], 1),
            self.Edge(nodes[2], nodes[4], 1),
            self.Edge(nodes[2], nodes[13], 1),
            self.Edge(nodes[2], nodes[19], 1),
            self.Edge(nodes[3], nodes[11], 1),
            self.Edge(nodes[3], nodes[14], 1),
            self.Edge(nodes[4], nodes[18], 1),
            self.Edge(nodes[4], nodes[19], 1),
            self.Edge(nodes[5], nodes[6], 1),
            self.Edge(nodes[5], nodes[7], 1),
            self.Edge(nodes[5], nodes[8], 1),
            self.Edge(nodes[5], nodes[9], 1),
            self.Edge(nodes[6], nodes[9], 1),
            self.Edge(nodes[6], nodes[12], 1),
            self.Edge(nodes[6], nodes[16], 1),
            self.Edge(nodes[7], nodes[9], 1),
            self.Edge(nodes[7], nodes[15], 1),
            self.Edge(nodes[7], nodes[17], 1),
            self.Edge(nodes[8], nodes[20], 1),
            self.Edge(nodes[8], nodes[21], 1),
            self.Edge(nodes[9], nodes[16], 1),
            self.Edge(nodes[9], nodes[17], 1),
            self.Edge(nodes[10], nodes[11], 1),
            self.Edge(nodes[10], nodes[12], 1),
            self.Edge(nodes[11], nodes[16], 1),
            self.Edge(nodes[12], nodes[20], 1),
            self.Edge(nodes[13], nodes[14], 1),
            self.Edge(nodes[13], nodes[15], 1),
            self.Edge(nodes[14], nodes[17], 1),
            self.Edge(nodes[15], nodes[21], 1),
            self.Edge(nodes[16], nodes[17], 1),
            self.Edge(nodes[18], nodes[19], 1),
            self.Edge(nodes[18], nodes[20], 1),
            self.Edge(nodes[19], nodes[21], 1),
            ]
        return nodes, edges

    def run(self, matrix):
        axis = []
        nodes, edges = self.default(matrix)
        iter = 1
        temp = 1
        MaxForce = 1000
        while iter < self.MaxIter and MaxForce > self.eplison:
            #self.ax = self.draw(self.ReturnAxis(nodes)[0], self.ReturnAxis(nodes)[1])
            #MaxForce = 0
            iter += 1

            # Compute Forces
            for i, u in enumerate(nodes):
                u.dx = 0
                u.dy = 0
                for j, v in enumerate(nodes):
                    if i != j:
                        u.dx += self.rep(u, v) * self.normx(v, u)
                        u.dy += self.rep(u, v) * self.normy(v, u)

            for e in edges:
                u = e.u
                v = e.v
                u.dx += self.attr(u, v) * self.normx(u, v)
                u.dy += self.attr(u, v) * self.normy(u, v)
                v.dx += self.attr(v, u) * self.normx(v, u)
                v.dy += self.attr(v, u) * self.normy(v, u)

            for i, u in enumerate(nodes):
                u.force = self.vecdist(u.dx, u.dy)
                if u.force > 0:
                    #if iter == 2:
                    #    print("hey", u.dx / u.force * min(u.force, temp * self.IdealLength * 2))
                    u.dx = self.ApplyTemp(u.dx, u.force, temp)
                    u.dy = self.ApplyTemp(u.dy, u.force, temp)
                u.force = self.vecdist(u.dx, u.dy)
                MaxForce = max(MaxForce, u.force)
                u.x = u.x + u.dx
                u.y = u.y + u.dy
            temp = self.cool(temp)
            axis.append(self.ReturnAxis(nodes))
        return axis

m = Main()
M = [random.sample(range(0, 30), 30) for i in range(30)]


axis = m.run(M)
fig, ax = plt.subplots()
pt, = ax.plot([], [], 'o-', markersize=10)
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
count = 0
def animate(frame):
    x, y = frame
    pt.set_data(x, y)
    ax.set_xlim(min(x) - max(x) * 0.1, max(x) + max(x) * 0.1)
    ax.set_ylim(min(y) - max(y) * 0.1, max(y) + max(y) * 0.1)
    return pt,

ani = FuncAnimation(fig, animate, frames=axis,
                    interval=200, repeat=False)

#print(axis)
plt.show()
