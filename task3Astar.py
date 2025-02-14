from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list.get(v, []) 

    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""
        H = {  
            'The': 4,
            'cat': 3,
            'dog': 3,
            'runs': 2,
            'fast': 1
        }
        return H.get(n, 0)  

    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""
        open_list = set([start_node])
        closed_list = set([])

        g = {}  
        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None  
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print("Path does not exist!")
                return None

           
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print("Path found: {}".format(reconst_path))
                total_cost = 0
                for i in range(len(reconst_path) - 1):
                    total_cost += self.edge_cost(reconst_path[i], reconst_path[i+1])

                print("Total cost : {}".format(total_cost))

                return reconst_path

        
            for (m, weight) in self.get_neighbors(n):
              
                if m not in open_list and m in closed_list:
                    continue

               
                tentative_g = g[n] + weight

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = tentative_g
                else:
                    if tentative_g >= g.get(m, float('inf')):
                        continue

                    parents[m] = n
                    g[m] = tentative_g

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None

    def edge_cost(self, node1, node2):
        """Returns the cost of the edge between node1 and node2."""
        neighbors = self.get_neighbors(node1)
        for neighbor, weight in neighbors:
            if neighbor == node2:
                return weight
        return float('inf')  
    

adjacency_list = {
    'The': [('cat', 2), ('dog', 3)],
    'cat': [('runs', 2)],
    'dog': [('runs', 4)],
    'runs': [('fast', 1)],
    'fast': []
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('The', 'fast')
