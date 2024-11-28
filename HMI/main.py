# 2024.6 WZ
# ui转py: python -m PyQt5.uic.pyuic YDS_v1.ui -o YDS_v1.py
import sys
import threading
import os
import socket
from parameter import parameter
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from datetime import datetime
from multiprocessing import Process, Pipe, Manager
from funcImages import getImage
from YDS_v1 import Ui_MainWindow
from dataFlow import socketInitImage, socketInitCtrl, socketInitClose, recvData_UDP

# output_path = 'C:/Users/HOH/Desktop/YDS上位机/Pic/'  # C:/Users/HOH/Desktop/YDS上位机/Pic/      './Pic/'

# 定义一个信号，用于从 UDP 线程向主线程发送消息
class Communicate(QObject):
    udp_message = pyqtSignal(str)

class UDPListener(threading.Thread):
    def __init__(self, communicate, udp_socket):
        threading.Thread.__init__(self)
        self.communicate = communicate
        self.running = True
        self.udp_socket = udp_socket

    def run(self):
        self.udp_socket.settimeout(1)
        while self.running:
            try:
                if self.udp_socket:
                    data_ctrl, addr123 = self.udp_socket.recvfrom(1024)
                    message_ctrl = data_ctrl.decode('utf-8')
                    if "CollectDone" in message_ctrl:
                        self.communicate.udp_message.emit("雷达扫描结束，可出图")
                        data_ctrl = None
                        message_ctrl = None
            except socket.timeout:
                continue
            except OSError as e:
                print(f"Socket error(ly): {e}")
                self.communicate.udp_message.emit(f"套接字错误(ly): {e}")
                break

    def stop(self):
        self.running = False
        if self.udp_socket:
            self.udp_socket.close()


class MainWindow(QMainWindow): # 创建类MainWindow，使其继承QMainWindow的所有属性和方法
    def __init__(self, file_path_pipe,socketctrl,output_path): # __init__ 是 Python 中的构造方法，用于初始化类的实例 ；方法名前后的双下划线是 Python 的命名约定，表示这是一个特殊方法（通常称为“魔法方法”或“内置方法”），它由 Python 解释器自动调用。
        super().__init__()# 调用父类初始化，保证父类方法和属性可被正常使用
        self.file_path_pipe = file_path_pipe
        self.output_path = output_path
        self.udp_socket_close = socketInitClose()
        self.title = "控制与成像结果显示窗口"

        self.__ui = Ui_MainWindow() # 前置下划线是一种约定，用来指示属性或方法的“私有”性，告诉其他程序员这个变量或方法应该仅在类内部使用，而不是公开使用，不希望在类的外部被直接访问或修改。
        self.__ui.setupUi(self) # 双下划线 __ 前缀：触发“名称修饰”机制，将属性名变成 _类名__属性名 的格式，以避免属性名在继承关系中与子类产生冲突。
        self.setWindowTitle(self.title)

        self.__ui.pushButton_2d.clicked.connect(self.loadPic_2d)
        self.__ui.pushButton_3d.clicked.connect(self.loadPic_3d)
        self.__ui.pushButton_data.clicked.connect(self.loadPic_local)
        self.__ui.pushButton_radar_1.clicked.connect(self.loadParameter_reset)
        self.__ui.pushButton_radar_2.clicked.connect(self.loadParameter)
        self.__ui.pushButton_start.clicked.connect(self.sysStart)
        self.mode = 1  # 1: 实时显示 0: 显示本地Pic
        self.flag = 0  # 1: 数据有更新 0: 数据无更新
        self.para = parameter()
        self.timer = QTimer(self)  
        
        current_hour = datetime.now().hour
        current_minute = datetime.now().minute
        current_second = datetime.now().second
        self.__ui.textBrowser.append(f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}" + "  上位机启动成功")
        self.__ui.textEdit_prf.setText(f"{self.para.prf}")
        self.__ui.textEdit_B.setText(f"{self.para.B}")
        self.__ui.textEdit_fc.setText(f"{self.para.fc}")
        self.__ui.textEdit_T.setText(f"{self.para.T}")
        
        self.timer.timeout.connect(self.saveFile)    # 连接定时器超时信号，将 saveFile 方法连接到 timer 的 timeout 信号。当计时器超时时，saveFile 方法会自动被调用。
        self.timer.timeout.connect(self.upgratePic)    # 连接定时器超时信号  
        self.timer.start(1000)  # 设置定时器每秒触发一次   
        #回车键绑定按钮，但只能在文本框外进行
        # self.__ui.go_Button.setShortcut(Qt.Key_Return)

        # 创建 Communicate 对象，它将用于在 UDP 线程和主线程之间通信
        self.communicate = Communicate()

        # 连接信号和槽
        self.communicate.udp_message.connect(self.display_udp_message)

        # 初始化 UDP 监听线程
        self.socketctrl = socketctrl
        self.udp_listener = UDPListener(self.communicate, self.socketctrl)
        self.udp_listener.daemon = True # 将线程设置为守护线程
        self.udp_listener.start()

    # 当有新图像被完整接收并被保存后，更新最新文件名并打印时间与内容
    def saveFile(self):
        if self.file_path_pipe.poll(): # 用文件名的管道判断是否有新文件产生 poll() 方法：poll() 是 Pipe 对象的一个方法，用来检查管道中是否有数据可以读取
            self.flag = 1
            self.fileNew = self.file_path_pipe.recv()
            # 获取当前的小时、分钟和秒
            current_hour = datetime.now().hour
            current_minute = datetime.now().minute
            current_second = datetime.now().second
            self.__ui.textBrowser.append(f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}" + "  保存成像结果" + self.fileNew.replace(self.output_path, "").replace(".html", ""))

    # 当为动态显示模式（mode==1）并有新图像产生时（flag==1）更新显示内容并拉低新图像产生信号（flag）
    def upgratePic(self):
        if self.flag and self.mode:
            self.flag = 0
            self.__ui.webEngineView.load(QUrl(self.fileNew)) # self.__ui.webEngineView 是一个用于显示网页内容的视图组件。这个组件通常是 QWebEngineView（PyQt 中的网页浏览组件），可以用来加载和显示 HTML 页面或本地文件中的 HTML 内容。

    # 当2D按下时，更改模式为动态显示（mode==1）
    def loadPic_2d(self):
        self.mode = 1

        # 获取当前的小时、分钟和秒
        current_hour = datetime.now().hour
        current_minute = datetime.now().minute
        current_second = datetime.now().second
        self.__ui.textBrowser.append(f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}" + "  接收图像中...")
        message = "SendBIN"
        udp_socket_ctrl.sendto(message.encode('utf-8'), parameter.remoteAddr_ctrl)

        if self.flag:
        # 网页加载方法        
            self.__ui.webEngineView.load(QUrl(self.fileNew)) # QUrl(self.fileNew) 将 self.fileNew（文件的路径）转换为 QUrl 对象，使得 webEngineView 能够识别并加载文件。

    def loadPic_3d(self):
        url = self.output_path + 'sr1st.html'
        # 网页加载方法        
        self.__ui.webEngineView.load(QUrl(url))

    # 当local按下时，更改模式为历史显示（mode==0）
    def loadPic_local(self):
        self.mode = 0
        url = self.__ui.textEdit_local.toPlainText()
        self.__ui.webEngineView.load(QUrl(self.output_path + url + ".html"))

    # 加载默认的雷达参数
    def loadParameter_reset(self):
        self.para.rstParameter()
        self.__ui.textEdit_prf.setText(f"{self.para.prf}")
        self.__ui.textEdit_B.setText(f"{self.para.B}")
        self.__ui.textEdit_fc.setText(f"{self.para.fc}")
        self.__ui.textEdit_T.setText(f"{self.para.T}")
        print(self.para.prf, self.para.B, self.para.fc, self.para.T)

    # 雷达参数配置
    def loadParameter(self):
        self.para.prf = int(self.__ui.textEdit_prf.toPlainText())
        self.para.B = int(self.__ui.textEdit_B.toPlainText())
        self.para.fc = int(self.__ui.textEdit_fc.toPlainText())
        self.para.T = int(self.__ui.textEdit_T.toPlainText())
        print(self.para.prf, self.para.B, self.para.fc, self.para.T)
    
    # Zynq程序与导轨启动
    def sysStart(self):
        message = "BEGIN"
        udp_socket_ctrl.sendto(message.encode('utf-8'), parameter.remoteAddr_ctrl)
        # 获取当前的小时、分钟和秒
        current_hour = datetime.now().hour
        current_minute = datetime.now().minute
        current_second = datetime.now().second
        self.__ui.textBrowser.append(f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}" + "  雷达导轨启动！" )

    def display_udp_message(self, message):
        # 在 textBrowser 中显示接收到的 UDP 消息
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            self.__ui.textBrowser.append(f"{current_time}  {message}")
        except Exception as e:
            print(f"Error in display_udp_message: {e}")

    def stop_udp_listener(self):
        # 停止 UDP 监听线程
        self.udp_listener.stop()
        self.udp_listener.join()  # 等待线程结束

    def closeEvent(self, event):
        # 在窗口关闭时停止 UDP 监听线程
        # self.stop_udp_listener()
        message = "CLOSE"
        self.udp_socket_close.sendto(message.encode('utf-8'), parameter.remoteAddr_close)
        self.udp_socket_close.close()
        super().closeEvent(event)

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    print(f"Uncaught exception(ly): {exc_type}, {exc_value}")

