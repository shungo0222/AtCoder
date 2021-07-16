from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

class DAG(object):
    """
    Graph is represented using adjacency list. Every
    node of adjacency list contains vertex number of
    the vertex to which edge connects. It also contains
    weight of the edge
    
    Parameters
    ----------
    V : int
        number of vertices
    graph : dict
        dictionary containing adjacency list
    topological_sort : list
        sorted vertices list by topological sort
    """
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.topological_sort = []
    
    def addEdge(self, u, v, w):
        """
        function to add an edge to graph
        
        Parameters
        ----------
        u : int
            start point
        v : int
            end point
        w : int or float
            weight
        """
        self.graph[u].append((v, w))
    
    def _topologicalSortUtil(self, v, visited, calculated, stack):
        """A recursive function used by topologicalSort"""
        
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                # visiting the uncalculated vertices twice means that there is a loop
                if visited[node] and not calculated[node]:
                    return -1
                
                if not visited[node]:
                    if self._topologicalSortUtil(node, visited, calculated, stack) == -1:
                        return -1
        
        calculated[v] = True
        
        # Push current vertex to stack which stores result
        stack.append(v)
        
        return None
    
    def topologicalSort(self):
        """
        The function to do Topological Sort. It uses recursive
        _topologicalSortUtil()
        """
        
        # Mark all the vertices as not visited
        visited = [False] * self.V
        
        # Mark all the vertices as not calculated
        calculated = [False] * self.V
        
        # sorted vertices
        stack = []
        
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                if self._topologicalSortUtil(i, visited, calculated, stack) == -1:
                    return -1
        
        # store list in reverse order
        self.topological_sort = stack[::-1]
        
        return None
    
    def getTopologicalSort(self):
        if not self.topological_sort:
            if self.topologicalSort() == -1:
                return -1
        
        return self.topological_sort
    
    def shortestPath(self, s):
        """The function to find shortest paths from given vertex"""
        if not self.topological_sort:
            if self.topologicalSort() == -1:
                return 'There is a loop!!'
        
        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float('inf')] * self.V
        dist[s] = 0
        
        # Process vertices in topological order
        flag = False
        for i in self.topological_sort:
            if i == s:
                flag = True
            if flag:
                # Update distances of all adjacent vertices
                for node, weight in self.graph[i]:
                    if dist[node] > dist[i] + weight:
                        dist[node] = dist[i] + weight
        
        return dist
    
    def longestPath(self, s):
        """The function to find longest paths from given vertex"""
        if not self.topological_sort:
            if self.topologicalSort() == -1:
                return 'There is a loop!!'
        
        dist = [1] * self.V
        
        # Process vertices in topological order
        flag = False
        for i in self.topological_sort:
            if i == s:
                flag = True
            if flag:
                # Update distances of all adjacent vertices
                for node, weight in self.graph[i]:
                    if dist[node] < dist[i] + weight:
                        dist[node] = dist[i] + weight
        
        return dist

def main():
    n = int(input())
    a = [[0]*(n-1) for _ in range(n)]
    id = [[0]*n for _ in range(n)]
    
    v = 0
    for i in range(n-1):
        for j in range(i+1, n):
            id[i][j] = v
            v += 1
    
    g = DAG(n*(n-1)//2)
    
    for i in range(n):
        x = list(map(int, input().split()))
        for j in range(n-1):
            tmp = sorted([i, x[j]-1])
            a[i][j] = id[tmp[0]][tmp[1]]
        for j in range(n-2):
            g.addEdge(a[i][j], a[i][j+1], 1)
    
    x = g.getTopologicalSort()
    if x == -1:
        print(-1)
    else:
        print(max(g.longestPath(x[0])))

if __name__ == '__main__':
    main()