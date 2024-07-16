import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import interp1d

# 创建图形和子图，背景设置为黑色
fig, ax = plt.subplots(facecolor='black')

# 设置坐标轴范围
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)

# 初始化龙卷风参数
num_particles = 200  # 颗粒数量
radius = 1.5  # 颗粒的半径
speed = 0.5  # 旋转速度
angle = 0.0  # 初始角度

# 初始位置在正中间生成一个白色颗粒
x = [0.0]
y = [0.0]
colors = ['white']
sizes = [1.0]

# 创建散点图
scat = ax.scatter(x, y, s=sizes, c=colors, alpha=0.8)

# 定义心形曲线方程
def heart_shape(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# 生成心形曲线的参数
t = np.linspace(0, 2*np.pi, 100)
heart_x, heart_y = heart_shape(t)

# 初始化插值函数
interp_func_x = interp1d(np.arange(len(heart_x)), heart_x, kind='cubic')
interp_func_y = interp1d(np.arange(len(heart_y)), heart_y, kind='cubic')

# 更新函数
def update(frame):
    global x, y, angle
    
    # 更新角度
    angle += speed
    
    # 计算新的位置
    x = x + radius * np.cos(np.radians(angle))
    y = y + radius * np.sin(np.radians(angle))
    
    # 逐步从白色颗粒变成爱心形状
    progress = frame / 180.0  # 根据帧数计算过渡进度
    new_heart_x = interp_func_x(np.arange(len(heart_x)) * progress)
    new_heart_y = interp_func_y(np.arange(len(heart_y)) * progress)
    
    # 更新散点图数据
    scat.set_offsets(np.column_stack((x, y)))
    scat.set_sizes(sizes * (1 - progress) + 5 * progress)  # 调整大小
    scat.set_color(plt.cm.gray(0.5 * (1 - progress)))  # 调整颜色
    
    # 绘制爱心曲线
    ax.plot(new_heart_x, new_heart_y, color='white', alpha=0.5)
    
    return scat,

# 创建动画
ani = animation.FuncAnimation(fig, update, frames=180, interval=50)
plt.show()
