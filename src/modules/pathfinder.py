import numpy as np
import matplotlib.pyplot as plt


class Pathfinder:
    """
    A class representing that optimizes bot routes with Manhatan Distance Shortest Path
    
    """
    def __init__(self):
        pass
    
    def manhattan_distance(self, start: list, target: list):
        return abs(start[0] - target[0]) + abs(start[1] - target[1])
    
    def shortest_path_nearest_neighbors(self, start: list, destionations: list) -> list:
        self.start = start
        coords = [start] + destionations
        visited = [False] * len(coords)
        path_by_index = [0] * len(coords)
        current = 0
        visited[current] = True
        for i in range(1, len(coords)):
            nearest_dist = float('inf')
            nearest_index = -1
            for j in range(len(coords)):
                if not visited[j]:
                    dist = self.manhattan_distance(coords[current], coords[j])
                    if dist < nearest_dist:
                        nearest_dist = dist
                        nearest_index = j
            visited[nearest_index] = True
            path_by_index[i] = nearest_index
            current = nearest_index
        self.path = [coords[i] for i in path_by_index]
        return self.path[1:]
     
    
    def _init_grid(self): 
        try:
            min_x = np.min(np.array(self.path), axis=0)[0]
            min_y = np.min(np.array(self.path), axis=0)[1]
            max_x = np.max(np.array(self.path), axis=0)[0]
            max_y = np.max(np.array(self.path), axis=0)[1]
            grid = [[x, y] for y in range(min_y, max_y+1) for x in range(min_x, max_x+1)]
            self.grid = [x for x, _ in grid], [y for _, y in grid]
        except:
            self.grid = []

    def plot_path(self):
        self._init_grid()
        if len(self.grid != 0):
            plt.scatter(self.grid[0], self.grid[0], label='No Wheat')
            labels = range(1, len(self.path))
            for i, label in enumerate(labels):
                plt.annotate(label, self.path[i+1])
            plt.scatter([x for x, y in self.path], [y for _, y in self.path], label='Wheat')
            plt.scatter([self.start[0]], [self.start[1]], label='Starting point')
            plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
            plt.gca().invert_yaxis()
            plt.show()
        else:
            print('Empty path')

    
  