if __name__ == '__main__':
    # 获取当前路径
    current_file_path = os.path.abspath(__file__)
    filepath = f"{os.path.dirname(current_file_path)}{os.path.sep}"
    output_path = filepath.replace("\\", "/")
    # 初始化套接字
    udp_socket_image = socketInitImage()
    udp_socket_ctrl = socketInitCtrl()
    
    imageData_pipe = Pipe() # Pipe() 是 multiprocessing 模块中的一个方法，用于创建管道（Pipe）对象。 管道是一种进程间通信的机制，允许两个进程之间直接进行数据传输。
    file_path_pipe = Pipe() # Pipe() 返回一对连接的对象，这两个端点具有对称性。通常称为 pipe_end1 和 pipe_end2。这两个端点表示管道的两端，可以用来进行数据的发送和接收。
    sys.excepthook = handle_exception
    # UDP接收
    recvData_UDP_p = Process(target = recvData_UDP, args = (imageData_pipe[0], udp_socket_image), daemon=True) # aemon=True 可以在创建线程或进程时传入，表示该线程或进程将作为守护进程运行。 当主程序结束时，守护线程会被自动终止，无论它是否完成了任务。
    # UDP数据转图像并保存
    getImage_p = Process(target = getImage, args = (imageData_pipe[1], file_path_pipe[0], output_path), daemon=True)  # args是一个元组，元组只有一个元素的时候，不能省略逗号
    recvData_UDP_p.start()
    getImage_p.start()
    # CollectDone_p.start()
    app=QApplication(sys.argv)
    win=MainWindow(file_path_pipe[1],udp_socket_ctrl,output_path) #类的定义和实例化是两个不同的步骤。在类定义时，file_path_pipe[1] 并不需要直接体现在类的定义中。类的构造方法 __init__(self, ...) 用于接收并处理实例化时传入的参数。
    win.show()
    sys.exit(app.exec())
    

