# Springpy

![Pypi Version](https://img.shields.io/pypi/v/springpy?label=Pypi%20Version)  
Springpy visualises a distance matrix.

## Download
```sh
pip3 install springpy
```

## Usage
```py
import springpy as sp
matrix = [[0, 0.2, 0.1],
		  [0.2, 0, 0.3],
		  [0.1, 0.3, 0]]

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
Data: Click Here

Result(animation & video):

https://user-images.githubusercontent.com/30309285/230230490-a8efb0eb-b12b-4ed2-9f08-1aefd3099c97.mp4

Result(graph):
Currently Unavaliable(Visit GitHub page for more information)

### Change Default Values
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
- [Bibliography](https://www.github.com/kiwirafe/springpy)
