import struct
import socket
import time
import os 
import numpy as np 
from parameter import parameter

def socketInitImage():
    udp_socket_image = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    udp_socket_image.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket_image.bind(parameter.localAddr_image)
    return udp_socket_image

    
if __name__ == '__main__':
    # udp_socket_image = socketInitImage()
    # data_row = np.zeros((parameter.send_bytes_max), dtype = np.uint8) 
    # data, client = udp_socket_image.recvfrom(parameter.send_bytes_max)
    # print(data)
    # 获取当前脚本（main.py）的路径
    current_file_path = os.path.abspath(__file__)
    
    # 获取当前脚本所在的目录
    current_file_path = os.path.abspath(__file__)
    filepath = f"{os.path.dirname(current_file_path)}{os.path.sep}"
    output_path = filepath.replace("\\", "/")

    
    # 打印outpath以验证结果
    print("Outpath:", output_path)