from pyecharts.charts import Line
from pyecharts.options import *

line = Line()

line.add_xaxis(['2022-12', '2023-1', '2023-2', '2023-3', '2023-4', '2023-5', '2023-6', '2023-7',
                '2023-8', '2023-9', '2023-10', '2023-11', '2023-12'])

line.add_yaxis('新增玩家', [86, 97, 52, 54, 40, 48, 83, 146, 207, 188, 112, 89, 106])
line.add_yaxis('总玩家', [86, 183, 235, 289, 329, 377, 460, 606, 813, 1001, 1113, 1202, 1308])


line.set_global_opts(
    title_opts=TitleOpts(title='AXE Kreedz总游玩人数', pos_left='center', pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    # visualmap_opts=VisualMapOpts(
    #     is_show=False,
    #     pos_left='right',
    # ),
)

line.render()
