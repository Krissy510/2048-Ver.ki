from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_profile(object):
    def setupUi(self, profile):
        self.centralwidget = QtWidgets.QWidget(profile)
        # Create bg
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.bg.setPixmap(QtGui.QPixmap("sourcepic\\bgplain1.png"))
        self.setupUI_label()
        self.setup_UI_button()

    def setupUI_label(self):
        # Create profile pic label
        self.pplbl = QtWidgets.QLabel(self.centralwidget)
        self.pplbl.setGeometry(QtCore.QRect(70, 70,220, 220))
        self.pplbl.setFrameShape(QtWidgets.QFrame.Box)
        # Create Username label
        self.uslbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.uslbl.setGeometry(QtCore.QRect(310, 70, 621, 81))
        self.uslbl.setFont(font)
        self.uslbl.setFrameShape(QtWidgets.QFrame.Box)
        self.uslbl.setText("USERNAME:")
        # Create Birth date label
        self.bdlbl = QtWidgets.QLabel(self.centralwidget)
        self.bdlbl.setGeometry(QtCore.QRect(310, 180, 621, 81))
        self.bdlbl.setFont(font)
        self.bdlbl.setFrameShape(QtWidgets.QFrame.Box)
        self.bdlbl.setText("BIRTH DATE:")
        # Create phonenum label
        self.pnlbl = QtWidgets.QLabel(self.centralwidget)
        self.pnlbl.setGeometry(QtCore.QRect(310, 290, 621, 81))
        self.pnlbl.setFont(font)
        self.pnlbl.setFrameShape(QtWidgets.QFrame.Box)
        self.pnlbl.setText("PHONE NUMBER:")
        # Create high score label
        self.hslbl = QtWidgets.QLabel(self.centralwidget)
        self.hslbl.setGeometry(QtCore.QRect(310, 400, 621, 81))
        self.hslbl.setFont(font)
        self.hslbl.setFrameShape(QtWidgets.QFrame.Box)
        self.hslbl.setText("HIGH SCORE:")
        # Create rank label
        self.ranklbl = QtWidgets.QLabel(self.centralwidget)
        self.ranklbl.setGeometry(QtCore.QRect(90, 290, 181, 41))
        # font.setPointSize(10)
        self.ranklbl.setFont(font)
        self.ranklbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ranklbl.setText("RANK:")

    def setup_UI_button(self):
        # Create back button
        self.backbt = QtWidgets.QPushButton(self.centralwidget)
        self.backbt.setGeometry(QtCore.QRect(50, 600, 171, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.backbt.setFont(font)
        self.backbt.setText("Back")
        # Create change pass button
        self.cpbt = QtWidgets.QPushButton(self.centralwidget)
        self.cpbt.setGeometry(QtCore.QRect(310, 525, 180, 71))
        font.setPointSize(10)
        self.cpbt.setFont(font)
        self.cpbt.setText("Change\npassword")
        # Create edit pic button
        self.epbt = QtWidgets.QPushButton(self.centralwidget)
        self.epbt.setGeometry(QtCore.QRect(530, 525, 180, 71))
        self.epbt.setFont(font)
        self.epbt.setText("Edit\nProfile PIC")
        # Create edit info button
        self.eibt = QtWidgets.QPushButton(self.centralwidget)
        self.eibt.setGeometry(QtCore.QRect(750, 525, 180, 71))
        self.eibt.setFont(font)
        self.eibt.setText("Edit Info")
        # Create refresh button
        self.refreshbt = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbt.setGeometry(QtCore.QRect(90, 330, 181, 41))
        self.refreshbt.setFont(font)
        self.refreshbt.setText("Refresh")

