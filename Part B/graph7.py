import networkx as nx


def Graph():
    G = nx.Graph()

    k = 30

    for i in range(1, 2 * k + 2):
        G.add_node(i)

    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(1, 3)

    for i in range(2, k + 1):
        G.add_edge(2 * i - 2, 2 * i)
        G.add_edge(2 * i - 1, 2 * i)
        G.add_edge(2 * i - 1, 2 * i + 1)
        G.add_edge(2 * i, 2 * i + 1)

    G.add_nodes_from(G.nodes(), color='never coloured')
    G.add_nodes_from(G.nodes(), label=-1)
    G.add_nodes_from(G.nodes(), visited='no')

    return G
