import numpy as np
import os
import plotly.express as px # plotly.express（简称 px），plotly 库中的子模块，提供了许多用于快速绘图的简单接口。
from parameter import parameter 

# output_path = 'C:/Users/HOH/Desktop/YDS上位机/Pic/'  c:\Users\HOH\Desktop\YDS上位机\
 
# imageData_pipe: UDP进程传来的图像数据; file_path_pipe: 图像保存后的文件路径
def getImage(imageData_pipe, file_path_pipe,output_path):  #是否要判断接受进来的数据类型？
    imageData = np.array([])
    i = 0
    file_path = output_path + 'pic2D_' + str(i) + '.html'
    while True:
        if os.path.exists(file_path):  # exists() 是 os.path 模块下的一个函数，用来检查指定路径（file_path）是否存在。
            i = i + 1
            file_path = output_path + 'pic2D_' + str(i) + '.html'
        else:
            break

    while True:
        imageData_temp = imageData_pipe.recv()
        imageData = np.append(imageData, imageData_temp)
        if len(imageData) == parameter.numPoints:
            matrix = np.resize(imageData, (parameter.numRow, parameter.numCol))
            imageData = None
            imageData = np.array([])
            
            fig = px.imshow(matrix, aspect='auto')  # 使用viridis颜色映射 imshow()，用于将二维数组（矩阵）显示为图像。
            fig.update_layout(width=800,height=600) # update_layout()，Plotly 图表对象的一个方法，用于更新或自定义图表的布局（包括尺寸、标题、背景等）。
            fig.write_html(file_path)
            file_path_pipe.send(file_path)
            i = i + 1
            file_path = output_path + 'pic2D_' + str(i) + '.html'

