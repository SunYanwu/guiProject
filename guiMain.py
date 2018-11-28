import sys,math,cairo
from PIL import Image
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap

#主界面
class baseWedget(QtGui.QMainWindow):
    def __init__(self):
        super(baseWedget, self).__init__()
        self.initUI()

    def initUI(self):
        self.main_frame = QtGui.QWidget()
        self.setWindowIcon(QtGui.QIcon("Icon.jpg"))
        # 菜单
        ope = QtGui.QAction(QtGui.QIcon('Icon.jpg'), '打开', self)
        self.connect(ope, QtCore.SIGNAL('triggered()'), self.showDialogFile)

        clos = QtGui.QAction(QtGui.QIcon("Icon.jpg"), '关闭', self)
        self.connect(clos, QtCore.SIGNAL('triggered()'), self.close)

        sett = QtGui.QAction(QtGui.QIcon("Ioon.jpg"), '配置', self)
        self.connect(sett, QtCore.SIGNAL('triggered()'), self.showDialogConf)

        help = QtGui.QAction(QtGui.QIcon("Icon.jpg"), '作者', self)
        self.connect(help, QtCore.SIGNAL('triggered()'), self.showDialogHelp)

        # 添加菜单栏
        menubar = self.menuBar()
        file = menubar.addMenu('文件')
        file.addAction(ope)
        file.addAction(clos)

        setting = menubar.addMenu('配置')
        setting.addAction(sett)

        helpp = menubar.addMenu('帮助')
        helpp.addAction(help)
        #添加功能按钮
        analyButton = QtGui.QPushButton("分析", self)
        analyButton.setFixedSize(100,50)
        bigButton = QtGui.QPushButton("放大", self)
        bigButton.setFixedSize(100,50)
        smallButton = QtGui.QPushButton("缩小", self)
        smallButton.setFixedSize(100,50)
        adaptButton = QtGui.QPushButton("缩放合适大小", self)
        adaptButton.setFixedSize(100,50)
        #定义和绑定退出动作
        quitButton = QtGui.QPushButton("退出", self)
        quitButton.clicked.connect(self.onClickQuit)
        quitButton.setFixedSize(100,50)
        picWedget = QtGui.QLabel(self)
        picWedget.setPixmap(QPixmap("building.png"))
        picWedget.setGeometry(0, 50, 900, 675)
        #定义主界面布局
        vbox2 = QtGui.QVBoxLayout()
        vbox2.addWidget(analyButton)
        # vbox2.setStretchFactor(analyButton)
        vbox2.addWidget(bigButton)
        vbox2.addWidget(smallButton)
        vbox2.addWidget(adaptButton)
        vbox2.addWidget(quitButton)
        vbox2.addStretch(1)
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(picWedget)
        hbox2.addLayout(vbox2)
        hbox2.addStretch(1)

        #加载页面配置
        self.main_frame.setLayout(hbox2)
        self.setCentralWidget(self.main_frame)

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

    # 退出键响应
    def onClickQuit(self, evt):
        quit()
    # 配置对话框
    def showDialogConf(self):
        dialog = QtGui.QDialog()  # 创建QDialog对象
        btn = QtGui.QPushButton('保存', dialog)  # 创建按钮到新创建的dialog对象中
        btn.move(300, 220)
        dialog.connect(btn, QtCore.SIGNAL('clicked()'), self.saveNum)  # 保存输入数据
        # 创建4个输入框
        b = [u'热噪声:', u'带宽:', u'频率:', u'RSRP门限:']
        d = ['dBm/Hz', 'Hz', 'MHz', 'dBm']
        for i in range(4):
            b1 = QtGui.QLabel(dialog)
            b1.setText(b[i])
            b1.setGeometry(50, 50 + i * 40, 60, 30)
            d1 = QtGui.QLabel(dialog)
            d1.setText(d[i])
            d1.setGeometry(210, 50 + i * 40, 60, 30)
        self.c1 = QtGui.QLineEdit(dialog)
        self.c1.setGeometry(110, 50 + 0 * 40, 80, 25)
        self.c2 = QtGui.QLineEdit(dialog)
        self.c2.setGeometry(110, 50 + 1 * 40, 80, 25)
        self.c3 = QtGui.QLineEdit(dialog)
        self.c3.setGeometry(110, 50 + 2 * 40, 80, 25)
        self.c4 = QtGui.QLineEdit(dialog)
        self.c4.setGeometry(110, 50 + 3 * 40, 80, 25)
        # 取名
        dialog.setWindowTitle("配置")
        dialog.exec_()
     # 保存配置参数
    def saveNum(self):
        num1 = self.c1.text()
        num2 = self.c2.text()
        num3 = self.c3.text()
        num4 = self.c4.text()
        try:
            self.noise = int(num1)
            self.bw = int(num2)
            self.fre = int(num3)
            self.rsrpl = int(num4)
            print('保存成功')
        except:
            print('无效输入')
    # 帮助对话框
    def showDialogHelp(self):
        dialog = QtGui.QDialog()
        a = QtGui.QLabel(dialog)
        a.setText('制作人：孙岩武  41504166')
        a.setGeometry(100, 100, 200, 150)
        dialog.setWindowTitle("作者")
        dialog.exec_()
    # 打开文件并画图
    def showDialogFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, '打开文件', './')
        WIDTH = 5000  # 6000*3500
        HEIGHT = 4000
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        ctx = cairo.Context(surface)
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(1);
        # 设置边框
        ctx.set_source_rgb(1, 1, 1)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.fill_preserve()
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()
        # 打开文件
        with open(filename) as f:
            data = []
            for i in range(1627):  # 读取建筑信息
                s1 = f.readline()
                s1 = s1.strip('\n')
                data.append(s1.split('\t'))
                num = int(data[i][2])
                x = []
                y = []
                for j in range(num):
                    s2 = (f.readline())
                    s2 = s2.strip('\n')
                    d = s2.split('\t')
                    x.append(int((float(d[0]) - 440500)))
                    y.append(int((float(d[1]) - 4427000)))
                ctx.set_source_rgb(0, 0, 0)
                ctx.set_line_width(1)
                ctx.move_to(x[0], y[0])
                for k in range(num - 1):
                    ctx.line_to(x[k + 1], y[k + 1])
                ctx.stroke()
                # print i
            for i1 in range(25):  # 读取25个基站信息
                ss = (f.readline())
                ss1 = (f.readline())
                ss1 = ss1.strip('\n')
                ss1 = ss1.split('\t')
                x1 = int((float(ss1[0]) - 440500))
                y1 = int((float(ss1[1]) - 4427000))
                self.data1.append(ss1[2])
                ctx.set_source_rgb(1, 0, 0)
                ctx.set_line_width(4)
                ctx.arc(x1, y1, 50, 0, 2 * math.pi)
                ctx.stroke()
                # print i1,self.data1
            ctx.set_source_rgb(0, 0, 0)
            ctx.rectangle(0, 0, WIDTH, HEIGHT)
            ctx.stroke()
            surface.write_to_png("build.png")

app = QtGui.QApplication(sys.argv)
ex = baseWedget()
ex.show()
sys.exit(app.exec_())