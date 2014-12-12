import sys
from random import randint


def MatrixFactory(n, m=None):
    if not m:
        m = n
    return [[0 for c in range(n)] for r in range(m)]


class Graph(object):

    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.order = len(v)
        self.size = len(e)
        self.matrix = MatrixFactory(len(v))
        for r, c in e:
            self.matrix[r][c] = 1
            self.matrix[c][r] = 1

    def adjacent(self, v1, v2):
        if v1 == v2:
            return 0
        return self.matrix[v1][v2]

    def __str__(self):
        rv = '\n'.join([', '.join([str(r) for r in row]) for row in self.matrix]) 
        return rv


class AssocGraph(Graph):
    
    def __init__(self, g1, g2):
        self.order = g1.order * g2.order
        self.v = [(a, b) for a in range(g1.order) for b in range(g2.order)]
        print self.v
        self.matrix = MatrixFactory(self.order)
        for i1, v1 in enumerate(self.v):
            for i2, v2 in enumerate(self.v):
                if i1 == i2:
                    continue
                if g1.adjacent(v1[0], v2[0]) and g2.adjacent(v1[1], v2[1]):
                    self.matrix[i1][i2] = 1
                elif not g1.adjacent(v1[0], v2[0]) and not g2.adjacent(v1[1], v2[1]):
                    self.matrix[i1][i2] = 1
                else:
                    self.matrix[i1][i2] = 0


if __name__ == "__main__":
    nodes = 3
    edges = 2

    g1 = Graph([0 for x in range(nodes)], [(randint(0,nodes-1), randint(0, nodes-1)) for x in range(edges)])
    g2 = Graph([0 for x in range(nodes)], [(randint(0,nodes-1), randint(0, nodes-1)) for x in range(edges)])

    g1 = Graph([0, 1, 2], [(0,1), (1,2)])
    g2 = Graph([0, 1, 2], [(0,1), (1,2)])

    ag = AssocGraph(g1, g2)
    
    sys.stdout.write("%s\n\n%s\n\n%s\n" % (g1, g2, ag))
