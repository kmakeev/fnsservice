# -*- coding: utf-8 -*-

from bokeh.plotting import figure, show, ColumnDataSource
import numpy as np
import pandas as pd
from bokeh.models import HoverTool
from bokeh.models import WheelZoomTool, PanTool


colors = ["green", "blue", "magenta", "olive", "red", "brown", "yellow", "cyan", "pink", "blue", "black", "silver", "teal", "tomato",
              "gray", "darkred", "aqua",]

data = pd.read_csv('states.csv', dtype={'States': int, 'State_names': str, 'Counts': int}, sep=',').sort_values('Counts', ascending=False)
print(data['State_names'])
summ = data.Counts.sum()
color = colors[0:len(data.States)]
angles = [i/summ*2*np.pi for i in data.Counts]
start_angles = []
end_angles = []
end_angle = 2 * np.pi
for i in range(len(angles)):
    end_angles.append(end_angle)
    start_angle = end_angle - angles[i]
    start_angles.append(start_angle)
    end_angle = start_angle

source = ColumnDataSource(data=dict(
    start_angles=start_angles,
    end_angles=end_angles,
    color=colors[0:len(data.States)],
    # count=data.Counts,
    desc=data['State_names'],

))

hover = HoverTool(tooltips=[
    ("Состояние", "@desc"),
])

i_color = 0
width = 800
height = 800
inner_radius = 30
outer_radius = 400 - 30
p = figure(plot_width=width, plot_height=height,
           x_axis_type=None, y_axis_type=None,
           x_range=(-400, 400), y_range=(-400, 400),
           min_border=0, outline_line_color="white", tools=[hover])
p.add_tools(WheelZoomTool())
p.add_tools(PanTool())

p.annular_wedge(0, 30, inner_radius, outer_radius, alpha=0.6, start_angle='start_angles',
                end_angle='end_angles', color='color', source=source)


p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

show(p)



