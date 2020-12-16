from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginsection(object):
    def setupUi(self, loginsection):
        self.centralwidget = QtWidgets.QWidget(loginsection)
        # Create bg
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.bg.setPixmap(QtGui.QPixmap("sourcepic\\bg1.jpg"))
        # Create username line edit
        self.usernameLE = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLE.setGeometry(QtCore.QRect(380, 200, 291, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.usernameLE.setFont(font)
        # Create username label
        self.usernamelbl = QtWidgets.QLabel(self.centralwidget)
        self.usernamelbl.setGeometry(QtCore.QRect(240, 200, 141, 31))
        font.setPointSize(18)
        self.usernamelbl.setFont(font)
        self.usernamelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.usernamelbl.setText("Username")
        # Create password line edit
        self.passwordLE = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setGeometry(QtCore.QRect(380, 250, 291, 31))
        font.setPointSize(16)
        self.passwordLE.setFont(font)
        # Create password label
        self.passwordlbl = QtWidgets.QLabel(self.centralwidget)
        self.passwordlbl.setGeometry(QtCore.QRect(240, 250, 141, 31))
        font.setPointSize(18)
        self.passwordlbl.setFont(font)
        self.passwordlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordlbl.setText("Password")
        # Create login button
        self.loginbt = QtWidgets.QPushButton(self.centralwidget)
        self.loginbt.setGeometry(QtCore.QRect(410, 310, 191, 51))
        self.loginbt.setFont(font)
        self.loginbt.setText("Login")
        # Create back button
        self.backbt = QtWidgets.QPushButton(self.centralwidget)
        self.backbt.setGeometry(QtCore.QRect(20, 630, 171, 51))
        font.setPointSize(18)
        self.backbt.setFont(font)
        self.backbt.setText("Back")
        # Create error label
        self.errorlbl = QtWidgets.QLabel(self.centralwidget)
        self.errorlbl.setGeometry(QtCore.QRect(255, 150, 421, 31))
        font.setPointSize(14)
        self.errorlbl.setFont(font)
        self.errorlbl.setStyleSheet("color: red;")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginsection = QtWidgets.QMainWindow()
    ui = Ui_loginsection()
    ui.setupUi(loginsection)
    loginsection.show()
    sys.exit(app.exec_())
