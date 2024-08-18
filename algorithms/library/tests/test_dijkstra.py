from library.model.graphs.sparse import *
from library.model.heap import *
from library.apply.graph.dijkstra import *


def test_shortest_path(flights):
    cloud = shortest_path(flights, flights["BWI"])

    assert cloud['LAX'] == 2658


def test_build_shortest_path_tree(flights):
    cloud = shortest_path(flights, flights["BWI"])
    tree = build_shortest_path_tree(flights, flights["BWI"], cloud)

    parent = tree['LAX'].origin
    path = ['LAX']

    while parent:
        path.append(parent.uid)
        if parent.uid in tree:
            parent = tree[parent.uid].origin
        else:
            break

    assert path[-1::-1] == ['BWI', 'ORD', 'DFW', 'LAX']
