from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_leaderboard(object):
    def setupUi(self, leaderboard):
        self.centralwidget = QtWidgets.QWidget(leaderboard)
        # Create bg
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.bg.setPixmap(QtGui.QPixmap("sourcepic\\bgplain1.png"))
        self.setupUi_rank()
        self.setupUi_label()

    def setupUi_rank(self):
        self.rank = QtWidgets.QLabel(self.centralwidget)
        self.rank.setGeometry(QtCore.QRect(50, 60, 100, 92))
        self.rank.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_2 = QtWidgets.QLabel(self.centralwidget)
        self.rank_2.setGeometry(QtCore.QRect(50, 170, 100, 92))
        self.rank_2.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_3 = QtWidgets.QLabel(self.centralwidget)
        self.rank_3.setGeometry(QtCore.QRect(50, 280, 100, 92))
        self.rank_3.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_4 = QtWidgets.QLabel(self.centralwidget)
        self.rank_4.setGeometry(QtCore.QRect(50, 390, 100, 92))
        self.rank_4.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_5 = QtWidgets.QLabel(self.centralwidget)
        self.rank_5.setGeometry(QtCore.QRect(50, 500, 100, 92))
        self.rank_5.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_6 = QtWidgets.QLabel(self.centralwidget)
        self.rank_6.setGeometry(QtCore.QRect(510, 60, 100, 92))
        self.rank_6.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_7 = QtWidgets.QLabel(self.centralwidget)
        self.rank_7.setGeometry(QtCore.QRect(510, 170, 100, 92))
        self.rank_7.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_8 = QtWidgets.QLabel(self.centralwidget)
        self.rank_8.setGeometry(QtCore.QRect(510, 280, 100, 92))
        self.rank_8.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_9 = QtWidgets.QLabel(self.centralwidget)
        self.rank_9.setGeometry(QtCore.QRect(510, 390, 100, 92))
        self.rank_9.setFrameShape(QtWidgets.QFrame.Box)
        self.rank_10 = QtWidgets.QLabel(self.centralwidget)
        self.rank_10.setGeometry(QtCore.QRect(510, 500, 100, 92))
        self.rank_10.setFrameShape(QtWidgets.QFrame.Box)

    def setupUi_label(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label.setGeometry(QtCore.QRect(160, 60, 311, 92))
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 170, 311, 92))
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 280, 311, 92))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 390, 311, 92))
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(font)
        self.label_5.setGeometry(QtCore.QRect(160, 500, 311, 92))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFont(font)
        self.label_6.setGeometry(QtCore.QRect(620, 60, 311, 92))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setFont(font)
        self.label_7.setGeometry(QtCore.QRect(620, 170, 311, 92))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setFont(font)
        self.label_8.setGeometry(QtCore.QRect(620, 280, 311, 92))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setFont(font)
        self.label_9.setGeometry(QtCore.QRect(620, 390, 311, 92))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 500, 311, 92))
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.backbt = QtWidgets.QPushButton(self.centralwidget)
        self.backbt.setGeometry(QtCore.QRect(50, 600, 141, 51))


