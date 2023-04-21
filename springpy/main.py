import random
import math
import os
from functools import partial
import matplotlib.pyplot as plt
import matplotlib.animation as ani

class Main:
    def __init__(self):
        self.IdealLength = 35
        self.w = 100
        self.h = 100
        self.delta = 0.975
        self.eplison = 10
        self.MaxIter = 500
        self.animation = False
        
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
    
    # Returns axis like x = [x1, x2] y = [x1, x2]
    def ReturnAxis(self, nodes):
        x = []
        y = []
        for node in nodes:
            x.append(node.x)
            y.append(node.y)
        return (x, y)
    
    # Returns axis like [(x1, y1), (x2, y2)]
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

    # Turn the matrix into apporiate nodes and edges
    def default(self, matrix):
        n = len(matrix)
        # Apply a random axis at the start
        nodes = [self.Node(random.uniform(0, self.w), random.uniform(0, self.h)) 
            for _ in range(n)]
        edges = []

        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i != j:
                    edges.append(self.Edge(node1, node2, (matrix[i][j] + matrix[j][i]) / 2))
            
        return nodes, edges
        
    def cool(self, temp):
        return self.delta * temp

    def ApplyTemp(self, dir, force, temp):
        return dir / force * min(force, temp * self.IdealLength * 2)

    # Main function to calcuate
    def run(self, matrix):
        axis = []
        nodes, edges = self.default(matrix)
        self.IdealLength = math.sqrt(self.w * self.h / len(matrix))
        iter = 1
        temp = 1
        MaxForce = 1000
        # Break if MaxIter reached or the change in distance(size of force)
        # is smaller than the eplison, which meaning no significant change
        while iter < self.MaxIter and MaxForce > self.eplison:
            #self.ax = self.draw(self.ReturnAxis(nodes)[0], self.ReturnAxis(nodes)[1])
            #MaxForce = 0
            iter += 1

            # Compute Forces
            # The relpusion force
            for i, u in enumerate(nodes):
                u.dx = 0
                u.dy = 0
                for j, v in enumerate(nodes):
                    if i != j:
                        u.dx += self.rep(u, v) * self.normx(v, u)
                        u.dy += self.rep(u, v) * self.normy(v, u)

            # The attracting force
            for e in edges:
                u = e.u
                v = e.v
                u.dx += self.attr(u, v) * self.normx(u, v) * e.width
                u.dy += self.attr(u, v) * self.normy(u, v) * e.width
                v.dx += self.attr(v, u) * self.normx(v, u) * e.width
                v.dy += self.attr(v, u) * self.normy(v, u) * e.width

            for i, u in enumerate(nodes):
                u.force = self.vecdist(u.dx, u.dy)
                if u.force > 0:
                    u.dx = self.ApplyTemp(u.dx, u.force, temp)
                    u.dy = self.ApplyTemp(u.dy, u.force, temp)
                u.force = self.vecdist(u.dx, u.dy)
                MaxForce = min(MaxForce, u.force)

                # Update the axis
                u.x = u.x + u.dx
                u.y = u.y + u.dy

            # To cool the graph down and append the current axis
            temp = self.cool(temp)

            if self.animation:
                axis.append(self.ReturnAxis(nodes))

        if self.animation:
            return axis
        else:
            return self.ReturnAxis(nodes)

    def AnimateFunc(self, frame, pt, ax):
        x, y = frame
        pt.set_data(x, y)
        # Changes the x and y limits to make the graph corresponding
        ax.set_xlim(min(x) - max(x) * 0.2, max(x) + max(x) * 0.2)
        ax.set_ylim(min(y) - max(y) * 0.2, max(y) + max(y) * 0.2)
        return pt,

    # Animate the entire process
    def animate(self, matrix, save=False, interval=100, VideoName="springpy_result.gif"):
        self.animation = True
        axis = self.run(matrix)
        fig, ax = plt.subplots()
        pt, = ax.plot([], [], 'o-', markersize=10)

        animation = ani.FuncAnimation(fig, partial(self.AnimateFunc, pt=pt, ax=ax), frames=axis,
                    interval=interval, repeat=False)
        
        if save:
            animation.save(os.path.join(os.path.abspath(os.getcwd()), VideoName))
        else:
            plt.show()
        
    def graph(self, matrix, save=False, ImageName = "springpy_result.jpg"):
        #self.ax.clear()
        # Annotate is a method that belongs to axes
        (x, y) = self.run(matrix)
        fig, ax = plt.subplots()
        ax.plot(x, y, 'o-', markersize=15)

        ## controls the extent of the plot.
        ax.set_xlim(min(x) - max(x) * 0.2, max(x) + max(x) * 0.2)
        ax.set_ylim(min(y) - max(y) * 0.2, max(y) + max(y) * 0.2)

        count = 1
        # Loop through each x, y pair
        for i, j in zip(x, y):
            ax.annotate(str(count),  xy=(i, j), ha='center', va='center')
            count += 1
        
        if save:
            plt.savefig(ImageName)
        else:
            plt.show()