# -*- coding: utf-8 -*-
from bokeh.models import HoverTool
from bokeh.plotting import figure, show, output_file, ColumnDataSource
import pandas as pd
import numpy as np
from bokeh.models import WheelZoomTool, PanTool
from bokeh.colors import named as named_color

print(named_color)

colormap = ["green", "blue", "magenta", "olive", "red", "brown", "yellow", "cyan", "pink", "blue", "black", "silver", "teal", "tomato",
              "gray", "darkred", "aqua", "darkred", "moccasin", "darkkhaki", "lime", "skyblue", ]

data = pd.read_csv('terminated.csv', dtype={'Capital': float, 'Addr': int}, sep=',', parse_dates=['Start_date', 'End_date'])

# print(data.info(), type(data))
# filter = data[data['Start_date'] > '2010-01-01']
# print(type(filter))
# print(filter.iloc[0])
# print(filter.iloc[0]['Start_date'])
# print((filter.iloc[0]['End_date'] - filter.iloc[0]['Start_date']).days)
# data['Days'] = (data['End_date'] - data['Start_date']).dt.days
data['Years'] = (data['End_date'] - data['Start_date']).astype('timedelta64[Y]')
c = data['Years'].count()
allocation = []
MAX_ALLOCATION = 15
for i in range(MAX_ALLOCATION):
    allocation.append(len(data[data['Years'] == i]))
allocation.append(len(data[data['Years'] >= MAX_ALLOCATION]))
size = pd.Series([i * 2000 / c for i in allocation])
colors = pd.Series(colormap[0:MAX_ALLOCATION+1])
"""
less_10_day = len(data[data['Days'] < 10])
less_100_day = len(data[(data['Days'] >= 10) & (data['Days'] < 100)])
less_356_day = len(data[(data['Days'] >= 100) & (data['Days'] < 356)])
less_1000_day = len(data[(data['Days'] >= 356) & (data['Days'] < 1000)])
less_1500_day = len(data[(data['Days'] >= 1000) & (data['Days'] < 1500)])
less_3000_day = len(data[(data['Days'] >= 1500) & (data['Days'] < 3000)])
less_5000_day = len(data[(data['Days'] >= 3000) & (data['Days'] < 5000)])
more_5000_day = len(data[data['Days'] >= 5000])
allocation = pd.Series([less_10_day, less_100_day, less_356_day, less_1000_day, less_1500_day, less_3000_day, less_5000_day, more_5000_day])
"""

source = ColumnDataSource(data=dict(
    x=[i for i in range(MAX_ALLOCATION+1)],
    # y=[1 for i in range(MAX_ALLOCATION+1)],
    top=size,
    color=colors,
    desc=allocation,
    size=size,
))

hover = HoverTool(tooltips=[
    ("Год деятельности", "$index"),
    ("Прекратило существование ЮЛ", "@desc"),
])


p = figure(title="Деятельность ЮЛ прекращена", plot_width=1200, plot_height=1200,
           toolbar_location="below", tools=[hover])
p.add_tools(WheelZoomTool())
p.add_tools(PanTool())
p.xaxis.axis_label = 'Продолжительность деятельности в годах'
p.yaxis.axis_label = ''

p.vbar(x='x', width=0.9,  top='top', bottom=0, color='color',  source=source)

output_file("term.html", title="Terminated file")

show(p)

"""
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


i_color = 0
width = 800
height = 800
inner_radius = 30
outer_radius = 400 - 30
p = figure(plot_width=width, plot_height=height,
           x_axis_type=None, y_axis_type=None,
           x_range=(-400, 400), y_range=(-400, 400),
           min_border=0, outline_line_color="white")
p.annular_wedge(0, 30, inner_radius, outer_radius,
                start_angle=start_angles, end_angle=end_angles, color=colors[0:len(data.States)], alpha=0.6)
x = [-380 for x in range(len(angles))]
y = [-250 - x*10 for x in range(len(angles))]
p.circle(x, y, color=colors[0:len(data.States)], radius=3)
p.text([i + 15 for i in x], [i for i in y], text=data.State_names,
       text_font_size="7pt", text_align="left", text_baseline="middle")

# legend=item["legend"] + " - " + str(item["count"]))

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.title.align = "center"
show(p)

"""



