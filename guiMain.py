import sys,matplotlib
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap


class baseWedget(QtGui.QWidget):
    def __init__(self):
        super(baseWedget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon("example.png"))
        fileButton = QtGui.QPushButton("文件", self)
        fileButton.setFixedSize(100, 50)
        confButton = QtGui.QPushButton("配置", self)
        confButton.setFixedSize(100, 50)
        helpButton = QtGui.QPushButton("帮助", self)
        helpButton.setFixedSize(100, 50)
        analyButton = QtGui.QPushButton("分析", self)
        analyButton.setFixedSize(100,50)
        bigButton = QtGui.QPushButton("放大", self)
        bigButton.setFixedSize(100,50)
        smallButton = QtGui.QPushButton("缩小", self)
        smallButton.setFixedSize(100,50)
        adaptButton = QtGui.QPushButton("缩放合适大小", self)
        adaptButton.setFixedSize(100,50)
        quitButton = QtGui.QPushButton("退出", self)
        quitButton.setFixedSize(100,50)
        picWedget = QtGui.QLabel(self)
        picWedget.setPixmap(QPixmap("example.png"))
        picWedget.setGeometry(0, 50, 900, 675)
        #菜单栏
        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(fileButton)
        hbox1.addWidget(confButton)
        hbox1.addWidget(helpButton)
        hbox1.addStretch(1)
        #绘图栏 + 竖排菜单栏
        vbox2 = QtGui.QVBoxLayout()
        vbox2.addWidget(analyButton)
        vbox2.setStretchFactor(analyButton,2)
        vbox2.addWidget(bigButton)
        vbox2.addWidget(smallButton)
        vbox2.addWidget(adaptButton)
        vbox2.addWidget(quitButton)
        vbox2.addStretch(1)
        vbox = QtGui.QVBoxLayout()
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(picWedget)
        hbox2.addLayout(vbox2)
        hbox2.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        vbox.addStretch(1)
        QtGui.QPixmap
        # self.text = "Hello @ USTB"
        self.setGeometry(300, 200, 1080, 800)
        self.setWindowTitle('交互式移动通信网络分析和规划')
        self.show()
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        # self.drawRectangles(qp)
        # self.drawText(event, qp)
        qp.end()
    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 30))
        qp.setFont(QtGui.QFont('Times New Roman', 100))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)

    def drawRectangles(self, qp):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)


app = QtGui.QApplication(sys.argv)
ex = baseWedget()
sys.exit(app.exec_())