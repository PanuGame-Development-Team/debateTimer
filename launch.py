import font_rc
from mainui import Ui_Form
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QFontDatabase,QFont,QGuiApplication
# from player import PlayerWidget
from PyQt5.QtCore import pyqtSlot,Qt,QCoreApplication
from os import popen
QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling,True)
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
app = QApplication(["argtimer"])
fontdb = QFontDatabase()
fontid = fontdb.addApplicationFont(":resources/FiraCode-Regular.ttf")
class Window(QWidget):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.setFont(QFont("Fira Code"))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.status = 0
    @pyqtSlot()
    def on_startstep_clicked(self):
        if self.status == 0:
            dtime = eval(self.ui.time1.text())
            self.status = 1
        elif int(self.status) == 1:
            dtime = eval(self.ui.time2.text())
            self.status += 0.25
        elif self.status == 2:
            dtime = eval(self.ui.time3.text())
            self.status = 3
        elif self.status == 3:
            dtime = eval(self.ui.time3a.text())
        else:
            dtime = eval(self.ui.time4.text())
            self.status = -1
        # PlayerWidget(dtime=dtime).exec()
        popen("player.exe dtime=%d"%dtime).read()
        if self.status == -1:
            self.close()
        self.repaint()
    @pyqtSlot()
    def on_passstep_clicked(self):
        if self.status >= 1 and self.status < 2:
            self.status += 0.25
        else:
            self.status += 1
        if self.status > 4:
            self.close()
        self.repaint()
    def paintEvent(self,event):
        if self.status >= 4:
            self.ui.label3a.setDisabled(True)
            self.ui.second3a.setDisabled(True)
            self.ui.time3a.setDisabled(True)
            y = 190
        elif self.status >= 3:
            self.ui.label3.setDisabled(True)
            self.ui.second3.setDisabled(True)
            self.ui.time3.setDisabled(True)
            y = 150
        elif self.status >= 2:
            self.ui.label2.setDisabled(True)
            self.ui.second2.setDisabled(True)
            self.ui.time2.setDisabled(True)
            self.ui.round.setDisabled(True)
            self.ui.round_text.setDisabled(True)
            y = 110
        elif self.status >= 1:
            self.ui.label1.setDisabled(True)
            self.ui.second1.setDisabled(True)
            self.ui.time1.setDisabled(True)
            self.ui.round.setText(str(int(self.status*4-3)))
            y = 70
        else:
            y = 30
        self.ui.pointer.setGeometry(20,y,40,30)
window = Window()
window.show()
app.exec_()