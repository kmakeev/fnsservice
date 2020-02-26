# -*- coding: utf-8 -*-
from bokeh.io import show, output_file

from fnsservice.fns.views import DublicatedGraph

g = DublicatedGraph(width=800, height=800, N=1500)
p = g.get_graph()

output_file("graph.html")
show(p)



