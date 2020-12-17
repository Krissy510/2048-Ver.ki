import sys
# import os
import cv2
import sqlite3
from PIL import Image
from time import sleep
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QImage
from entui import *
from baseloginui import *
from changepicui import *
from menuui import *
from profileui import *
from leaderboard import *

class DBedit:
    @staticmethod
    def checkItemExist(item, type):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'SELECT {type} FROM player ')
        row = cur.fetchall()
        for value in row:
            if item == value[0]:
                return True
        return False

    @staticmethod
    def adddatabase(us,ps,bd,pn):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        sql = "INSERT OR IGNORE INTO player VALUES (?,?,?,?,0,NULL)"
        cur.execute(sql, (us, ps, bd, pn))
        con.commit()

    @staticmethod
    def getitemDatabase(us,type):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'SELECT username,{type} FROM player')
        row = cur.fetchall()
        for value in row:
            if us == value[0]:
                return value[1]

    @staticmethod
    def updateDatabase(us,type,new):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        sql = f"UPDATE player SET {type} = ? WHERE username = ?"
        cur.execute(sql,[new,us])
        con.commit()

    @staticmethod
    def getRank(us):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'SELECT username FROM player ORDER BY highscore DESC')
        row = cur.fetchall()
        rank = 1
        for value in row:
            if us == value[0]:
                return rank
            else:
                rank += 1


class USER:
    def __init__(self,us):
        self.us = us
        self.bd = DBedit().getitemDatabase(us,"bd")
        self.pnum = DBedit().getitemDatabase(us,"pnum")
        self.hscore = DBedit().getitemDatabase(us,"highscore")
        self.rank = DBedit().getRank(us)
        self.pic = DBedit().getitemDatabase(us,"pic")

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
        self.ui.loginbt.clicked.connect(lambda: widget.setCurrentIndex(1))
        self.ui.regisbt.clicked.connect(lambda: widget.setCurrentIndex(2))
        self.ui.guestbt.clicked.connect(self.gotomenu)
        self.ui.qtbt.clicked.connect(lambda leave: quit(0))

    def gotomenu(self):
        global player
        player = "Guest"
        widget.setCurrentIndex(4)


class LoginandRegisterBaseUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginsection()
        self.ui.setupUi(self)
        self.additionwidget()
        self.ui.backbt.clicked.connect(self.gobackEnt)

    @staticmethod
    def checkPasswordFormat(ps):
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

    @staticmethod
    def checkUser(us):
        if us != "" and " " not in us:
            if DBedit().checkItemExist(us,"username"):
                return 1
            else:
                return -1
        else:
            return 0

    def checkPassFormat(self,ps):
        if ps != "" and " " not in ps:
            if self.checkPasswordFormat(ps):
                return 1
            else:
                return -1
        else:
            return 0

    @staticmethod
    def checkBDFormat(bd):
        if bd != "" and  " " not in bd:
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
                            if bd[0] == 30 and bd[1] in [4,6,9,11,1,3,5,7,8,10,12]:
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

    @ staticmethod
    def checkPN(pn):
        if pn != "" and " " not in pn:
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

    def additionwidget(self):
        pass

    @staticmethod
    def clearText(label_list):
        for wg in label_list:
            wg.setText("")

    @staticmethod
    def gotoMenu():
        widget.setCurrentIndex(4)

    @staticmethod
    def gotoRegister():
        widget.setCurrentIndex(2)

    @staticmethod
    def gotoLogin():
        widget.setCurrentIndex(1)

    @staticmethod
    def gobackEnt():
        widget.setCurrentIndex(0)


