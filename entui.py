from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_entranceSection(object):
    def setupUi(self, entranceSection):
        self.centralwidget = QtWidgets.QWidget(entranceSection)
        self.centralwidget.setObjectName("centralwidget")
        # Create background
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.bg.setPixmap(QtGui.QPixmap("sourcepic\\bgplain1.png"))
        self.setup_UI_button()
    def setup_UI_button(self):
        # Create login button
        self.loginbt = QtWidgets.QPushButton(self.centralwidget)
        self.loginbt.setText("Login")
        self.loginbt.setGeometry(QtCore.QRect(350, 125, 300, 100))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.loginbt.setFont(font)
        # Create register button
        self.regisbt = QtWidgets.QPushButton(self.centralwidget)
        self.regisbt.setText("Register")
        self.regisbt.setGeometry(QtCore.QRect(350, 240, 300, 100))
        self.regisbt.setFont(font)
        # Create guest button
        self.guestbt = QtWidgets.QPushButton(self.centralwidget)
        self.guestbt.setText("Guest")
        self.guestbt.setGeometry(QtCore.QRect(350, 355, 300, 100))
        self.guestbt.setFont(font)
        # Create Quit button
        self.qtbt = QtWidgets.QPushButton(self.centralwidget)
        self.qtbt.setText("Quit")
        self.qtbt.setGeometry(QtCore.QRect(350, 470, 300, 100))
        self.qtbt.setFont(font)

