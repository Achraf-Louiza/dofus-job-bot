import numpy as np
import matplotlib.pyplot as plt


class Pathfinder:
    """
    A class representing that optimizes bot routes with Manhatan Distance Shortest Path
    
    """
    def __init__(self):
        self.coords_debug=[]
        self.path_debug=[]
    
    def _manhattan_dist(self, a: list, b: list) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _nearest_neighbor(self, coords: list) -> list:
        visited = [False] * len(coords)
        path = [0] * len(coords)
        current = 0
        visited[current] = True
        self.coords_debug=coords[current]
        for i in range(1, len(coords)):
            nearest_dist = float('inf')
            nearest_index = -1
            for j in range(len(coords)):
                if not visited[j]:
                    dist = self._manhattan_dist(coords[current], coords[j])
                    if dist < nearest_dist:
                        nearest_dist = dist
                        nearest_index = j
            visited[nearest_index] = True
            path[i] = nearest_index
            current = nearest_index
            self.path_debug=[coords[i] for i in path]
        return [coords[i] for i in path]
    
    def _grid(self)-> list: 
        min_x = np.min(np.array(self.path_debug), axis=0)[0]
        min_y = np.min(np.array(self.path_debug), axis=0)[1]
        max_x = np.max(np.array(self.path_debug), axis=0)[0]
        max_y = np.max(np.array(self.path_debug), axis=0)[1]
        grid = [[x, y] for y in range(min_y, max_y+1) for x in range(min_x, max_x+1)]
        return [x for x, _ in grid], [y for _, y in grid]

    def plot_grid(self):
        my_grid=self._grid(self.path_debug)
        plt.scatter(my_grid[0], my_grid[1], label='No Wheat')
        labels = range(1, len(self.path_debug))
        for i, label in enumerate(labels):
            plt.annotate(label, self.path_debug[i+1])
        plt.scatter([x for x, y in self.path_debug], [y for _, y in self.path_debug], label='Wheat')
        plt.scatter([self.coords_debug[0]], [self.coords_debug[1]], label='Starting point')
        plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
        plt.gca().invert_yaxis()
        plt.show()

    def shortest_path_nearest_neighbors(self, start: list, destination_coordinates:list) -> list:
        return self._nearest_neighbor([start]+destination_coordinates)