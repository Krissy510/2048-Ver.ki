from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu(object):
    def setupUi(self, menu):
        self.centralwidget = QtWidgets.QWidget(menu)
        # Create bg
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.bg.setPixmap(QtGui.QPixmap("sourcepic\\bgplain1.png"))
        # Create Logo label
        self.logolbl = QtWidgets.QLabel(self.centralwidget)
        self.logolbl.setGeometry(QtCore.QRect(100,20,800,271))
        self.logolbl.setAlignment(QtCore.Qt.AlignCenter)
        self.logolbl.setPixmap(QtGui.QPixmap("sourcepic\\logo.png"))
        # Create play button
        self.playbt = QtWidgets.QPushButton(self.centralwidget)
        self.playbt.setGeometry(QtCore.QRect(420,270,181,61))
        self.playbt.setText("Play")
        # Create Profile button
        self.profilebt = QtWidgets.QPushButton(self.centralwidget)
        self.profilebt.setGeometry(QtCore.QRect(420, 340, 181, 61))
        self.profilebt.setText("Profile")
        # Create Leader board button
        self.LeaderBbt = QtWidgets.QPushButton(self.centralwidget)
        self.LeaderBbt.setGeometry(QtCore.QRect(420, 410, 181, 61))
        self.LeaderBbt.setText("Leader board")
        # Create Change account button
        self.changeAbt = QtWidgets.QPushButton(self.centralwidget)
        self.changeAbt.setGeometry(QtCore.QRect(420, 480, 181, 61))
        self.changeAbt.setText("Change account")
        # Create Quit button
        self.quitbt = QtWidgets.QPushButton(self.centralwidget)
        self.quitbt.setGeometry(QtCore.QRect(420, 550, 181, 61))
        self.quitbt.setText("Quit")
