import sys
import os
import cv2
import sqlite3
from PIL import Image
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QImage
from entui import *
from baseloginui import *
from changepicui import *
from forgotps import *
from menuui import *

class DBedit:
    def checkItemExist(self, item, type):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'SELECT {type} FROM player')
        row = cur.fetchall()
        for value in row:
            if item == value[0]:
                return True
        return False

    def adddatabase(self,us,ps,bd,pn):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        sql = "INSERT OR IGNORE INTO player VALUES (?,?,?,?,0,NULL)"
        cur.execute(sql, (us, ps, bd, pn))
        con.commit()

    def getitemDatabase(self,us,type):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'SELECT username,{type} FROM player')
        row = cur.fetchall()
        for value in row:
            if us == value[0]:
                return value[1]

    def updateDatabase(self,us,type,new):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        sql = f"UPDATE player SET {type} = ? WHERE username = ?"
        cur.execute(sql,[new,us])
        con.commit()

class USER:
    def __init__(self,us):
        self.us = us
        self.pnum = DBedit().getitemDatabase(us,"pnum")
        self.hscore = DBedit().getitemDatabase(us,"highscore")

def errorbox(msg):
    esg = QMessageBox()
    esg.setIcon(QMessageBox.Critical)
    esg.setWindowTitle("ERROR!")
    esg.setWindowIcon(QtGui.QIcon('sourcepic\\erroricon.png'))
    esg.setText(msg)
    esg.setStandardButtons(QMessageBox.Close)
    esg.exec_()

def successbox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Success")
    msg.setWindowIcon(QtGui.QIcon('sourcepic\\check.png'))
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Close)
    msg.exec_()

# Widget index 0
class EntUI(QWidget):
    def __init__(self):
        super(EntUI, self).__init__()
        self.ui = Ui_entranceSection()
        self.ui.setupUi(self)
        self.ui.loginbt.clicked.connect(lambda gotologin: widget.setCurrentIndex(1))
        self.ui.regisbt.clicked.connect(lambda gotoregister: widget.setCurrentIndex(2))
        self.ui.guestbt.clicked.connect(self.gotomenu)
        self.ui.qtbt.clicked.connect(lambda leave: quit(0))

    def gotomenu(self):
        global player
        player = "Guest"
        widget.setCurrentIndex(5)


class LoginandRegisterBaseUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginsection()
        self.ui.setupUi(self)
        self.ui.backbt.clicked.connect(self.gobackMenu)

    def checkPasswordFormat(self, ps):
        check = [0,0,0]
        for char in ps:
            if char.isdigit():
                check[0] = 1
            elif char.isupper():
                check[1] = 1
            elif char.islower():
                check[2] = 1
        if sum(check) == 3:
            return True
        else:
            return False

    def checkUser(self,us):
        if us != "" and " " not in us:
            if DBedit().checkItemExist(us,"username"):
                return 1
            else:
                return -1
        else:
            return 0

    def checkPassFormat(self,ps):
        if ps != "" or " " in ps:
            if self.checkPasswordFormat(ps):
                return 1
            else:
                return -1
        else:
            return 0

    def checkBDFormat(self,bd):
        if bd != "" or " " in bd:
            if len(bd) != 5:
                return -1
            elif bd[2] != "/":
                return -1
            else:
                bd = bd.split("/")
                if bd[0].isdigit() and bd[1].isdigit():
                    bd = list(map(int,bd))
                    if 1 <= bd[0] <=31:
                        if 1 <= bd[1] <= 12:
                            if bd[0] == 30 and bd[1] in [4,6,9,11]:
                                return 1
                            elif bd[0] == 31 and bd[1] in [1,3,5,7,8,10,12]:
                                return 1
                            elif bd[0] < 30:
                                return 1
                            else:
                                return -2
                        else:
                            return -3
                    else:
                        return -2
                elif not bd[0].isdigit():
                    return -2
                elif not bd[1].isdigit():
                    return -3
        else:
            return 0

    def checkPN(self,pn):
        if pn != "" or " " in pn:
            if 4 <= len(pn) <= 12:
                if pn.isdigit():
                    if DBedit().checkItemExist(pn,"pnum"):
                        return -2
                    else:
                        return 1
                else:
                    return -1
            else:
                return -1
        else:
            return 0

    def clearText(self,label_list):
        for wg in label_list:
            wg.setText("")

    def gobackMenu(self):
        self.clearText([self.ui.usernameLE,self.ui.passwordLE,self.ui.errorlbl])
        widget.setCurrentIndex(0)

