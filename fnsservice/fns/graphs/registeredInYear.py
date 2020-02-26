import numpy as np
import pandas as pd
from bokeh.models import HoverTool
from bokeh.models import WheelZoomTool, PanTool
from bokeh.plotting import figure,  ColumnDataSource

from .colors import colormap


class RegisteredInYearGraph:

    def __init__(self, filename='registered.csv', width=300, height=300):
        self.width = width
        self.height = height
        #self.colormap = colormap

        self.data = pd.read_csv(filename, sep=',', dtype={'Register_years': int, 'Counts': int, 'Counts_together': int})
        self.count = self.data['Register_years'].count()

    def get_graph(self):
        c = self.count

        size = pd.Series([i * 2000 / c for i in self.data['Counts']])
        #colors = pd.Series(self.colormap[0:len(self.data['Counts'])])
        source = ColumnDataSource(data=dict(
            x=[i for i in range(len(self.data['Counts']))],
            y=self.data['Counts'],
            top=size,
            #color=colors,
            year=self.data['Register_years'],
            y2=self.data['Counts'] + self.data['Counts_together'],
            size=size,
        ))

        hover = HoverTool(tooltips=[
            ("Год регистрации - ", "@year"),
            ("Зарегистрировано новых ЮЛ - ", "@y"),
            ("Зарегистрировано ЮЛ с учетом созданных до 01.07.2002, а также по законодательству Украины  - ", "@y2"),
        ])

        p = figure(plot_width=self.width, plot_height=self.height, x_axis_type=None, y_axis_type=None,
                   min_border=0, outline_line_color="white", tools=[hover])
        p.add_tools(WheelZoomTool())
        p.add_tools(PanTool())
        p.xaxis.axis_label = 'Регистриция новых ЮЛ по годам'
        p.yaxis.axis_label = ''
        #p.vbar(x='x', width=0.9, top='top', bottom=0, color='color', source=source)
        p.line(x='x', y='y', color="dimgray", line_width=2,  source=source)
        p.circle(x='x', y='y', fill_color="white", size=4, source=source)
        p.line(x='x', y='y2', color="darkred", line_width=2, source=source)
        p.circle(x='x', y='y2', fill_color="white", size=4, source=source)
        return p
