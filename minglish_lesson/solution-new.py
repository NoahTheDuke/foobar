from itertools import islice
from collections import deque

class Vertex(object):
    def __init__(self, key):
        #self.id
        self.key = key
        #self.connectedTo
        self.edges = []

    #def addNeighbor
    def add_edge(self, edge):
        self.edges.append(edge)

    #def getConnections
    def get_edges(self):
        return self.edges.keys()

    #def getId
    def get_key(self):
        return self.key

    def __str__(self):
        return str(self.key) + ' connected to ' + str([x.key for x in self.edges])

    def __repr__(self):
        return "Edge: {}".format(', '.join(map(str, self.edges)))

class Graph(object):
    def __init__(self):
        #self.vertList
        self.vertices = {}

    #def addEdge
    def add_edge(self, vert, edge):
        if vert not in self.vertices:
            self.add_vertex(vert)
        if edge not in self.vertices:
            self.add_vertex(edge)
        self.vertices[vert].add_neighbor(self.vertices[edge])

    #def addVertex
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def get(self, key):
        return self.__getitem__(key)

    #def getVertices
    def get_vertices(self):
        return self.vertices.iteritems()

    #def getVertex
    def get_vertex(self, key):
        return self.vertices.get(key) if key in self.vertices.keys() else None

    def __contains__(self, item):
        return item in self.vertices

    def __getitem__(self, key):
        return self.vertices.get(key, None)

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        temp = []
        for x in self.vertices.items():
            temp.append(str('Vertex: {}'.format(x)))
        return '\n'.join(temp)

def answer(words):
    return find_alphabet(build_graph(words))

def build_graph(words):
    graph = Graph()

    for x, y in zip(*(islice(words, i, None) for i in range(2))):
        for letter in set(list(x) + list(y)):
            if not graph[letter]:
                graph.add_vertex(letter)

        vertex, edge = get_edge(x, y)
        if vertex and edge:
            graph[vertex].edges.append(edge)
    return graph

def get_edge(x, y):
    max_length = min(map(len, [x, y]))
    for _x, _y in zip(x[:max_length], y[:max_length]):
        if _x != _y:
             return _x, _y
    return None, None

def find_alphabet(graph):
    def visit(node):
        if node in temp:
            raise Exception("Not a directed acyclic graph.")
        if node not in visited:
            temp.add(node)
            for edge in graph[node].edges:
                visit(edge)
            visited.add(node)
            temp.remove(node)
            alphabet.appendleft(node)

    alphabet = deque()
    temp = set()
    visited = set()

    for node, edge in graph.get_vertices():
        if node not in visited:
            visit(node)

    return ''.join(list(alphabet))

def main():
    print(answer(['c', 'cac', 'cb', 'bcc', 'ba']))
    print(answer(["y", "z", "xy"]))
    print(answer(["z", "yx", "yz"]))


if __name__ == '__main__':
    main()