# Widget index 1
class LoginUI(LoginandRegisterBaseUI):
    def __init__(self):
        super(LoginUI, self).__init__()
        # Create forgot password bt
        self.fpbt = QtWidgets.QPushButton(self.ui.centralwidget)
        self.fpbt.setGeometry(QtCore.QRect(760, 630, 230, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.fpbt.setFont(font)
        self.fpbt.setText("Forgot Password?")
        self.fpbt.setObjectName("fpbt")
        # self.ui.backbt.clicked.connect(self.gobackMenu)
        self.ui.loginbt.clicked.connect(self.loginbtPressed)
        self.fpbt.clicked.connect(lambda gotoforgotpass: widget.setCurrentIndex(4))

    def loginbtPressed(self):
        user = self.ui.usernameLE.text()
        ps = self.ui.passwordLE.text()
        self.clearText([self.ui.errorlbl])
        # Check user
        checkus = self.checkUser(user)
        checkps = self.checkPasswordFormat(ps)
        if checkus == 1 and checkps == 1:
            if ps == DBedit().getitemDatabase(user,"password"):
                self.clearText([self.ui.usernameLE,self.ui.passwordLE])
                successbox(f"Successfully login as {user}")
                global player
                player = USER(user)
                widget.setCurrentIndex(5)
            else:
                self.ui.errorlbl.setText("Error: Not matched")
        else:
            # Check user
            if checkus == 0 or checkps == 0:
                self.ui.errorlbl.setText("Error: Blank space detect")
            elif checkus == -1:
                self.ui.errorlbl.setText("Error: User not exist")
            elif checkps == -1:
                self.ui.errorlbl.setText("Incorrect password format")


# Widget index 2
class RegisterUI(LoginandRegisterBaseUI):
    def __init__(self):
        super(RegisterUI, self).__init__()
        self.ui.loginbt.setText("Register")
        # self.ui.backbt.clicked.connect(self.gobackMenu)
        self.ui.usernameLE.move(360, 130)
        self.ui.usernamelbl.move(220, 130)
        self.ui.passwordlbl.move(220, 190)
        self.ui.passwordLE.move(360, 190)
        self.ui.loginbt.move(410,430)
        self.additionalUI()
        self.errlbl_list = [self.erroruslbl,self.errorpslbl,self.errorcnlbl,self.errorbdlbl,self.errorpnlbl]
        self.ui.loginbt.clicked.connect(self.checkAll)

    def additionalUI(self):
        # Create confirmation label
        self.confirmationlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.confirmationlbl.setGeometry(QtCore.QRect(225, 250, 139, 31))
        self.confirmationlbl.setText("Confirmation")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setBold(True)
        font.setPointSize(11)
        self.confirmationlbl.setFont(font)
        self.confirmationlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmationlbl.setObjectName("confirmationlbl")
        # Create confirmation line edit
        self.confirmationLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.confirmationLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmationLE.setGeometry(QtCore.QRect(360, 250, 291, 31))
        font.setBold(False)
        font.setPointSize(16)
        self.confirmationLE.setFont(font)
        self.confirmationLE.setObjectName("confirmationLE")
        # Create birth date label
        self.bdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.bdlbl.setGeometry(QtCore.QRect(220, 310, 141, 31))
        self.bdlbl.setText("Birth date")
        self.bdlbl.setFont(font)
        self.bdlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.bdlbl.setObjectName("bdlbl")
        # Create birth date line edit
        self.bdLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.bdLE.setGeometry(QtCore.QRect(360, 310, 291, 31))
        self.bdLE.setFont(font)
        self.bdLE.setObjectName("bdLE")
        # Create phone number line edit
        self.pnLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.pnLE.setGeometry(QtCore.QRect(360, 370, 291, 31))
        self.pnLE.setFont(font)
        self.pnLE.setObjectName("pnLE")
        # Create phone number label
        self.pnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.pnlbl.setGeometry(QtCore.QRect(220, 370, 141, 31))
        self.pnlbl.setText("Phone num")
        self.pnlbl.setFont(font)
        self.pnlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pnlbl.setObjectName("pnlbl")
        # Create error user label
        self.erroruslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.erroruslbl.setStyleSheet("color: red;")
        self.erroruslbl.setGeometry(QtCore.QRect(660, 130, 321, 31))
        font.setPointSize(11)
        self.erroruslbl.setFont(font)
        self.erroruslbl.setObjectName("erroruslbl")
        # Create error password label
        self.errorpslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorpslbl.setStyleSheet("color: red;")
        self.errorpslbl.setGeometry(QtCore.QRect(660, 190, 321, 31))
        self.errorpslbl.setFont(font)
        self.errorpslbl.setObjectName("errorpslbl")
        # Create error confirmation label
        self.errorcnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorcnlbl.setStyleSheet("color: red;")
        self.errorcnlbl.setGeometry(QtCore.QRect(660, 250, 321, 31))
        self.errorcnlbl.setFont(font)
        self.errorcnlbl.setObjectName("errorcnlbl")
        # Create error birth date label
        self.errorbdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorbdlbl.setStyleSheet("color: red;")
        self.errorbdlbl.setGeometry(QtCore.QRect(660, 310, 321, 31))
        self.errorbdlbl.setFont(font)
        self.errorbdlbl.setObjectName("errorbdlbl")
        # Create error birth phonenumber label
        self.errorpnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorpnlbl.setStyleSheet("color: red;")
        self.errorpnlbl.setGeometry(QtCore.QRect(660, 370, 321, 31))
        self.errorpnlbl.setFont(font)
        self.errorpnlbl.setObjectName("errorpnlbl")
        # Create example birth date label
        self.exbdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.exbdlbl.setGeometry(QtCore.QRect(360, 279, 201, 31))
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.exbdlbl.setText("Example: 05/10")
        self.exbdlbl.setFont(font)
        # Create example phone number label
        self.expnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.expnlbl.setGeometry(QtCore.QRect(360, 340, 201, 31))
        self.expnlbl.setText("Example: 0875548888")
        self.expnlbl.setFont(font)
        # Create example password label
        self.expslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.expslbl.setGeometry(QtCore.QRect(360, 160, 291, 31))
        self.expslbl.setText("Must contain: 1 Capital 1 Alphabet 1 Digit")
        font.setPointSize(11)
        self.expslbl.setFont(font)

    def checkAll(self):
        self.checklist = [0, 0, 0, 0]
        self.clearText(self.errlbl_list)
        us = self.ui.usernameLE.text()
        ps = self.ui.passwordLE.text()
        cn = self.confirmationLE.text()
        bd = self.bdLE.text()
        pn = self.pnLE.text()
        checkus = self.checkUser(us)
        checkps = self.checkPasswordFormat(ps)
        checkcn = self.checkPasswordFormat(cn)
        checkbd = self.checkBDFormat(bd)
        checkpn = self.checkPN(pn)
        # Check user
        if checkus == 0:
            self.errlbl_list[0].setText("Error: Blank space detect")
        elif checkus == 1:
            self.errlbl_list[0].setText("Error: User already exist")
        else:
            self.checklist[0] = 1
        # Check format password
        if checkps == 0:
            self.errlbl_list[1].setText("Error: Blank space detect")
        elif checkps == -1:
            self.errlbl_list[1].setText("Error: Invalid format")
        else:
            # Check confirm
            if checkcn == 0:
                self.errlbl_list[2].setText("Error: Blank space detect")
            elif checkps == -1:
                self.errlbl_list[2].setText("Error: Invalid format")
            else:
                # If ps and confirm are the same
                if ps == cn:
                    self.checklist[1] = 1
                else:
                    self.errlbl_list[1].setText("Error: Not matched")
                    self.errlbl_list[2].setText("Error: Not matched")
        # Check birth date
        if checkbd == 0:
            self.errlbl_list[3].setText("Error: Blank space detect")
        elif checkbd == -1:
            self.errlbl_list[3].setText("Error: Invalid format")
        elif checkbd == -2:
            self.errlbl_list[3].setText("Error: Invalid Date")
        elif checkbd == -3:
            self.errlbl_list[3].setText("Error: Invalid Month")
        else:
            self.checklist[2] = 1
        # Check phone number
        if checkpn == 0:
            self.errlbl_list[4].setText("Error: Blank space detect")
        elif checkpn == -1:
            self.errlbl_list[4].setText("Error: Invalid format")
        elif checkpn == -2:
            self.errlbl_list[4].setText("Error: Already used")
        else:
            self.checklist[3] = 1
        if 0 not in self.checklist:
            DBedit().adddatabase(us,ps,bd,pn)
            successbox(f"Successfully registered as {us}")
            self.clearText(self.errlbl_list)
            self.clearText([self.ui.usernameLE,self.ui.passwordLE,self.confirmationLE,self.bdLE,self.pnLE])
            global player
            player = USER(us)
            widget.setCurrentIndex(3)


# Widget index 3
class ChangepicUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_changePic()
        self.ui.setupUi(self)
        self.ui.finishedbt.setEnabled(False)
        self.sourcephoto = f'temp\\temp.jpg'
        self.timer1 = QTimer()
        try:
            self.cap = cv2.VideoCapture(0)
        except:
            errorbox("Camera is unavailable")
            self.ui.liveviewbt.setEnabled(False)
            self.ui.takepicbt.setEnabled(False)
            self.ui.getpicbt.setEnabled(False)
        self.timer1.timeout.connect(self.viewCam)
        self.ui.skipbt.clicked.connect(self.skipclicked)
        self.ui.finishedbt.clicked.connect(self.finished)
        self.ui.liveviewbt.clicked.connect(self.viewCam)
        self.ui.takepicbt.clicked.connect(self.takeapic)
        self.ui.getpicbt.clicked.connect(self.selectpic)

    def skipclicked(self):
        confirmation = QMessageBox.question(self, 'Skip', "Do you want to skip?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.ui.previewlbl.setText("Preview")
            self.timer1.stop()
            widget.setCurrentIndex(5)

    def takeapic(self):
        self.ui.finishedbt.setEnabled(True)
        self.timer1.stop()
        ret, image = self.cap.read()
        if ret:
            cv2.imwrite(self.sourcephoto, image)
            self.ui.previewlbl.setPixmap(QtGui.QPixmap(self.sourcephoto))
        else:
            errorbox("Didn't found any camera")
            self.ui.liveviewbt.setEnabled(False)
            self.ui.takepicbt.setEnabled(False)
            self.ui.getpicbt.setEnabled(False)

    def viewCam(self):
        self.timer1.start()
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.previewlbl.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def selectpic(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','c:\\',"Image files (*.jpg *.png)")
        if fname != ('', ''):
            image = Image.open(fname[0])
            new_img = image.resize((640, 480))
            new_img.save("temp\\temp.jpg")
            self.ui.previewlbl.setPixmap(QtGui.QPixmap(self.sourcephoto))
            self.ui.finishedbt.setEnabled(True)

    def finished(self):
        confirmation = QMessageBox.question(self, 'Finishing setup', "Finished?", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if confirmation == QMessageBox.Yes:
            self.timer1.stop()
            global player
            image = Image.open(self.sourcephoto)
            image.save(f'profilepic\\{player.pnum}.jpg')
            DBedit().updateDatabase(player.us,"pic",f'profilepic\\{player.pnum}.jpg')
            widget.setCurrentIndex(5)


# Widget index 4
class ForgotpsUI(LoginandRegisterBaseUI):
    def __init__(self):
        super().__init__()
        self.ui.usernamelbl.move(240, 190)
        self.ui.usernameLE.move(380, 190)
        self.ui.passwordlbl.move(230, 340)
        self.ui.passwordLE.move(380, 340)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ui.passwordlbl.setFont(font)
        self.ui.passwordlbl.setText("New password")
        self.ui.loginbt.setFont(font)
        self.ui.loginbt.setText("Change password")
        self.ui.loginbt.move(400, 440)
        self.additional_UI()
        self.ui.loginbt.clicked.connect(self.changePS)

    def additional_UI(self):
        # Create Birth date line edit
        self.birthdateLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.birthdateLE.setGeometry(QtCore.QRect(380, 240, 291, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.birthdateLE.setFont(font)
        # Create Birth date line edit
        self.birthdateLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.birthdateLE.setGeometry(QtCore.QRect(380, 240, 291, 31))
        self.birthdateLE.setFont(font)
        # Create Birth date label
        self.birthdatelbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.birthdatelbl.setGeometry(QtCore.QRect(240, 240, 141, 31))
        font.setPointSize(16)
        self.birthdatelbl.setFont(font)
        self.birthdatelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.birthdatelbl.setText("Birth date")
        # Create Error User label
        self.erroruslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.erroruslbl.setGeometry(QtCore.QRect(680, 190, 311, 31))
        self.erroruslbl.setText("")
        self.erroruslbl.setStyleSheet("color: red;")
        # Create phone num label
        self.phonenumlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.phonenumlbl.setGeometry(QtCore.QRect(230, 290, 151, 31))
        font.setPointSize(14)
        self.phonenumlbl.setFont(font)
        self.phonenumlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.phonenumlbl.setText("Phone number")
        # Create phone num line edit
        self.phonenumLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.phonenumLE.setGeometry(QtCore.QRect(380, 290, 291, 31))
        font.setPointSize(16)
        self.phonenumLE.setFont(font)
        # Create confirm Line Edit
        self.confirmLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.confirmLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmLE.setGeometry(QtCore.QRect(380, 390, 291, 31))
        self.confirmLE.setFont(font)
        # Create confirm label
        self.confirmlabel = QtWidgets.QLabel(self.ui.centralwidget)
        self.confirmlabel.setGeometry(QtCore.QRect(230, 390, 151, 31))
        font.setPointSize(18)
        self.confirmlabel.setFont(font)
        self.confirmlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmlabel.setText("Confirm")
        # Create error new pass label
        self.errornewpslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errornewpslbl.setGeometry(QtCore.QRect(680, 340, 311, 31))
        self.errornewpslbl.setText("")
        self.errornewpslbl.setStyleSheet("color: red;")
        # Create error confrim label
        self.errorconfirmlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorconfirmlbl.setGeometry(QtCore.QRect(680, 390, 311, 31))
        self.errorconfirmlbl.setText("")
        self.errorconfirmlbl.setStyleSheet("color: red;")
        # Create Error User label
        self.erroruslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.erroruslbl.setGeometry(QtCore.QRect(680, 190, 311, 31))
        self.erroruslbl.setText("")
        self.erroruslbl.setStyleSheet("color: red;")
        # Create example password label
        self.expslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.expslbl.setGeometry(QtCore.QRect(380, 320, 281, 21))
        self.expslbl.setText("Must contain: 1 Capital 1 Alphabet 1 Digit")
        font.setPointSize(9)
        font = QtGui.QFont()
        self.expslbl.setFont(font)

    def gobackMenu(self):
        self.clearText([self.ui.usernameLE,self.ui.passwordLE,self.phonenumLE,self.birthdateLE,self.confirmLE])
        widget.setCurrentIndex(1)

    def changePS(self):
        us = self.ui.usernameLE.text()
        bd = self.birthdateLE.text()
        pn = self.phonenumLE.text()
        new_ps = self.ui.passwordLE.text()
        confirm = self.confirmLE.text()
        checkus = self.checkUser(us)
        checknew_ps = self.checkPasswordFormat(new_ps)
        checkcn = self.checkPasswordFormat(confirm)
        self.clearText([self.erroruslbl,self.errornewpslbl,self.errorconfirmlbl])
        if checkus == 0:
            self.erroruslbl.setText("Error: Blank space detect")
        elif checkus == -1:
            self.erroruslbl.setText("Error: User does not exist")
        else:
            if [bd,pn] == [DBedit().getitemDatabase(us,"bd"),DBedit().getitemDatabase(us,"pnum")]:
                if checknew_ps == 0:
                    self.errornewpslbl.setText("Error: Blank space detect")
                elif checknew_ps == -1:
                    self.errornewpslbl.setText("Error: Invalid format")
                else:
                    if checkcn == 0:
                        self.errorconfirmlbl.setText("Error: Blank space detect")
                    elif checkcn == -1:
                        self.errorconfirmlbl.setText("Error: Invalid format")
                    else:
                        if new_ps == confirm:
                            DBedit().updateDatabase(us, "password", new_ps)
                            successbox("Successfully changed your password")
                        else:
                            self.errornewpslbl.setText("Error: Not match")
            else:
                self.erroruslbl.setText("Error: Info is wrong!")





# Widget index 5
class MenuUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_menu()
        self.ui.setupUi(self)
        self.ui.backbt.clicked.connect(lambda x: widget.setCurrentIndex(0))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = "Guest"
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(EntUI())
    widget.addWidget(LoginUI())
    widget.addWidget(RegisterUI())
    widget.addWidget(ChangepicUI())
    widget.addWidget(ForgotpsUI())
    widget.addWidget(MenuUI())
    widget.setWindowTitle("2048")
    widget.setWindowIcon(QtGui.QIcon("sourcepic\\logo.png"))
    widget.setFixedSize(1000, 700)
    widget.show()
    sys.exit(app.exec_())


