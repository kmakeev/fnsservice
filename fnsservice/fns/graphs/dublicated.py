from bokeh.plotting import figure
import pandas as pd
import networkx as nx
from bokeh.models import Circle,  MultiLine, WheelZoomTool, PanTool, HoverTool, TapTool, BoxSelectTool
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes

class DublicatedGraph:

    def __init__(self, filename='dublicate.csv', N=500,  width=300, height=300):
        self.width = width
        self.height = height
        self.N = N

        d = pd.read_csv(filename, sep=',')[:N]
        #self.data = d.sort_values(by='Quantity', ascending=False)[:N]
        self.data = d.sort_values(by='Quantity', ascending=False)

    def get_graph(self):

        start = self.data['Start']
        end = self.data['End']
        fl = self.data['Index']
        fio = self.data['FIO']
        node_indices = end.append(pd.Series(pd.Series.unique(self.data['Start'])), ignore_index=True)
        #fl = pd.Series.unique(self.data['Index'])
        #fl = self.data['Index']
        #edges = zip(start, end)
        edges =[]
        for i in range(len(start)):
                edges.append(tuple([start[i], end[i], {'OGRNIP': str(fl[i]) + " - " + str(fio[i])}]))
        G = nx.Graph()
        G.add_nodes_from(node_indices)
        G.add_edges_from(edges)
        #print(G.adj.items())
        #print(G.edges.data())
        ogrns =[]
        for item in G.edges.data():
            #print(item[2]['OGRNIP'])
            ogrns.append(item[2]['OGRNIP'])
        tooltips=[
            #("index", "$index"),
            #("(x,y)", "($x, $y)"),
            ("1 - ОГРН", "@start"),
            ("2 - ОГРН", "@end"),
            ("ФЛ", "@OGRNIP"),
            #("Моя подсказка", "@end"),
        ]
        # hover = HoverTool(tooltips=tooltips)

        p = figure(plot_width=self.width, plot_height=self.height, x_range=(-3.1, 3.1), y_range=(-3.1, 3.1),
                   x_axis_type=None, y_axis_type=None, tools=[],
                   min_border=0, outline_line_color="white")

        # p.add_tools(WheelZoomTool())
        # p.add_tools(PanTool())
        p.add_tools(HoverTool(tooltips=tooltips), TapTool(), BoxSelectTool(), WheelZoomTool(), PanTool())

        #graph = from_networkx(G, nx.circular_layout, scale=1, center=(0, 0))
        graph = from_networkx(G, nx.spring_layout, scale=2, center=(0, 0))
        graph.node_renderer.glyph = Circle(size=5, fill_color="gray")
        graph.node_renderer.hover_glyph = Circle(size=5, fill_color="red")
        graph.node_renderer.selection_glyph = Circle(size=5, fill_color="green")

        graph.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=1)
        graph.edge_renderer.selection_glyph = MultiLine(line_color="gray", line_width=1)
        graph.edge_renderer.hover_glyph = MultiLine(line_color="gray", line_width=1)

        graph.selection_policy = NodesAndLinkedEdges()
        graph.inspection_policy = EdgesAndLinkedNodes()
        # print(graph.node_renderer.data_source.data)
        # print(graph.edge_renderer.data_source.data)
        graph.edge_renderer.data_source.data['OGRNIP'] = ogrns
        #print(graph.edge_renderer.data_source.data)
        #print(graph.node_renderer.data_source.data)
        p.renderers.append(graph)

        return p
