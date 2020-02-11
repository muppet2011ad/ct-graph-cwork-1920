import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G, i):
    # n = len(G.nodes())
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

    print()
    for i in G.nodes():
        G.nodes[i]['colour'] = find_smallest_colour(G, i)
        print('vertex', i, ': colour', G.nodes[i]['colour'])
        if G.nodes[i]["colour"] > kmax:
            kmax = G.nodes[i]["colour"]
    print()
    print('The number of colours that Greedy computed is:', kmax)


print('Graph G1:')
G = graph1.Graph()
greedy(G)

print('Graph G2:')
G = graph2.Graph()
greedy(G)

print('Graph G3:')
G = graph3.Graph()
greedy(G)

print('Graph G4:')
G = graph4.Graph()
greedy(G)

print('Graph G5:')
G = graph5.Graph()
greedy(G)
