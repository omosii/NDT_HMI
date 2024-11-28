import sys
import MainWinSignalSlot
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = MainWinSignalSlot.Ui_MainWindow()
    # 向QMainWindow()添加控件
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())