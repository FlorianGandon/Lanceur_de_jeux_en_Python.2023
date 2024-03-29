from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class RegisterScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 530)
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
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.RegisterWidget = QtWidgets.QWidget(parent=self)
        self.RegisterWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.RegisterWidget)
        self.Titre = QtWidgets.QLabel(parent=self.RegisterWidget)
        self.Titre.setFixedHeight(80)
        self.Titre.setFocus()
        self.Titre.setStyleSheet("font: 15pt \"3ds\";\n"
"font-weight: bold;")
        self.Titre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.Titre)
        self.RegisterForm = QtWidgets.QGroupBox(parent=self.RegisterWidget)
        self.RegisterForm.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.RegisterForm.setStyleSheet("QGroupBox {\n"
"border: 1px solid white;\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.RegisterForm.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.RegisterForm)
        self.LabelUsername = QtWidgets.QLabel(parent=self.RegisterForm)
        self.LabelUsername.setFixedHeight(40)
        self.gridLayout_2.addWidget(self.LabelUsername, 1, 0, 1, 1)
        self.InputConfirmPassword = QtWidgets.QLineEdit(parent=self.RegisterForm)
        self.InputConfirmPassword.setFixedHeight(40)
        self.InputConfirmPassword.setMaxLength(30)
        self.InputConfirmPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.InputConfirmPassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputConfirmPassword.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.InputConfirmPassword, 4, 1, 1, 1)
        self.InputUsername = QtWidgets.QLineEdit(parent=self.RegisterForm)
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
        self.gridLayout_2.addWidget(self.InputUsername, 1, 1, 1, 1)
        self.LabelError = QtWidgets.QLabel(parent=self.RegisterForm)
        self.LabelError.setFixedHeight(40)
        self.LabelError.setStyleSheet("border: none;\n"
"color: #c5001a;\n"
"font: italic;\n"
"background: none;")
        self.LabelError.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.LabelError.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.gridLayout_2.addWidget(self.LabelError, 0, 0, 1, 2)
        self.ButtonRegister = QtWidgets.QPushButton(parent=self.RegisterForm)
        self.ButtonRegister.setFixedHeight(40)
        self.ButtonRegister.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.gridLayout_2.addWidget(self.ButtonRegister, 7, 0, 1, 2)
        self.LabelConfirmPassword = QtWidgets.QLabel(parent=self.RegisterForm)
        self.LabelConfirmPassword.setFixedHeight(40)
        self.gridLayout_2.addWidget(self.LabelConfirmPassword, 4, 0, 1, 1)
        self.Inputemail = QtWidgets.QLineEdit(parent=self.RegisterForm)
        self.Inputemail.setFixedHeight(40)
        self.Inputemail.setMaxLength(60)
        self.Inputemail.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.Inputemail.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Inputemail.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.Inputemail, 5, 1, 1, 1)
        self.LabelPassword = QtWidgets.QLabel(parent=self.RegisterForm)
        self.LabelPassword.setFixedHeight(40)
        self.gridLayout_2.addWidget(self.LabelPassword, 3, 0, 1, 1)
        self.InputPassword = QtWidgets.QLineEdit(parent=self.RegisterForm)
        self.InputPassword.setFixedHeight(40)
        self.InputPassword.setMaxLength(30)
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.InputPassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputPassword.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.InputPassword, 3, 1, 1, 1)
        self.LabelEmail = QtWidgets.QLabel(parent=self.RegisterForm)
        self.LabelEmail.setFixedHeight(40)
        self.gridLayout_2.addWidget(self.LabelEmail, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.RegisterForm)
        self.LabelAcount = QtWidgets.QLabel(parent=self.RegisterWidget)
        self.LabelAcount.setFixedHeight(40)
        self.LabelAcount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.LabelAcount)
        self.ButtonLogin = QtWidgets.QPushButton(parent=self.RegisterWidget)
        self.ButtonLogin.setEnabled(True)
        self.ButtonLogin.setFixedHeight(40)
        self.verticalLayout.addWidget(self.ButtonLogin)
        self.gridLayout.addWidget(self.RegisterWidget, 0, 1, 1, 1)

        self.setText()
        self.setTabOrder(self.InputUsername, self.InputPassword)
        self.setTabOrder(self.InputPassword, self.InputConfirmPassword)
        self.setTabOrder(self.InputConfirmPassword, self.Inputemail)
        self.setTabOrder(self.Inputemail, self.ButtonRegister)
        self.setTabOrder(self.ButtonRegister, self.ButtonLogin)
        self.setTabOrder(self.ButtonLogin, self.Titre)

    def setText(self):
        self.Titre.setText("OmegaGames Launcher")
        self.RegisterForm.setTitle("Register From :")
        self.LabelUsername.setText("Username : ")
        self.LabelError.setText("Wrong password")
        self.ButtonRegister.setText("Create a free acount !")
        self.ButtonRegister.setShortcut("Return")
        self.LabelConfirmPassword.setText("Password \nconfirm :")
        self.LabelPassword.setText("Password : ")
        self.LabelEmail.setText("Email :")
        self.LabelAcount.setText("Have an acount ?")
        self.ButtonLogin.setText("Login !")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = RegisterScreen()
    windows.show()
    sys.exit(app.exec())
