import numpy as np
import os
import struct
# import matplotlib.pyplot as plt
import plotly.express as px
# 文件路径
file_path = 'data_PCBfig.bin'
output_path = 'E:/VSCode_test/Pic/DianLuBanFig.html'

# 打开二进制文件
with open(file_path, 'rb') as file:
    # 确定文件大小
    file_size = os.path.getsize(file_path)
    # 确定单个浮点数的字节数
    float_size = struct.calcsize('f')  # 对于32位浮点数
    # 或者 float_size = struct.calcsize('d') # 对于64位浮点数

    # 计算文件中浮点数的数量
    num_floats = file_size // float_size
    float_value = np.zeros(num_floats)

    # 读取并解析浮点数
    for i in range(num_floats):
        # 读取一个浮点数的字节
        bytes = file.read(float_size)
        # 解析浮点数
        float_value[i], = struct.unpack('f', bytes)  # 对于32位浮点数
        # 或者 float_value, = struct.unpack('d', bytes) # 对于64位浮点数

matrix = float_value.reshape(404, 124).T
# 绘制矩阵的热图
fig = px.imshow(-matrix, aspect='auto')  # 使用viridis颜色映射
fig.update_layout(width=400,height=300)
# fig.update_layout(margin=dict(l=0,r=0,t=0,b=0))
# # 添加颜色条
# fig.colorbar()

# # 添加标签和标题
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Matrix Heatmap')

# 显示图形
fig.show()

# # fig.write_html(output_path)

# from datetime import datetime

# # 获取当前的日期和时间
# now = datetime.now()

# # 获取当前的小时、分钟和秒
# current_hour = now.hour
# current_minute = now.minute
# current_second = now.second

# print(f"当前时间：{current_hour:02d}:{current_minute:02d}:{current_second:02d}")