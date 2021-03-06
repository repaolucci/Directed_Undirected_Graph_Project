# Course: CS261 - Data Structures
# Author: Rebecca Paolucci
# Assignment: 6
# Description: Assignment 6 for Summer 2021 CS 261, involving directed graphs.

import heapq
from collections import deque


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        A method that adds a new vertex to the graph.
        """
        # adds list to adjacency matrix and increments v_count
        self.adj_matrix.append([])
        self.v_count += 1

        # fills out each row (list) with 0
        for a_list in self.adj_matrix:
            while len(a_list) < self.v_count:
                a_list.append(0)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        A method that adds a new edge to the graph, connecting the two vertices with the provided
        indices. If either (or both) indices do not exist in the graph, or if the weight is not
        a positive integer, or if src and dst refer to the same vertex, the method does nothing.
        If an edge already exists in the graph, the method will update its weight.
        """
        # checks conditions that do nothing from Docstrings
        if weight < 1:
            return
        if src == dst:
            return
        if src > self.v_count-1 or dst > self.v_count-1:
            return
        if src < 0 or dst < 0:
            return

        # adds vertex at position in matrix
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        A method that removes an edge between two vertices with provided indices.
        If either (or both) vertex indices do not exist in the graph, or if there is no
        edge between them, the method does nothing.
        """
        # checks conditions that do nothing from Docstrings
        if src > self.v_count-1 or dst > self.v_count-1:
            return
        if src < 0 or dst < 0:
            return
        if self.adj_matrix[src][dst] == 0:
            return

        # adds 0 at position in matrix
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns a list of vertices of the graph.
        """
        a_list = []
        for num in range(self.v_count):
            a_list.append(num)
        return a_list

    def get_edges(self) -> []:
        """
        Returns a list of edges in the graph. Each edge is returned as a tuple of two incident
        vertex indices and weight. The first element in the tuple refers to the source vertex.
        The second element in the tuple refers to the destination vertex. The third element in the
        tuple is the weight of the edge.
        """
        # initializes edge list
        edge_list = []

        # iterates through matrix
        for a_list in range(len(self.adj_matrix)):
            for val in range(len(self.adj_matrix)):
                # checks for edge at each position
                if self.adj_matrix[a_list][val] != 0:
                    # assigns weight at edge to wt
                    wt = self.adj_matrix[a_list][val]
                    # adds tuple to edge_list
                    edge_list.append((a_list, val, wt))
        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        A method that takes a list of vertex indices and returns True if the sequence of
        vertices represents a valid path in the graph. An empty path is considered valid.
        """
        # handles empty path
        if path == []:
            return True

        # checks consecutive values for valid edge
        for val in range(len(path)-1):
            if self.adj_matrix[path[val]][path[val+1]] == 0:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        A method that performs a depth-first search in the graph and returns a list of vertices
        visited during the search, in the order they were visited. V_start is the index from which
        the search will start, v_end is an optional parameter for the index of the end vertex
        that will stop the search once it is reached.
        """
        if v_start < 0 or v_start > self.v_count:
            return []

        # initializes empty list of visited vertices and an empty stack
        visited = []
        stack = []
        # returns an empty list if the starting vertex is not in the graph
        if v_start < 0 or v_start > self.v_count:
            return visited

        # adds v_start to stack
        stack.append(v_start)

        if v_end is None:
            while len(stack) > 0:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.append(vertex)
                    # creates temp list that will store neighbors
                    temp = []
                    # adds neighbors to temp
                    for val in range(len(self.adj_matrix[vertex])):
                        if self.adj_matrix[vertex][val] != 0:
                            temp.append(val)
                        # sorts and reverses temp list
                        temp.sort()
                        temp.reverse()
                        # appends values in reverse so that they will be popped in the correct order
                        for num in temp:
                            stack.append(num)
            return visited

        # proceed as if there is no end vertex
        elif v_end < 0 or v_end > self.v_count:
            while len(stack) > 0:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.append(vertex)
                    # creates temp list that will store neighbors
                    temp = []
                    # adds neighbors to temp
                    for val in range(len(self.adj_matrix[vertex])):
                        if self.adj_matrix[vertex][val] != 0:
                            temp.append(val)
                    # sorts and reverses temp list
                    temp.sort()
                    temp.reverse()
                    # appends values in reverse so that they will be popped in the correct order
                    for num in temp:
                        stack.append(num)
            return visited

        # v_end exists
        while len(stack) > 0:
            vertex = stack.pop()
            # terminates the search at v_end
            if vertex == v_end:
                visited.append(vertex)
                return visited
            if vertex not in visited:
                visited.append(vertex)
                # creates temp list that will store neighbors
                temp = []
                # adds neighbors to temp
                for val in range(len(self.adj_matrix[vertex])):
                    if self.adj_matrix[vertex][val] != 0:
                        temp.append(val)
                # sorts and reverses temp list
                temp.sort()
                temp.reverse()
                # appends values in reverse so that they will be popped in the correct order
                for num in temp:
                    stack.append(num)
        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        A method that performs a breadth-first search in the graph and returns a list of vertices
        visited during the search, in the order they were visited. V_start is the index from which
        the search will start, v_end is an optional parameter for the index of the end vertex
        that will stop the search once it is reached.
        """

        if v_start < 0 or v_start > self.v_count:
            return []

        # initializes empty list of visited vertices and an empty stack
        visited = []
        queue = []
        # returns an empty list if the starting vertex is not in the graph
        if v_start < 0 or v_start > self.v_count:
            return visited

        # adds v_start to stack
        queue.append(v_start)

        if v_end is None:
            while len(queue) > 0:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.append(vertex)
                    # creates temp list that will store neighbors
                    temp = []
                    # adds neighbors to temp
                    for val in range(len(self.adj_matrix[vertex])):
                        if self.adj_matrix[vertex][val] != 0:
                            temp.append(val)
                        # sorts and reverses temp list
                        temp.sort()
                        # appends values in reverse so that they will be popped in the correct order
                        for num in temp:
                            if num not in visited:
                                queue.append(num)
            return visited

        # proceed as if there is no end vertex
        elif v_end < 0 or v_end > self.v_count:
            while len(queue) > 0:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.append(vertex)
                    # creates temp list that will store neighbors
                    temp = []
                    # adds neighbors to temp
                    for val in range(len(self.adj_matrix[vertex])):
                        if self.adj_matrix[vertex][val] != 0:
                            temp.append(val)
                    # sorts and reverses temp list
                    temp.sort()
                    # appends values in reverse so that they will be popped in the correct order
                    for num in temp:
                        if num not in visited:
                            queue.append(num)
            return visited

        # v_end exists
        while len(queue) > 0:
            vertex = queue.pop(0)
            # terminates the search at v_end
            if vertex == v_end:
                visited.append(vertex)
                return visited
            if vertex not in visited:
                visited.append(vertex)
                # creates temp list that will store neighbors
                temp = []
                # adds neighbors to temp
                for val in range(len(self.adj_matrix[vertex])):
                    if self.adj_matrix[vertex][val] != 0:
                        temp.append(val)
                # sorts and reverses temp list
                temp.sort()
                # appends values in reverse so that they will be popped in the correct order
                for num in temp:
                    if num not in visited:
                        queue.append(num)
        return visited

    def has_cycle(self):
        """
        A method that returns True if graph contains a cycle; False otherwise.
        """
        pass
        if self.v_count == 0:
            return False

        # checks for a cycle between two vertices with edges pointing to each other
        for li in range(self.v_count):
            for col in range(self.v_count):
                if self.adj_matrix[li][col] != 0:
                    if self.adj_matrix[col][li] != 0:
                        return True

        for vertex in range(self.v_count):
            # calls helper cycle_dfs on vertex and returns True if a cycle is found
            if self.cycle_dfs(vertex) is True:
                return True
        return False

    def cycle_dfs(self, v_start):
        """
        Helper method for has_cycle, using DFS algorithm. Returns True if a cycle is found, and
        False otherwise.
        """
        # initializes empty list of visited vertices and an empty stack
        visited = []
        stack = []
        # returns an empty list if the starting vertex is not in the graph
        if v_start < 0 or v_start > self.v_count:
            return visited

        # adds v_start to stack
        stack.append((v_start, None))

        while len(stack) > 0:
            # sets tuple to vertex and parent
            vertex, parent = stack.pop()

            if vertex not in visited:
                visited.append(vertex)
                # creates temp list that will store neighbors
                temp = []
                # adds neighbors to temp
                for val in range(len(self.adj_matrix[vertex])):
                    if self.adj_matrix[vertex][val] != 0:
                        temp.append(val)
                # sorts and reverses temp list
                temp.sort(reverse=True)
                for val in temp:
                    # conditions for cycle
                    if val in visited and val != parent:
                        for h in self.adj_matrix[val]:
                            # must have outgoing edge
                            if h != 0:
                                return True
                    # adds tuple to stack consisting of val and vertex as new parent
                    stack.append((val, vertex))
        return False

    def dijkstra(self, src: int) -> []:
        """
        Implements the Dijkstra algorithm to compute the length of the shortest path from a
        given vertex to all other vertices in the graph. Returns a list with one value per
        each vertex in the graph, where the value at index 0 is the length of the shortest path
        from vertex SRC to vertex 0, the value at index 1 is the length of the shortest path
        from vertex SRC to vertex 1, etc. If a certain vertex is not reachable from SRC, the
        returned value should be infinity. Assumes that SRC is a valid vertex.
        Citation: I consulted a tutor on how to initializing the distances dictionary with each
        value set to float("inf"), as well as the first conditional statement in the while loop.
        """
        # initializes dictionary for distances and sets default distance to float("inf")
        distances = {}
        for num in range(self.v_count):
            distances[num] = float("inf")
        # default at src is 0
        distances[src] = 0

        # initializes an empty priority queue, and insert src into it with distance (priority) 0
        hq = []
        heapq.heappush(hq, (0, src))

        # while the priority queue is not empty
        while len(hq) > 0:
            # Remove the first element (a vertex) from the priority queue and assign it to v
            # Let dist be v???s distance (priority)
            dist, v = heapq.heappop(hq)

            # checks whether dist is less than the current distance
            if dist <= distances[v]:
                for val in range(len(self.adj_matrix[v])):
                    # if there is an edge between v and val
                    if self.adj_matrix[v][val] != 0:
                        # sets new dist_2 variable to dist + weight of current edge
                        dist_2 = dist + self.adj_matrix[v][val]
                        # sets distance to dist_2 if the path is shorter
                        if dist_2 < distances[val]:
                            distances[val] = dist_2
                            # pushes tuple to hq
                            heapq.heappush(hq, (dist_2, val))

        # returns list of shortest paths
        ret_list = []
        for key in distances:
            ret_list.append(distances[key])
        return ret_list

if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
