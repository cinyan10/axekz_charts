import json

from pyecharts.charts import Map
from pyecharts.options import *

map_data = [
    ("上海市", 42),
    ("云南省", 16),
    ("内蒙古自治区", 10),
    ("北京市", 36),
    ("台湾省", 20),
    ("吉林省", 11),
    ("四川省", 89),
    ("天津市", 26),
    ("宁夏回族自治区", 0),
    ("安徽省", 29),
    ("山东省", 51),
    ("山西省", 17),
    ("广东省", 255),
    ("广西壮族自治区", 36),
    ("新疆维吾尔自治区", 4),
    ("江苏省", 81),
    ("江西省", 25),
    ("河北省", 39),
    ("河南省", 51),
    ("浙江省", 114),
    ("海南省", 4),
    ("湖北省", 55),
    ("湖南省", 44),
    ("澳门特别行政区", 2),
    ("甘肃省", 8),
    ("福建省", 44),
    ("西藏自治区", 1),
    ("贵州省", 21),
    ("辽宁省", 33),
    ("重庆市", 32),
    ("陕西省", 43),
    ("青海省", 1),
    ("香港特别行政区", 46),
    ("黑龙江省", 8),
]

map = Map()

map.add('玩家数量', map_data)

map.set_global_opts(
    title_opts=TitleOpts(title="AXE KZ玩家分布"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=False,
        # pieces=[
        #     {"min": 1, "max": 5, "lable": "1~5人", "color": "#CCFFFF"},
        #     {"min": 6, "max": 10, "lable": "100~9999人", "color": "#FFFF99"},
        #     {"min": 11, "max": 20, "lable": "1000~4999人", "color": "#FF9966"},
        #     {"min": 20, "max": 50, "lable": "5000~99999人", "color": "#FF6666"},
        #     {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
        #     {"min": 100000, "lable": "100000+", "color": "#990033"},
        # ]
    )
)

map.render()

