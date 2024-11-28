# import sys
import struct
import socket
import time
import numpy as np 
from parameter import parameter
from datetime import datetime

def delay_ms(ms):
    start = time.perf_counter()
    while (time.perf_counter() - start) < ms / 1000:
        pass

def socketInitImage():
    # 1.创建一个udp套接字
    udp_socket_image = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.socket() 是 Python socket 模块中的一个方法，用于创建套接字对象。 socket.AF_INET 表示使用 IPv4 地址（网络地址家族）；socket.SOCK_DGRAM 表示使用 UDP 协议（无连接、数据报协议）。
    udp_socket_image.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    # ip一般不用写
    udp_socket_image.bind(parameter.localAddr_image)
    return udp_socket_image

def socketInitCtrl():
    # 1.创建一个udp套接字
    udp_socket_ctrl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket_ctrl.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    # ip一般不用写
    udp_socket_ctrl.bind(parameter.localAddr_ctrl)
    return udp_socket_ctrl

def socketInitClose():
    # 1.创建一个udp套接字
    udp_socket_close = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.socket() 是 Python socket 模块中的一个方法，用于创建套接字对象。 socket.AF_INET 表示使用 IPv4 地址（网络地址家族）；socket.SOCK_DGRAM 表示使用 UDP 协议（无连接、数据报协议）。
    udp_socket_close.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    # ip一般不用写
    udp_socket_close.bind(parameter.localAddr_close)
    return udp_socket_close

def recvData_UDP(imageData_pipe, udp_socket):
    if parameter.bytes_perImage == 4:
        data_row = np.zeros((int)(parameter.send_bytes_max/4), dtype = np.float32)   # 默认为浮点数64,应改为float32
        while True:
            data, client = udp_socket.recvfrom(parameter.send_bytes_max)
            k = 0
            while 4 * k + 4 <= len(data):
                temp = struct.unpack('f', data[4 * k : 4 * k + 4]) # 数据不对的话可能要注意大小端 data[4 * k : 4 * k + 4]提取四个元素，即不包含data[4 * k + 4]
                temp = float(temp[0])
                data_row[k] = temp
                k = k + 1
            imageData_pipe.send(data_row)
    elif parameter.bytes_perImage == 1:
        data_row = np.zeros((parameter.send_bytes_max), dtype = np.uint8) 
        while True:
            data, client = udp_socket.recvfrom(parameter.send_bytes_max)
            k = 0
            while k + 1 <= len(data): # 为什么要循环不能直接赋过去
                # print(type(data))
                # temp = struct.unpack('B', data[k])
                # temp = int(temp[0])
                data_row[k] = data[k]
                k = k + 1
            # data_row = data
            imageData_pipe.send(data_row) # 通过管道发送给其他进程 



