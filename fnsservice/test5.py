# -*- coding: utf-8 -*-
import math
import pandas as pd
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
import networkx as nx
from bokeh.models.graphs import from_networkx

colormap = ["green", "blue", "magenta", "olive", "red", "brown", "yellow", "cyan", "pink", "blue", "black", "silver",
            "teal", "tomato", "green", "blue", "magenta", "olive", "red", "brown", "yellow", "cyan", "pink", "blue", "black", "silver",
            "gray", "darkred", "aqua", "darkred", "moccasin", "darkkhaki", "lime", "skyblue", ]

N = 500

d = pd.read_csv('dublicate.csv', sep=',')
data = d.sort_values(by='Quantity', ascending=False)[:N]
# print(data.head())
# start = pd.Series(pd.Series.unique(data['Start']))
start = data['Start']
end = data['End']
# print(end)
# print(start)
node_indices = end.append(pd.Series(pd.Series.unique(data['Start'])), ignore_index=True)
edges = zip(start, end)
# print(edges)
G = nx.Graph()
G.add_nodes_from(node_indices)
G.add_edges_from(edges)
plot = figure(title="Networkx Integration Demonstration", x_range=(-3.1, 3.1), y_range=(-3.1, 3.1))

graph = from_networkx(G, nx.spring_layout, scale=2, center=(0, 0))
plot.renderers.append(graph)

output_file("networkx_graph.html")
show(plot)

"""
y = []
x = []
node_indices = start.append(end, ignore_index=True)
print(node_indices)
for i in range(len(node_indices)//10):
    y = y + [200 - 3 - i] * 10
    x = x + [3 + i for i in range(80)]
y = y + [10 - 3 - len(node_indices)//10]*(len(node_indices) % 10)
x = x + [3 + i for i in range(len(node_indices) % 10)]

# print(node_indices)
plot = figure(title="Test Graph of Dublicate", x_range=(0, 100), y_range=(0, 100))

graph = GraphRenderer()

graph.node_renderer.glyph = Oval(height=0.5, width=0.5, fill_color="gray")
graph.node_renderer.data_source.data = dict(
    index=node_indices)

graph.edge_renderer.data_source.data = dict(
    start=data['Start'],
    end=data['End'])

### start of layout code

# print(zip(x, y))
# print(dict(zip(node_indices.tolist(), zip(x, y))))
graph_layout = dict(zip(node_indices.tolist(), zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file("graph.html")
show(plot)
"""


