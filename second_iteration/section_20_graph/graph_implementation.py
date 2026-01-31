class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            pairs = self.adj_list[vertex]
            while pairs:
                self.remove_edge(pairs[0], vertex)
            del self.adj_list[vertex]
            return True
        return False


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


g = Graph()

a = "A"
b = "B"
c = "C"
d = "D"

g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)

g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(a, d)
g.add_edge(b, d)
g.add_edge(c, d)

g.remove_vertex(d)

g.print_graph()