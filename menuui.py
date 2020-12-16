from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu(object):
    def setupUi(self, menu):
        self.centralwidget = QtWidgets.QWidget(menu)
        # Create back button
        self.backbt = QtWidgets.QPushButton(self.centralwidget)
        self.backbt.setGeometry(QtCore.QRect(20, 630, 171, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.backbt.setFont(font)
        self.backbt.setText("Back")
