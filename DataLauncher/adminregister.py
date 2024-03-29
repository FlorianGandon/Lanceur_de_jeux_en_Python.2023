from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog

class AdminRegister(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(550, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("* {\n"
"background-color: #424242;\n"
"font: 10pt \"3ds\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: #3C8F90;\n"
"border: 1px solid white;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"font: 10pt \"3ds\";\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"background-color: #3C8F90;\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #368383;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #368377;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.LabelPassword = QtWidgets.QLabel(parent=self)
        self.LabelPassword.setFixedHeight(40)
        self.gridLayout.addWidget(self.LabelPassword, 2, 0, 1, 1)
        self.InputUsername = QtWidgets.QLineEdit(parent=self)
        self.InputUsername.setFixedHeight(40)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InputUsername.setFont(font)
        self.InputUsername.setMaxLength(20)
        self.InputUsername.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputUsername.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.InputUsername, 1, 1, 1, 3)
        self.Inputemail = QtWidgets.QLineEdit(parent=self)
        self.Inputemail.setFixedHeight(40)
        self.Inputemail.setMaxLength(60)
        self.Inputemail.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Inputemail.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.Inputemail, 4, 1, 1, 3)
        self.RegisterButton = QtWidgets.QPushButton(parent=self)
        self.RegisterButton.setFixedHeight(40)
        self.gridLayout.addWidget(self.RegisterButton, 7, 3, 1, 1)
        self.LabelUsername = QtWidgets.QLabel(parent=self)
        self.LabelUsername.setFixedHeight(40)
        self.LabelUsername.setFocus()
        self.gridLayout.addWidget(self.LabelUsername, 1, 0, 1, 1)
        self.LabelGrade = QtWidgets.QLabel(parent=self)
        self.LabelGrade.setFixedHeight(40)
        self.gridLayout.addWidget(self.LabelGrade, 5, 0, 1, 1)
        self.LabelEmail = QtWidgets.QLabel(parent=self)
        self.LabelEmail.setFixedHeight(40)
        self.gridLayout.addWidget(self.LabelEmail, 4, 0, 1, 1)
        self.InputConfirmPassword = QtWidgets.QLineEdit(parent=self)
        self.InputConfirmPassword.setFixedHeight(40)
        self.InputConfirmPassword.setMaxLength(30)
        self.InputConfirmPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.InputConfirmPassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputConfirmPassword.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.InputConfirmPassword, 3, 1, 1, 3)
        self.LabelConfirmPassword = QtWidgets.QLabel(parent=self)
        self.LabelConfirmPassword.setFixedHeight(40)
        self.gridLayout.addWidget(self.LabelConfirmPassword, 3, 0, 1, 1)
        self.InputPassword = QtWidgets.QLineEdit(parent=self)
        self.InputPassword.setFixedHeight(40)
        self.InputPassword.setMaxLength(30)
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.InputPassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputPassword.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.InputPassword, 2, 1, 1, 3)
        self.CancelButton = QtWidgets.QPushButton(parent=self)
        self.CancelButton.setFixedHeight(40)
        self.CancelButton.setStyleSheet("QPushButton {\n"
"background:none;\n"
"color: #3C8F90;\n"
"border: 2px solid #3C8F90;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #368383;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #368377;\n"
"}")
        self.gridLayout.addWidget(self.CancelButton, 7, 2, 1, 1)
        self.InputGade = QtWidgets.QLineEdit(parent=self)
        self.InputGade.setFixedHeight(40)
        self.InputGade.setMaxLength(40)
        self.InputGade.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputGade.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.InputGade, 5, 1, 1, 3)
        self.LabelError = QtWidgets.QLabel(parent=self)
        self.LabelError.setFixedHeight(25)
        self.LabelError.setStyleSheet("border: none;\n"
"color: #c5001a;\n"
"font: italic;\n"
"background: none;")
        self.LabelError.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.LabelError.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridLayout.addWidget(self.LabelError, 6, 1, 1, 3)

        self.setText()
        self.setTabOrder(self.InputUsername, self.InputPassword)
        self.setTabOrder(self.InputPassword, self.InputConfirmPassword)
        self.setTabOrder(self.InputConfirmPassword, self.Inputemail)
        self.setTabOrder(self.Inputemail, self.InputGade)
        self.setTabOrder(self.InputGade, self.RegisterButton)
        self.setTabOrder(self.RegisterButton, self.CancelButton)
        self.setTabOrder(self.CancelButton, self.LabelUsername)

    def setText(self):
        self.setWindowTitle("Create an acount")
        self.LabelPassword.setText("Password : ")
        self.RegisterButton.setText("  Create an acount  ")
        self.LabelUsername.setText("Username : ")
        self.LabelGrade.setText("Grade :")
        self.LabelEmail.setText("Email :")
        self.LabelConfirmPassword.setText("Password \n"
"confirm :")
        self.CancelButton.setText("Cancel")
        self.LabelError.setText("")
        self.LabelError.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = AdminRegister()
    windows.show()
    sys.exit(app.exec())
