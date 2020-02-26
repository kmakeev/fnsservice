# -*- coding: utf-8 -*-
from bokeh.models import HoverTool
from bokeh.plotting import figure, show, output_file, ColumnDataSource
import pandas as pd
from bokeh.models import WheelZoomTool, PanTool

colormap = ["green", "blue", "magenta", "olive", "red", "brown", "yellow", "cyan", "pink", "blue", "black", "silver", "teal", "tomato",
              "gray", "darkred", "aqua",]

data = pd.read_csv('terminated.csv', dtype={'Capital': float, 'Addr': int}, sep=',', parse_dates=['Start_date', 'End_date'])[0:500]

# print(data.info(), type(data))
# filter = data[data['Start_date'] > '2010-01-01']
# print(type(filter))
# print(filter.iloc[0])
# print(filter.iloc[0]['Start_date'])
# print((filter.iloc[0]['End_date'] - filter.iloc[0]['Start_date']).days)
data['Days'] = (data['End_date'] - data['Start_date']).dt.days
print(data[data['Days'] < 10].count())
print(data[(data['Days'] >= 10) & (data['Days'] < 100)].count())
print(data[(data['Days'] >= 100) & (data['Days'] < 356)].count())
print(data[(data['Days'] >= 356) & (data['Days'] < 1000)].count())
print(data[(data['Days'] >= 1000) & (data['Days'] < 1500)].count())
print(data[(data['Days'] >= 1500) & (data['Days'] < 3000)].count())
print(data[(data['Days'] >= 3000) & (data['Days'] < 6000)].count())
print(data[data['Days'] >= 6000].count())
colors = []
for x in data['Addr']:
    if int(x) == 77:
        colors.append(colormap[1])
    elif int(x) == 63:
        colors.append(colormap[2])
    elif int(x) == 64:
        colors.append(colormap[3])
    elif int(x) == 66:
        colors.append(colormap[4])
    elif int(x) == 24:
        colors.append(colormap[5])
    elif int(x) == 16:
        colors.append(colormap[6])
    else:
        colors.append(colormap[10])

source = ColumnDataSource(data=dict(
    x=data["Days"],
    y=data["Capital"],
    End_date=data['End_date'],
    Start_date=data['Start_date'],
    capital=data['Capital'],
    color=colors,
    ogrn=data["OGRN"],
    desc=data["Name"],
))

hover = HoverTool(tooltips=[
    ("index", "$index"),
    # ("(day, cap)", "($x, $y)"),
    ("OGRN", "@ogrn"),
    ("desc", "@desc"),

    #("fill color", "$color[hex, swatch]:fill_color"),
])

TOOLS = "hover,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(title="Деятельность ЮЛ прекращена", plot_width=1200, plot_height=1200, y_range=(0, 1000000),
           toolbar_location="below", tools=[hover])
p.add_tools(WheelZoomTool())
p.add_tools(PanTool())
p.xaxis.axis_label = 'Период деятельности (в днях)'
p.yaxis.axis_label = 'Сумма уставного капитала'

p.circle(x='x', y='y', color='color', size=10, alpha=0.5,  source=source)

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



