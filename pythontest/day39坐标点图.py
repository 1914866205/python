from pyecharts.charts import Scatter
import pyecharts.options as opts
from random import uniform


def draw_uniform_options():
    x, y = [i for i in range(100)], [round(uniform(0, 10), 2)
                                     for _ in range(100)]
    print(y)
    c = (Scatter()
         .add_xaxis(x)
         .add_yaxis('y', y))
    c.render()


if __name__ == '__main__':
    draw_uniform_options()
