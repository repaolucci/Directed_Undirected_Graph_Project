# Course: CS 261 - Data Structures
# Author: Rebecca Paolucci
# Assignment: 6
# Description: Assignment 6 for Summer 2021 CS 261, involving undirected graphs.


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        # returns if vertex already exists
        for key in self.adj_list:
            if key == v:
                return

        # adds vertex
        self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if u == v:
            return

        # checks for key in the dictionary and creates the key if not present
        if v not in self.adj_list:
            self.adj_list[v] = []
        # checks for u in the list and adds it to the list if not present
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

        # checks for key in the dictionary and creates the key if not present
        if u not in self.adj_list:
            self.adj_list[u] = []
        # checks for u in the list and adds it to the list if not present
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        # checks for key in the dictionary and returns if not present
        if u not in self.adj_list or v not in self.adj_list:
            return
        # checks for edge and removes if present
        if u in self.adj_list[v] and v in self.adj_list[u]:
            self.adj_list[v].remove(u)
            self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        # returns if vertex does not exist
        if v not in self.adj_list:
            return
        # removes vertex
        del self.adj_list[v]
        # removes associated edges
        for key in self.adj_list:
            if v in self.adj_list[key]:
                self.adj_list[key].remove(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        # creates list
        vertices = []
        # iterates through dictionary to add each vertex to list
        for key in self.adj_list:
            vertices.append(key)
        return vertices

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        # creates list
        edges = []
        # iterates through each key and value
        for key in self.adj_list:
            for value in self.adj_list[key]:
                # ignores duplicates
                if (value, key) not in edges:
                    # adds tuple to list
                    edges.append((key, value))
        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        # empty path is valid
        if len(path) == 0:
            return True
        # handles path of size 1
        if len(path) == 1:
            # checks that vertex exists
            if path[0] not in self.adj_list:
                return False

        # iterates through list and checks for valid edges between consecutive vertices
        for num in range(len(path)-1):
            if path[num] not in self.adj_list[path[num+1]]:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        # initializes empty list of visited vertices and an empty stack
        visited = []
        stack = []
        # returns an empty list if the starting vertex is not in the graph
        if v_start not in self.adj_list:
            return visited

        # adds v_start to stack
        stack.append(v_start)

        # proceed as if there is no end vertex
        if v_end not in self.adj_list or v_end is None:
            while len(stack) > 0:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.append(vertex)
                    # sorts and reverses temp list
                    temp = self.adj_list[vertex]
                    temp.sort()
                    temp.reverse()
                    # appends values in reverse so that they will be popped in the correct order
                    for val in temp:
                        stack.append(val)
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
                # sorts and reverses temp list
                temp = self.adj_list[vertex]
                temp.sort()
                temp.reverse()
                # appends values in reverse so that they will be popped in the correct order
                for val in temp:
                    stack.append(val)
        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        # initializes empty list of visited vertices and an empty queue
        visited = []
        queue = []
        # returns an empty list if the starting vertex is not in the graph
        if v_start not in self.adj_list:
            return visited

        # adds v_start to queue
        queue.append(v_start)

        # proceed as if there is no end vertex
        if v_end not in self.adj_list or v_end is None:
            while len(queue) > 0:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.append(vertex)
                    # sorts temp list
                    temp = self.adj_list[vertex]
                    temp.sort()
                    # appends sorted values so that they will be popped in the correct order
                    for val in temp:
                        if val not in visited:
                            queue.append(val)
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
                # sorts temp list
                temp = self.adj_list[vertex]
                temp.sort()
                # appends sorted values so that they will be popped in the correct order
                for val in temp:
                    if val not in visited:
                        queue.append(val)
        return visited

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        # tracks all visited nodes
        connected = []
        # tracks number of connected components
        count = 0

        for key in self.adj_list:
            # checks whether a vertex has been visited
            if key not in connected:
                count += 1
                temp = self.dfs(key)
                # iterates through vertex's connections
                for val in temp:
                    connected.append(val)
        return count

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """

        # performs DFS on each key to check for a cycle
        for key in self.adj_list:
            # calls helper cycle_dfs on key and returns True if a cycle is found
            if self.cycle_dfs(key) is True:
                return True
        return False

    def cycle_dfs(self, v_start):
        """
        Helper method for has_cycle, using DFS algorithm. Returns True if a cycle is found, and
        False otherwise.
        Citation: I worked with a tutor, who taught me to pass a tuple to the stack
        to track a parent element.
        """
        # initializes empty list of visited vertices and an empty stack
        visited = []
        stack = []
        # returns an empty list if the starting vertex is not in the graph
        if v_start not in self.adj_list:
            return visited

        # adds v_start to stack
        stack.append((v_start, None))

        while len(stack) > 0:
            # sets tuple to vertex and parent
            vertex, parent = stack.pop()

            if vertex not in visited:
                visited.append(vertex)
                # sorts and reverses temp list
                temp = self.adj_list[vertex]
                temp.sort()
                temp.reverse()
                # appends values in reverse so that they will be popped in the correct order
                for val in temp:
                    # conditions for cycle
                    if val in visited and val != parent:
                        return True
                    # adds tuple to stack consisting of val and vertex as new parent
                    stack.append((val, vertex))
        return False


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
