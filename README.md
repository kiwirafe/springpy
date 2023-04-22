# Springpy

### Springpy visualises a distance matrix.
While similar to the "Spring Function" in [qgraph](https://github.com/SachaEpskamp/qgraph) in R and [networkx](https://networkx.org/) in Python, **springpy** provides a simple way to visualize a distance matrix using the Fruchterman Reingold method. **Springpy** allows you to create a spring graph or animate a distance matrix in just one line of code.

## Download
```sh
pip3 install springpy
```

## Usage
```py
import springpy as sp
matrix = [[0         , 0.00638545,  0.28778769],
          [0.00638545, 0         ,  0.21402251],
          [0.28778769, 0.21402251,  0         ]]

# Show a matplotlib animation
sp.animate(matrix)

# Save to video (Default Name:"spring_result.mp4")
sp.animate(matrix, save=True)

# Show a matplotlib graph
sp.graph(matrix)

# Save the graph(Default Name:"spring_result.jpg")
sp.graph(matrix, save=True)
```
Input: A [distance matrix](https://www.wikipedia.org/wiki/Distance_matrix) embedded into a 2D Python List.

### Demonstration:
Data: [dmatrix.csv](https://github.com/kiwirafe/springpy/blob/main/example/dmatrix.csv)  
Code: [example.py](https://github.com/kiwirafe/springpy/blob/main/example/example.py)

Result(animation & video):

https://user-images.githubusercontent.com/30309285/230230490-a8efb0eb-b12b-4ed2-9f08-1aefd3099c97.mp4

Result(graph):
![springpy_result](https://user-images.githubusercontent.com/30309285/233753442-ec1ed362-64dd-4dd4-a9ea-7c59c5f7c27d.jpg)

### Change Default Values
#### For Calculation
```py
import springpy as sp

# Width of the graph, default 100px
sp.w = 100
# Height of the graph, default 100px
sp.h = 100
# Cool down delta, default 0.975
sp.delta = 0.975
# The eplison, if the change is smaller than this value, then stop iterating, default 5
sp.eplison = 10
# Max iteration, the maximum number of iterations, default 500
sp.MaxIter = 500
```

#### For sp.animate:
```py
sp.animate(self, matrix, save=False, interval=100, VideoName="springpy_result.mp4"):
"""
:param save: whether to save the video, default False
:param interval: the interval between frames, default 100
:param VideoName: the name of the video for the result, default "springpy_result.gif". Note that this name must include the suffix(ie .gif)
""" 
```

#### For sp.graph:
```py
sp.graph(self, matrix, save=False, ImageName = "springpy_result.jpg"):
"""
:param save: whether to save the graph, default False
:param VideoName: the name of the graph for the result, default "springpy_result.jpg". Note that this name must include the suffix(ie .jpg or .png)
""" 
```

## Links
- [kiwirafe.com](kiwirafe.com)
- [Bibliography](https://github.com/kiwirafe/springpy/blob/main/Bib.md)
- [Example](https://github.com/kiwirafe/springpy/tree/main/example)