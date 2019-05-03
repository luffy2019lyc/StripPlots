"""
* date：2019/5/1 0001
* time：下午 6:57
__author__ = "lyc"

读取字符串型json数据画图并保存
图片名称  p_No
Coordinary   边缘点 ficoordinate
solar_R  半径
r  c   横长度  纵长度
x  y   圆心坐标
"""
import numpy as np
from matplotlib import pyplot as plt
import sys

# 文件路径
image_path = './images/'


def plotS(filename, solar_c, solar_R, rc, coordinate):
    """根据文件名，圆心，半径，xy范围， 散点 画图"""
    plt.figure()

    # figsize 设置图形的大小，a 为图形的宽， b 为图形的高，单位为英寸
    # 6.4 inches * 100 dpi = 640 pixels
    plt.figure(figsize=(8, 8))
    plt.axis((0, rc[0]+100, 0, rc[1]+100))

    # 画圆
    theta = np.arange(0, 2 * np.pi + 0.1, 2 * np.pi / 1000)
    x = solar_c[0] - 230 + solar_R * np.cos(theta)
    y = solar_c[1] -230 + solar_R * np.sin(theta)
    plt.plot(x, y, color='black', linewidth=1)

    # 画散点
    plt.scatter(coordinate[:,0], coordinate[:,1], c='blue', s=5)
    # 隐藏坐标轴
    # plt.axis('off')

    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')  # 将x轴的位置设置在顶部
    ax.yaxis.set_ticks_position('left')  # 将y轴的位置设置在右边
    ax.invert_yaxis()  # y轴反向
    # 第二个实参bbox_inches指定图标多余的空白区域裁剪掉
    path_name = image_path + filename
    plt.savefig(path_name, bbox_inches='tight')
    # plt.show()


def main(json_data):
    """根据json数据画图"""
    rows = json_data['rows']
    for row in rows:
        p_No = row['p_No']
        file_name = str(p_No) + '.jpg'
        solar_c = [float(row['x']), float(row['y'])]
        solar_R = float(row['solar_R'])
        rc = [float(row['r']), float(row['c'])]
        coordinate = np.array(eval(row['ficoordinate']))
        plotS(file_name, solar_c, solar_R, rc, coordinate)

    print('画图已保存')


if __name__ == '__main__':
    json_data = sys.argv[1]
    main(eval(json_data))
