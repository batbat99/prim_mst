class Graph:

    def __init__(self):
        self.adj_list =  {}
        self.length = 0

    def add_vertex(self,v):
        if v not in self.adj_list:
            self.adj_list[v] = []
            self.length += 1
        
    def add_edge(self, v1, v2, weight):
        if v1 in self.adj_list and v2 in self.adj_list:
            temp1  = [v2, weight]
            temp2 = [v1, weight]
            self.adj_list[v1].append(temp1)
            self.adj_list[v2].append(temp2)

    def __str__(self):
        string = ""
        for vertex in self.adj_list:
            for edge in self.adj_list[vertex]:
                string += str(vertex) + " -> " + str(edge[0]) + " edge weight: " + str(edge[1]) + "\n"
        return string


if __name__ == "__main__":
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)

    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 4)
    g.add_edge(4, 1, 5)
    print(g)