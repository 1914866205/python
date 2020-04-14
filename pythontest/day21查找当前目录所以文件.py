"""
查找当前目录所有文件
"""
from pyecharts.charts import Pie
from pyecharts import options as opts
import os
txt_numbers = 0
json_numbers = 0
jpg_numbers = 0
png_numbers = 0
csv_numbers = 0
html_numbers = 0


def get_all(cwd):
    result = []
    # 遍历当前目录，获取文件列表
    get_dir = os.listdir(cwd)
    # print(get_dir):
    for i in get_dir:
        # 第一步获取的文件加入路径
        print(i)
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)

            # 取出字符串点以后的字符串
            if file_name.split(".")[-1] == 'txt':
                global txt_numbers
                txt_numbers += 1
            elif file_name.split(".")[-1] == 'json':
                global json_numbers
                json_numbers += 1
            elif file_name.split(".")[-1] == 'csv':
                global csv_numbers
                csv_numbers += 1
            elif file_name.split(".")[-1] == 'jpg':
                global jpg_numbers
                jpg_numbers += 1
            elif file_name.split(".")[-1] == 'png':
                global png_numbers
                png_numbers += 1
            elif file_name.split(".")[-1] == 'html':
                global html_numbers
                html_numbers += 1
            result.append(file_name)
    return result


def drawPie(txt, json, csv, jpg, png, html):
    x_data = ["txt", "json", "csv", "jpg", "png", "html"]
    y_data = [txt, json, csv, jpg, png, html]
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])
    (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px",
                                    bg_color="#2c343c"))

        .add(
            series_name="访问来源",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center")
        )

        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Customized Pie",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a}<br/>{b}:{c}({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255,255,255,0.3)"),
        )
        .render("./res/测试饼状图.html")
    )


if __name__ == "__main__":
    # 取得当前目录:/home/ntt/python-learning,拼上子目录
    cur_path = os.getcwd()+'/res'
    print(cur_path)
    print("*************************")
    # 调用函数，统计res目录下的文件
    print('当前目录的所有文件', get_all(cur_path))
    print("txt数目为：", txt_numbers)
    print("json数目为：", json_numbers)
    print("csv数目为：", csv_numbers)
    print("jpg数目为：", jpg_numbers)
    print("png数目为：", png_numbers)
    print("html数目为：", html_numbers)
    drawPie(txt_numbers,
            json_numbers,
            csv_numbers,
            jpg_numbers,
            png_numbers,
            html_numbers)
