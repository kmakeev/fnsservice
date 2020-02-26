import numpy as np
import pandas as pd
from bokeh.models import HoverTool
from bokeh.models import WheelZoomTool, PanTool
from bokeh.plotting import figure,  ColumnDataSource
from .colors import colormap


class TerminatedGraph:

    def __init__(self, filename='states.csv',  width=300, height=300):
        self.width = width
        self.height = height
        self.colormap = colormap

        self.data = pd.read_csv(filename, dtype={'States': int, 'State_names': str, 'Counts': int},
                           sep=',').sort_values('Counts', ascending=False)
        self.summ = self.data.Counts.sum()

    def get_graph(self):

        summ = self.summ
        data = self.data
        angles = [i / summ * 2 * np.pi for i in data.Counts]
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
            color=self.colormap[0:len(data.States)],
            desc=data['State_names'],
        ))

        hover = HoverTool(tooltips=[
            ("Состояние", "@desc"),
        ])

        width = self.width
        height = self.height
        inner_radius = self.width/150
        outer_radius = self.width/2 - self.width/60
        p = figure(plot_width=width, plot_height=height,
                   x_axis_type=None, y_axis_type=None,
                   x_range=(-self.width/2, self.width/2), y_range=(-self.width/2, self.width/2),
                   min_border=0, outline_line_color="white", tools=[hover])
        p.add_tools(WheelZoomTool())
        p.add_tools(PanTool())

        p.annular_wedge(0, 10, inner_radius, outer_radius, alpha=0.6, start_angle='start_angles',
                        end_angle='end_angles', color='color', source=source)

        p.xgrid.grid_line_color = None
        p.ygrid.grid_line_color = None

        return p
