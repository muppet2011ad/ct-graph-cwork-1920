import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    global available
    next = min(available)
    available.remove(next)
    G.nodes[next]["visited"] = "yes"
    available = available | set([n for n in G[next] if G.nodes[n]["visited"] == "no"])
    return next


def find_smallest_colour(G, i):
    neighbour_colours = set()
    for x in G[i]:
        if G.nodes[x]["colour"] != "never coloured":
            neighbour_colours.add(G.nodes[x]["colour"])
    smol = 1
    while smol in neighbour_colours:
        smol += 1
    return smol


def greedy(G):
    kmax = 0
    global visited_counter
    global available
    available = {1}

    while len(available) > 0:
        node = find_next_vertex(G)
        G.nodes[node]['colour'] = find_smallest_colour(G, node)

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
        if G.nodes[i]["colour"] > kmax:
            kmax = G.nodes[i]["colour"]
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()


print('Graph G1:')
G = graph1.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)

print('Graph G2:')
G = graph2.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)

print('Graph G3:')
G = graph3.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)

print('Graph G4:')
G = graph4.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)

print('Graph G5:')
G = graph5.Graph()
G.add_nodes_from(G.nodes(), visited='no')
greedy(G)