# Widget index 1
class LoginUI(LoginandRegisterBaseUI):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.ui.loginbt.clicked.connect(self.loginbtPressed)


    def loginbtPressed(self):
        user = self.ui.usernameLE.text()
        ps = self.ui.passwordLE.text()
        self.clearText([self.ui.errorlbl])
        # Check user
        checkus = self.checkUser(user)
        checkps = self.checkPassFormat(ps)
        if checkus == 1 and checkps == 1:
            if ps == DBedit().getitemDatabase(user,"password"):
                self.clearText([self.ui.usernameLE,self.ui.passwordLE])
                successbox(f"Successfully login as {user}")
                global player
                player = USER(user)
                self.gotoMenu()
            else:
                self.ui.errorlbl.setText("Not matched")
        else:
            # Check user
            if checkus == 0 or checkps == 0:
                self.ui.errorlbl.setText("Blank space detect")
            elif checkus == -1:
                self.ui.errorlbl.setText("User not exist")
            elif checkps == -1:
                self.ui.errorlbl.setText("Incorrect password format")


    def gobackEnt(self):
        self.clearText([self.ui.usernameLE,self.ui.passwordLE,self.ui.errorlbl])
        super().gobackEnt()


# Widget index 2
class RegisterUI(LoginandRegisterBaseUI):
    def __init__(self):
        super(RegisterUI, self).__init__()
        self.editUI()
        self.additionwidget()
        self.errlbl_list = [self.erroruslbl,self.errorpslbl,self.errorcnlbl,self.errorbdlbl,self.errorpnlbl]
        self.ui.loginbt.clicked.connect(self.checkAll)

    def editUI(self):
        self.ui.loginbt.setText("Register")
        self.ui.usernameLE.move(360, 130)
        self.ui.usernamelbl.move(220, 130)
        self.ui.passwordlbl.move(220, 190)
        self.ui.passwordLE.move(360, 190)
        self.ui.loginbt.move(410, 430)

    def additionwidget(self):
        self.setUp_UI_label()
        self.setUp_UI_lineEdit()

    def setUp_UI_label(self):
        # Normal label
        # Create confirmation label
        self.confirmationlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.confirmationlbl.setGeometry(QtCore.QRect(225, 250, 139, 31))
        self.confirmationlbl.setText("Confirm")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.confirmationlbl.setFont(font)
        self.confirmationlbl.setAlignment(QtCore.Qt.AlignCenter)
        # Create birth date label
        self.bdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.bdlbl.setGeometry(QtCore.QRect(210, 310, 141, 31))
        self.bdlbl.setText("Birth date")
        self.bdlbl.setFont(font)
        self.bdlbl.setAlignment(QtCore.Qt.AlignCenter)
        # Create phone number label
        self.pnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.pnlbl.setGeometry(QtCore.QRect(220, 370, 141, 31))
        self.pnlbl.setText("Phone num")
        self.pnlbl.setFont(font)
        self.pnlbl.setAlignment(QtCore.Qt.AlignCenter)

        # Error label
        # Create error user label
        self.erroruslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.erroruslbl.setStyleSheet("color: red;")
        self.erroruslbl.setGeometry(QtCore.QRect(660, 130, 321, 31))
        font.setPointSize(9)
        self.erroruslbl.setFont(font)
        # Create error password label
        self.errorpslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorpslbl.setStyleSheet("color: red;")
        self.errorpslbl.setGeometry(QtCore.QRect(660, 190, 321, 31))
        self.errorpslbl.setFont(font)
        # Create error confirmation label
        self.errorcnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorcnlbl.setStyleSheet("color: red;")
        self.errorcnlbl.setGeometry(QtCore.QRect(660, 250, 321, 31))
        self.errorcnlbl.setFont(font)
        # Create error birth date label
        self.errorbdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorbdlbl.setStyleSheet("color: red;")
        self.errorbdlbl.setGeometry(QtCore.QRect(660, 310, 321, 31))
        self.errorbdlbl.setFont(font)
        # Create error birth phonenumber label
        self.errorpnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorpnlbl.setStyleSheet("color: red;")
        self.errorpnlbl.setGeometry(QtCore.QRect(660, 370, 321, 31))
        self.errorpnlbl.setFont(font)

        # Example label
        # Create example birth date label
        self.exbdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.exbdlbl.setGeometry(QtCore.QRect(360, 279, 201, 31))
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
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
        font.setPointSize(8)
        self.expslbl.setFont(font)

    def setUp_UI_lineEdit(self):
        # Create confirmation line edit
        self.confirmationLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.confirmationLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmationLE.setGeometry(QtCore.QRect(360, 250, 291, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.confirmationLE.setFont(font)
        # Create birth date line edit
        self.bdLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.bdLE.setGeometry(QtCore.QRect(360, 310, 291, 31))
        self.bdLE.setFont(font)
        # Create phone number line edit
        self.pnLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.pnLE.setGeometry(QtCore.QRect(360, 370, 291, 31))
        self.pnLE.setFont(font)

    def checkAll(self):
        self.checklist = [0, 0, 0, 0]
        self.clearText(self.errlbl_list)
        us = self.ui.usernameLE.text()
        ps = self.ui.passwordLE.text()
        cn = self.confirmationLE.text()
        bd = self.bdLE.text()
        pn = self.pnLE.text()
        checkus = self.checkUser(us)
        checkps = self.checkPassFormat(ps)
        checkcn = self.checkPassFormat(cn)
        checkbd = self.checkBDFormat(bd)
        checkpn = self.checkPN(pn)
        # Check user
        if checkus == 0:
            self.errlbl_list[0].setText("Blank space detect")
        elif checkus == 1:
            self.errlbl_list[0].setText("User already exist")
        else:
            self.checklist[0] = 1
        # Check format password
        if checkps == 0:
            self.errlbl_list[1].setText("Blank space detect")
        elif checkps == -1:
            self.errlbl_list[1].setText("Invalid format")
        else:
            # Check confirm
            if checkcn == 0:
                self.errlbl_list[2].setText("Blank space detect")
            elif checkps == -1:
                self.errlbl_list[2].setText("Invalid format")
            else:
                # If ps and confirm are the same
                if ps == cn:
                    self.checklist[1] = 1
                else:
                    self.errlbl_list[1].setText("Not matched")
                    self.errlbl_list[2].setText("Not matched")
        # Check birth date
        if checkbd == 0:
            self.errlbl_list[3].setText("Blank space detect")
        elif checkbd == -1:
            self.errlbl_list[3].setText("Invalid format")
        elif checkbd == -2:
            self.errlbl_list[3].setText("Invalid Date")
        elif checkbd == -3:
            self.errlbl_list[3].setText("Invalid Month")
        else:
            self.checklist[2] = 1
        # Check phone number
        if checkpn == 0:
            self.errlbl_list[4].setText("Blank space detect")
        elif checkpn == -1:
            self.errlbl_list[4].setText("Invalid format")
        elif checkpn == -2:
            self.errlbl_list[4].setText("Already used")
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

    def gobackEnt(self):
        self.clearText(self.errlbl_list)
        self.clearText([self.ui.usernameLE, self.ui.passwordLE, self.bdLE, self.pnLE, self.confirmationLE])
        super().gobackEnt()


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

    def forward(self):
        widget.setCurrentIndex(4)

    def skipclicked(self):
        confirmation = QMessageBox.question(self, 'Skip', "Do you want to skip?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.ui.previewlbl.setText("Preview")
            self.timer1.stop()
            self.forward()
            DBedit().updateDatabase(player.us, "pic", 'sourcepic\\player.jpg')

    def takeapic(self):
        self.timer1.stop()
        ret, image = self.cap.read()
        if ret:
            cv2.imwrite(self.sourcephoto, image)
            self.ui.previewlbl.setPixmap(QtGui.QPixmap(self.sourcephoto))
            self.ui.finishedbt.setEnabled(True)
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
        self.timer1.stop()
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
            player = USER(player.us)
            widget.setCurrentIndex(5)
            self.forward()

# Widget index 4
class MenuUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_menu()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.start()
        self.timer.timeout.connect(self.block_guest)
        self.ui.LeaderBbt.clicked.connect(lambda: widget.setCurrentIndex(9))
        self.ui.profilebt.clicked.connect(self.goto_prof)
        self.ui.changeAbt.clicked.connect(lambda: widget.setCurrentIndex(0))
        self.ui.quitbt.clicked.connect(lambda leave: quit(0))

    def block_guest(self):
        if player == "Guest":
            self.ui.profilebt.setEnabled(False)
        else:
            self.ui.profilebt.setEnabled(True)

    def goto_prof(self):
        if player == "Guest":
            errorbox("Guest isn't available for this feature.")
        else:
            widget.setCurrentIndex(5)

# Widget index 5
class ProfileUI(QWidget):
    def __init__(self):
        super(ProfileUI, self).__init__()
        # self.widget = QtWidgets.QStackedWidget()
        self.timer = QTimer()
        self.ui = Ui_profile()
        self.ui.setupUi(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_info_lbl)
        self.ui.refreshbt.clicked.connect(self.update_info_lbl)
        self.ui.backbt.clicked.connect(lambda: widget.setCurrentIndex(4))
        self.ui.epbt.clicked.connect(lambda: widget.setCurrentIndex(6))
        self.ui.cpbt.clicked.connect(lambda: widget.setCurrentIndex(7))
        self.ui.eibt.clicked.connect(lambda: widget.setCurrentIndex(8))

    def update_info_lbl(self):
        global player
        if player != "Guest":
            player = USER(player.us)
            self.ui.uslbl.setText(f"USERNAME: {player.us}")
            self.ui.bdlbl.setText(f"BIRTH DATE: {player.bd}")
            self.ui.pnlbl.setText(f"PHONE NUM: {player.pnum}")
            self.ui.hslbl.setText(f"HIGH SCORE: {player.hscore}")
            self.ui.ranklbl.setText(f"RANK: {player.rank}")
            if player.pic != None:
                image = Image.open(player.pic)
                new_img = image.resize((220, 220))
                new_img.save("temp\\temp2.jpg")
                self.ui.pplbl.setPixmap(QtGui.QPixmap("temp\\temp2.jpg"))


# Widget index 6
class SubChangepicUI(ChangepicUI):
    def forward(self):
        widget.setCurrentIndex(5)

# Widget index 7
class SubChangePassUI(LoginandRegisterBaseUI):
    def __init__(self):
        super().__init__()
        self.editUI()
        self.additional_UI()
        self.ui.backbt.clicked.connect(self.gotoLogin)
        self.ui.loginbt.clicked.connect(self.changePS)


    def gotoLogin(self):
        self.clearText([self.ui.passwordLE,self.confirmLE,self.ui.errorlbl])
        widget.setCurrentIndex(5)

    def editUI(self):
        self.ui.passwordlbl.move(230, 280)
        self.ui.passwordLE.move(380, 280)
        self.ui.usernameLE.hide()
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.ui.passwordlbl.setFont(font)
        self.ui.passwordLE.setFont(font)
        font.setPointSize(8)
        self.ui.errorlbl.setFont(font)
        self.ui.usernamelbl.setText("Old password")
        self.ui.usernamelbl.setFont(font)
        self.ui.passwordlbl.setText("New password")
        self.ui.loginbt.setFont(font)
        self.ui.loginbt.setText("Change password")
        self.ui.loginbt.move(400, 380)
        self.ui.errorlbl.move(680,280)

    def additional_UI(self):
        # Create example password label
        self.expslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.expslbl.setGeometry(QtCore.QRect(380, 240, 291, 51))
        self.expslbl.setText("Must contain: 1 Capital 1 Alphabet 1 Digit")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(8)
        self.expslbl.setFont(font)
        # Create confirm label
        self.confirmlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.confirmlbl.setGeometry(QtCore.QRect(255, 330, 141, 31))
        self.confirmlbl.setAlignment(QtCore.Qt.AlignCenter)
        font.setPointSize(10)
        self.confirmlbl.setFont(font)
        self.confirmlbl.setText("Confirm")
        # Create confirm line edit
        self.confirmLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.confirmLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmLE.setGeometry(QtCore.QRect(380, 330, 291, 31))
        self.confirmLE.setFont(font)
        # Create error password label
        self.errorpslbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorpslbl.setGeometry(QtCore.QRect(380, 200, 421, 31))
        font.setPointSize(12)
        self.errorpslbl.setFont(font)
        self.errorpslbl.setStyleSheet("color: red;")
        # Create password line edit
        self.oldpasswordLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.oldpasswordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldpasswordLE.setGeometry(QtCore.QRect(380, 200, 291, 31))
        self.oldpasswordLE.setFont(font)



    def changePS(self):
        global player
        if self.oldpasswordLE.text() == DBedit().getitemDatabase(player.us,"password"):
            new_ps = self.ui.passwordLE.text()
            check_ps = self.checkPassFormat(new_ps)
            con = self.confirmLE.text()
            check_cn = self.checkPassFormat(con)
            self.clearText([self.ui.errorlbl,self.errorpslbl])
            if new_ps == 0 or check_cn == 0:
                self.ui.errorlbl.setText("Blank space detect")
            elif new_ps == -1 or check_cn == -1:
                self.ui.errorlbl.setText("Invalid Format")
            else:
                self.clearText([self.ui.passwordLE, self.confirmLE,self.oldpasswordLE])
                DBedit().updateDatabase(player.us, "password", new_ps)
                successbox("Successfully changed the password.")
        else:
            self.errorpslbl.setText("Incorrect")

# Widget index 8
class EditInfoUI(LoginandRegisterBaseUI):
    def __init__(self):
        super(EditInfoUI, self).__init__()
        self.ui.usernamelbl.hide()
        self.ui.usernameLE.hide()
        self.ui.passwordlbl.hide()
        self.ui.passwordLE.hide()
        self.ui.loginbt.move(410, 430)
        self.additionwidget()
        self.ui.loginbt.setText("Change")
        self.ui.backbt.clicked.connect(self.back)
        self.ui.loginbt.clicked.connect(self.change)

    def back(self):
        self.clearText([self.confirmationLE,self.pnLE,self.bdLE])
        widget.setCurrentIndex(5)

    def additionwidget(self):
        self.setUp_UI_label()
        self.setUp_UI_lineEdit()

    def setUp_UI_label(self):
        # Normal label
        # Create confirmation label
        self.confirmationlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.confirmationlbl.setGeometry(QtCore.QRect(225, 250, 139, 31))
        self.confirmationlbl.setText("Confirm")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.confirmationlbl.setFont(font)
        self.confirmationlbl.setAlignment(QtCore.Qt.AlignCenter)
        # Create birth date label
        self.bdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.bdlbl.setGeometry(QtCore.QRect(210, 310, 141, 31))
        self.bdlbl.setText("Birth date")
        self.bdlbl.setFont(font)
        self.bdlbl.setAlignment(QtCore.Qt.AlignCenter)
        # Create phone number label
        self.pnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.pnlbl.setGeometry(QtCore.QRect(220, 370, 141, 31))
        self.pnlbl.setText("Phone num")
        self.pnlbl.setFont(font)
        self.pnlbl.setAlignment(QtCore.Qt.AlignCenter)

        # Error label
        # Create error confirmation label
        self.errorcnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorcnlbl.setStyleSheet("color: red;")
        self.errorcnlbl.setGeometry(QtCore.QRect(660, 250, 321, 31))
        self.errorcnlbl.setFont(font)
        # Create error birth date label
        self.errorbdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorbdlbl.setStyleSheet("color: red;")
        self.errorbdlbl.setGeometry(QtCore.QRect(660, 310, 321, 31))
        self.errorbdlbl.setFont(font)
        # Create error birth phonenumber label
        self.errorpnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.errorpnlbl.setStyleSheet("color: red;")
        self.errorpnlbl.setGeometry(QtCore.QRect(660, 370, 321, 31))
        self.errorpnlbl.setFont(font)

        # Example label
        # Create example birth date label
        self.exbdlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.exbdlbl.setGeometry(QtCore.QRect(360, 279, 201, 31))
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.exbdlbl.setText("Example: 05/10")
        self.exbdlbl.setFont(font)
        # Create example phone number label
        self.expnlbl = QtWidgets.QLabel(self.ui.centralwidget)
        self.expnlbl.setGeometry(QtCore.QRect(360, 340, 201, 31))
        self.expnlbl.setText("Example: 0875548888")
        self.expnlbl.setFont(font)

    def setUp_UI_lineEdit(self):
        # Create confirmation line edit
        self.confirmationLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.confirmationLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmationLE.setGeometry(QtCore.QRect(360, 250, 291, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.confirmationLE.setFont(font)
        # Create birth date line edit
        self.bdLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.bdLE.setGeometry(QtCore.QRect(360, 310, 291, 31))
        self.bdLE.setFont(font)
        # Create phone number line edit
        self.pnLE = QtWidgets.QLineEdit(self.ui.centralwidget)
        self.pnLE.setGeometry(QtCore.QRect(360, 370, 291, 31))
        self.pnLE.setFont(font)

    def change(self):
        global player
        checklist = [0, 0, 0]
        self.clearText([self.errorcnlbl,self.errorbdlbl,self.errorpnlbl])
        cn = self.confirmationLE.text()
        bd = self.bdLE.text()
        pn = self.pnLE.text()
        check = self.checkPassFormat(cn)
        checkbd = self.checkBDFormat(bd)
        checkpn = self.checkPN(pn)
        if check == 0:
            self.errorcnlbl.setText("Blank space detect")
        elif check == -1:
            self.errorcnlbl.setText("Invalid format")
        else:
            if cn == DBedit().getitemDatabase(player.us,"password"):
                checklist[0] = 1
            else:
                self.errorcnlbl.setText("Not match")
        # Check birth date
        if checkbd == -1:
            self.errorbdlbl.setText("Invalid format")
        elif checkbd == -2:
            self.errorbdlbl.setText("Invalid Date")
        elif checkbd == -3:
            self.errorbdlbl.setText("Invalid Month")
        elif checkbd == 1:
            checklist[1] = 1
        # Check phone number
        if checkpn == -1:
            self.errorpnlbl.setText("Invalid format")
        elif checkpn == -2:
            self.errorpnlbl.setText("Already used")
        elif checkpn == 1:
            checklist[2] = 1

        if checklist[0] == 1:
            if checklist[1] == 1:
                DBedit.updateDatabase(player.us,"bd",bd)
            if checklist[2] == 1:
                DBedit.updateDatabase(player.us, "pnum", pn)
            self.clearText([self.confirmationLE, self.pnLE, self.bdLE])
            successbox("Successfully update database!")

# Widget index 9
class LeaderboardUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_leaderboard()
        self.ui.setupUi(self)
        self.ui.backbt.clicked.connect(lambda: widget.setCurrentIndex(4))
        self.setTextWidget()
        self.imagelbl_list = [self.ui.rank, self.ui.rank_2, self.ui.rank_3, self.ui.rank_4, self.ui.rank_5, self.ui.rank_6, self.ui.rank_7, self.ui.rank_8, self.ui.rank_9, self.ui.rank_10]
        self.lbl_list = [self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5, self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_9, self.ui.label_10]
        self.setinfo()

    def setTextWidget(self):
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.ui.backbt.setFont(font)
        self.ui.backbt.setText("Back")

    def setinfo(self):
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        cur.execute(f'SELECT username FROM player ORDER BY highscore DESC')
        for i in range(10):
            row = cur.fetchone()
            if row != None:
                path_pic = DBedit().getitemDatabase(row[0], "pic")
                rank = DBedit().getRank(row[0])
                hsc = DBedit().getitemDatabase(row[0], "highscore")
                image = Image.open(path_pic)
                new_img = image.resize((100, 92))
                new_img.save("temp\\temp3.jpg")
                self.imagelbl_list[i].setPixmap(QtGui.QPixmap("temp\\temp3.jpg"))
                self.lbl_list[i].setText(f"RANK: {rank}\nUSER: {row[0]}\nHIGH SCORE:{hsc}")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = "Guest"
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(EntUI())               # 0
    widget.addWidget(LoginUI())             # 1
    widget.addWidget(RegisterUI())          # 2
    widget.addWidget(ChangepicUI())         # 3
    widget.addWidget(MenuUI())              # 4
    widget.addWidget(ProfileUI())           # 5
    widget.addWidget(SubChangepicUI())      # 6
    widget.addWidget(SubChangePassUI())     # 7
    widget.addWidget(EditInfoUI())          # 8
    widget.addWidget(LeaderboardUI())       # 9
    widget.setWindowTitle("2048")
    widget.setWindowIcon(QtGui.QIcon("sourcepic\\logo.png"))
    widget.setFixedSize(1000, 700)
    widget.show()
    sys.exit(app.exec_())


