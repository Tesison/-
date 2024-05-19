import threading
import time

import matplotlib.pyplot as plt
from  matplotlib.animation import  FuncAnimation
import globalVAR
import zlgcan

fig, ax = plt.subplots()
# 构造空线条
line, = ax.plot([], [])
# 构造线条数据结构
xdata, ydata = [], []
# 设置坐标轴刻度范围
ax.set_ylim(-10, 100)
ax.set_xlim(0, 100)

# 动画循环一次后进行初始化，清空数据
def init():
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

# 控制每帧画面如何绘制
def update(x):
    y = globalVAR.get_val("AxleSpeed_1")
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    fig.canvas.draw()
    return line,

if __name__ == "__main__":

    ani = FuncAnimation(fig, update, 100, interval=10, init_func=init)
    plt.show()





#print(globalVAR.get_val('AxleSpeed_1'))


