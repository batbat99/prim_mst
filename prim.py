import queue as Q

from graph import *

def prims_mst(g:Graph, start=1):
    w_sum = 0
    pq = Q.PriorityQueue()
    visited = []
    mst = []

    current = start

    while True:
        for edge in g.adj_list[current]:
            if edge[0] not in visited:
                pq.put((edge[1], (current,edge[0])))
        visited.append(current)

        best_edge = pq.get()
        if best_edge[1][1] not in visited:
            w_sum += best_edge[0]
            mst.append(best_edge[1])
            current = best_edge[1][1]



        if len(visited) == g.length:
            break

    return mst



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
    print(prims_mst(g))