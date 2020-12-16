from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_changePic(object):
    def setupUi(self, changePic):
        self.centralwidget = QtWidgets.QWidget(changePic)
        # Create bg
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.bg.setPixmap(QtGui.QPixmap("sourcepic\\bg1.jpg"))        # Create preview label
        self.previewlbl = QtWidgets.QLabel(self.centralwidget)
        self.previewlbl.setGeometry(QtCore.QRect(190, 50, 640, 480))
        self.previewlbl.setText("Preview")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.previewlbl.setFont(font)
        self.previewlbl.setFrameShape(QtWidgets.QFrame.Box)
        self.previewlbl.setAlignment(QtCore.Qt.AlignCenter)
        # Create get pic button
        self.getpicbt = QtWidgets.QPushButton(self.centralwidget)
        self.getpicbt.setText("Get\npicture")
        self.getpicbt.setGeometry(QtCore.QRect(190, 540, 150, 71))
        font.setPointSize(12)
        self.getpicbt.setFont(font)
        # Create take pic button
        self.takepicbt = QtWidgets.QPushButton(self.centralwidget)
        self.takepicbt.setText("Take\na\nPicture")
        self.takepicbt.setGeometry(QtCore.QRect(360, 540, 150, 71))
        font.setPointSize(12)
        self.takepicbt.setFont(font)
        # Create Live view button
        self.liveviewbt = QtWidgets.QPushButton(self.centralwidget)
        self.liveviewbt.setText("LIVE\nview")
        self.liveviewbt.setGeometry(QtCore.QRect(520, 540, 150, 71))
        font.setPointSize(12)
        self.liveviewbt.setFont(font)
        # Create finished button
        self.finishedbt = QtWidgets.QPushButton(self.centralwidget)
        self.finishedbt.setText("Finished")
        self.finishedbt.setGeometry(QtCore.QRect(680, 540, 150, 71))
        font.setPointSize(16)
        self.finishedbt.setFont(font)
        # Create skip button
        self.skipbt = QtWidgets.QPushButton(self.centralwidget)
        self.skipbt.setText("Skip")
        self.skipbt.setGeometry(QtCore.QRect(450, 620, 121, 41))
        font.setPointSize(16)
        self.skipbt.setFont(font)




