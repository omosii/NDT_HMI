import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from YDS import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.go_button.clicked.connect(self.geturl)
        #回车键绑定按钮，但只能在文本框外进行
        # self.__ui.go_Button.setShortcut(Qt.Key_Return)

    def geturl(self):
        url = self.__ui.url_box.toPlainText()
        # 网页加载方法        
        self.__ui.web_view.load(QUrl(url))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())
