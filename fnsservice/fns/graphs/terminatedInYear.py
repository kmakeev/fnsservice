import pandas as pd
from bokeh.models import HoverTool
from bokeh.models import WheelZoomTool, PanTool
from bokeh.plotting import figure, ColumnDataSource

from .colors import colormap


class TerminatedInYearGraph:

    def __init__(self, filename='terminated.csv',  width=300, height=300):
        self.width = width
        self.height = height
        self.colormap = colormap

        self.data = pd.read_csv('terminated.csv', dtype={'Capital': float, 'Addr': int}, sep=',',
                           parse_dates=['Start_date', 'End_date'])

        self.data['Years'] = (self.data['End_date'] - self.data['Start_date']).astype('timedelta64[Y]')
        self.count = self.data['Years'].count()

    def get_graph(self):
        allocation = []
        MAX_ALLOCATION = 15
        data = self.data
        c = self.count
        for i in range(MAX_ALLOCATION):
            allocation.append(len(data[data['Years'] == i]))
        allocation.append(len(data[data['Years'] >= MAX_ALLOCATION]))
        size = pd.Series([i * 2000 / c for i in allocation])
        colors = pd.Series(self.colormap[0:MAX_ALLOCATION + 1])
        source = ColumnDataSource(data=dict(
            x=[i for i in range(MAX_ALLOCATION + 1)],
            top=size,
            color=colors,
            desc=allocation,
            size=size,
        ))

        hover = HoverTool(tooltips=[
            ("Год деятельности", "$index"),
            ("Прекратило деятельность ЮЛ", "@desc"),
        ])

        p = figure(plot_width=self.width, plot_height=self.height, x_axis_type=None, y_axis_type=None,
                   min_border=0, outline_line_color="white", tools=[hover])
        p.add_tools(WheelZoomTool())
        p.add_tools(PanTool())
        p.xaxis.axis_label = 'Продолжительность деятельности в годах'
        p.yaxis.axis_label = ''
        p.vbar(x='x', width=0.9, top='top', bottom=0, color='color', source=source)

        return p
