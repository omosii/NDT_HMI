import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口大小
    w.resize(500,400)
    # 移动窗口
    w.move(300,300)

    # 设置窗口标题
    w.setWindowTitle('第一个基于PyQt5的窗口')

    # 显示窗口
    w.show()

    # 进入程序主循环，并通过exit函数确保主循环安全退出
    sys.exit(app.exec_())