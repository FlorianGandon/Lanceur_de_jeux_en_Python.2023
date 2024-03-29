from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        #self.resize(800, 530)
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
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.LoginWidget = QtWidgets.QWidget(parent=self)
        self.LoginWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.LoginWidget)
        self.Titre = QtWidgets.QLabel(parent=self.LoginWidget)
        self.Titre.setFixedHeight(80)
        self.Titre.setFocus()
        self.Titre.setStyleSheet("font: 15pt \"3ds\";\n"
"font-weight: bold;")
        self.Titre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3.addWidget(self.Titre, 0, 0, 1, 1)
        self.LoginForm = QtWidgets.QGroupBox(parent=self.LoginWidget)
        self.LoginForm.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.LoginForm.setStyleSheet("QGroupBox {\n"
"border: 1px solid white;\n"
"border-radius:10px;\n"
"color: white;\n"
"}")
        self.LoginForm.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.LoginForm)
        self.InputPassword = QtWidgets.QLineEdit(parent=self.LoginForm)
        self.InputPassword.setFixedHeight(40)
        self.InputPassword.setMaxLength(30)
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.InputPassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputPassword.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.InputPassword, 3, 1, 1, 1)
        self.InputUsername = QtWidgets.QLineEdit(parent=self.LoginForm)
        self.InputUsername.setFixedHeight(40)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InputUsername.setFont(font)
        self.InputUsername.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.InputUsername.setMaxLength(20)
        self.InputUsername.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InputUsername.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.InputUsername, 1, 1, 1, 1)
        self.LabelUsername = QtWidgets.QLabel(parent=self.LoginForm)
        self.LabelUsername.setFixedHeight(40)
        self.gridLayout_2.addWidget(self.LabelUsername, 1, 0, 1, 1)
        self.LabelPassword = QtWidgets.QLabel(parent=self.LoginForm)
        self.LabelPassword.setFixedHeight(40)
        self.gridLayout_2.addWidget(self.LabelPassword, 3, 0, 1, 1)
        self.ButtonLogin = QtWidgets.QPushButton(parent=self.LoginForm)
        self.ButtonLogin.setFixedHeight(40)
        self.ButtonLogin.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.gridLayout_2.addWidget(self.ButtonLogin, 5, 0, 1, 2)
        self.LabelError = QtWidgets.QLabel(parent=self.LoginForm)
        self.LabelError.setFixedHeight(40)
        self.LabelError.setStyleSheet("border: none;\n"
"color: #c5001a;\n"
"font: italic;\n"
"background: none;")
        self.LabelError.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.LabelError.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.gridLayout_2.addWidget(self.LabelError, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.LoginForm, 1, 0, 1, 1)
        self.LabelRegister = QtWidgets.QLabel(parent=self.LoginWidget)
        self.LabelRegister.setFixedHeight(40)
        self.LabelRegister.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3.addWidget(self.LabelRegister, 2, 0, 1, 1)
        self.ButtonRegister = QtWidgets.QPushButton(parent=self.LoginWidget)
        self.ButtonRegister.setFixedHeight(40)
        self.gridLayout_3.addWidget(self.ButtonRegister, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.LoginWidget, 0, 1, 1, 1)

        self.setText()
        self.setTabOrder(self.InputUsername, self.InputPassword)
        self.setTabOrder(self.InputPassword, self.ButtonLogin)
        self.setTabOrder(self.ButtonLogin, self.ButtonRegister)

    def setText(self):
        self.Titre.setText("OmegaGames Launcher")
        self.LoginForm.setTitle("Login From :")
        self.LabelUsername.setText("Username : ")
        self.LabelPassword.setText("Password : ")
        self.ButtonLogin.setText("Login !")
        self.ButtonLogin.setShortcut("Return")
        self.LabelError.setText("Wrong password")
        self.LabelRegister.setText("Don\'t have an acount ?")
        self.ButtonRegister.setText("Create a free acount")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = LoginScreen()
    windows.show()
    sys.exit(app.exec())
