from pyecharts import options as opts
from pyecharts.charts import Radar

v1 = [[60, 40, 53, 42, 51, 49]]
v2 = [[95, 85, 130, 0, 92, 87]]
v3 = [[99, 99, 99, 99, 99, 99]]
c = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="Bhop", max_=100),
            opts.RadarIndicatorItem(name="Combo", max_=100),
            opts.RadarIndicatorItem(name="加速", max_=100),
            opts.RadarIndicatorItem(name='智商', max_=100),
            opts.RadarIndicatorItem(name="滑坡", max_=100),
            opts.RadarIndicatorItem(name="梯子", max_=100),
        ]
    )
    .add("Exa", v1, color='blue')
    .add("gus", v2, color='green')
    .add("FrozeEnd", v3, color='purple')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        legend_opts=opts.LegendOpts(selected_mode="multi"),
        title_opts=opts.TitleOpts(title="Radar-单例模式"),
    )
    .render("radar_selected_mode.html")
)
