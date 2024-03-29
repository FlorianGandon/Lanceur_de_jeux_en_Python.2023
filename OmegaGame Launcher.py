import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication, QVBoxLayout
from PyQt6 import QtGui

from DataLauncher.login import LoginScreen
from DataLauncher.register import RegisterScreen
from DataLauncher.choose import SelectScreen
from DataLauncher.adminregister import AdminRegister

from DataLauncher.checkdata import check_email, check_password, check_username
from database_handler import DatabaseHandler


admin_key = "UnChatRoux"
#https://game-icons.net/

class Windows(QWidget):

    def __init__(self):
        super().__init__()
        
        # set Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        # set Title
        self.setWindowTitle("OmegaGames Launcher")
        
        # set  Widget
        self.verticalLayout = QVBoxLayout(self)
        self.widget = QWidget(self)
        self.setStyleSheet("* {\n"
"background-color: #424242;\n"
"}")
        
        self.init_LoginScreen()
        self.init_RegisterScreen()
        self.init_SelectSreen()
        
        # add Widget      
        self.verticalLayout.addWidget(self.LoginScreen)
        
        self.setFixedSize(900,500)
        #self.setFixedSize(1200,800)
        #self.resize(800,500)
        
        
        self.database_handler = DatabaseHandler("\\databases\\OmegaUsers.db")
        self.user = None

    def LoginToRegister(self):
        self.LoginScreen.setParent(None)
        self.verticalLayout.removeWidget(self.LoginScreen)
        self.LoginScreen.setParent(self)
        self.verticalLayout.addWidget(self.RegisterScreen)
        self.RegisterScreen.LabelError.setText("")
        self.RegisterScreen.LabelError.hide()
        
    def RegisterToLogin(self):
        self.RegisterScreen.setParent(None)
        self.verticalLayout.removeWidget(self.RegisterScreen)
        self.RegisterScreen.setParent(self)
        self.verticalLayout.addWidget(self.LoginScreen)
        self.LoginScreen.LabelError.setText("")
        self.LoginScreen.LabelError.hide()

    def SelectToLogin(self):
        self.SelectScreen.setParent(None)
        self.verticalLayout.removeWidget(self.SelectScreen)
        self.SelectScreen.setParent(self)
        self.verticalLayout.addWidget(self.LoginScreen)
        self.LoginScreen.LabelError.setText("")
        
        self.LoginScreen.LabelError.hide()
        self.user = None

    def LoginToSelect(self):
        self.LoginScreen.setParent(None)
        self.verticalLayout.removeWidget(self.LoginScreen)
        self.LoginScreen.setParent(self)
        self.verticalLayout.addWidget(self.SelectScreen)
        
        self.SelectScreen.LabelWelcome.setText("Bienvenue " + self.user["username"])
    
    def RegisterToSelect(self):
        self.RegisterScreen.setParent(None)
        self.verticalLayout.removeWidget(self.RegisterScreen)
        self.RegisterScreen.setParent(self)
        self.verticalLayout.addWidget(self.SelectScreen)
        
        self.SelectScreen.LabelWelcome.setText("Bienvenue " + self.user["username"])

    def closeEvent(self, event):
        reply = QMessageBox.warning(self, 'Alert',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    
    def init_LoginScreen(self):
        self.LoginScreen = LoginScreen()
        self.LoginScreen.ButtonRegister.clicked.connect(self.LoginToRegister)
        self.LoginScreen.ButtonLogin.clicked.connect(self.check_login)
        self.LoginScreen.LabelError.hide()
    
    def init_RegisterScreen(self):
        self.RegisterScreen = RegisterScreen()
        self.RegisterScreen.ButtonLogin.clicked.connect(self.RegisterToLogin)
        self.RegisterScreen.ButtonRegister.clicked.connect(lambda : self.check_register(self.RegisterScreen))
        self.RegisterScreen.LabelError.hide()
    
    def init_SelectSreen(self):
        self.SelectScreen = SelectScreen()
        self.SelectScreen.PlayButton.clicked.connect(self.PlayGame)
        self.SelectScreen.ImageSettings.clicked.connect(self.SelectToLogin)
    
    def PlayGame(self):
        #self.close()
        self.hide()
        selected_game = self.SelectScreen.proposegames[self.SelectScreen.main_game][0]
        game = self.SelectScreen.games.get(selected_game)
        try:
            game.init(self.user)
            game.run()
        except:
            game = None
        finally:
            self.show()

    def check_register(self, screen, admin = False):
        Username = screen.InputUsername.text()
        Password = screen.InputPassword.text()
        ConfirmPassword = screen.InputConfirmPassword.text()
        Email = screen.Inputemail.text()
        
        if admin:
            Grade = self.AdminRegisterScreen.InputGade.text()
            
        
        if Username == "" and Password == admin_key and ConfirmPassword == admin_key and Email == "" and not admin:
            self.clear_input_register()
            self.AdminRegisterScreen = AdminRegister()
            self.AdminRegisterScreen.CancelButton.clicked.connect(self.AdminRegisterScreen.close)
            self.AdminRegisterScreen.RegisterButton.clicked.connect(lambda : self.check_register(self.AdminRegisterScreen, True))
            self.AdminRegisterScreen.exec()
        else:
            try:
                if admin:
                    #assert len(Grade) > 3, 
                    Gade_assert = Grade.lower()
                    print(Gade_assert, Grade)
                    assert Gade_assert == "master", "You can't be the Master"
                assert check_username(Username) == True, check_username(Username)
                assert check_password(Password) == True, check_password(Password)
                assert Password == ConfirmPassword, "The two password are different."
                assert check_email(Email) == True, check_email(Email)
                screen.LabelError.hide()
                screen.LabelError.setText("")
                if admin:
                    adduser = self.database_handler.add_user(Username, Password, Email, Grade, admin)
                else :
                    adduser = self.database_handler.add_user(Username, Password, Email)
                if not adduser[0]:
                    screen.LabelError.show()
                    screen.LabelError.setText(adduser[1])
                else:
                    self.clear_input_register()
                    self.user = self.database_handler.get_data(int(adduser[1]))
                    self.RegisterToSelect()
            except AssertionError as error:
                screen.LabelError.show()
                screen.LabelError.setText(str(error))
                
            
    def check_login(self):
        self.LoginScreen.LabelError.hide()
        self.LoginScreen.LabelError.setText("")
        Username = self.LoginScreen.InputUsername.text()
        Password = self.LoginScreen.InputPassword.text()
        LoginUser = self.database_handler.check_login(Username, Password)
        if not LoginUser[0]:
            self.LoginScreen.LabelError.show()
            self.LoginScreen.LabelError.setText(LoginUser[1])
        else:
            self.clear_input_login()
            self.user = self.database_handler.get_data(int(LoginUser[1]))
            self.LoginToSelect()

    def clear_input_register(self):
        self.RegisterScreen.InputUsername.setText("")
        self.RegisterScreen.InputPassword.setText("")
        self.RegisterScreen.InputConfirmPassword.setText("")
        self.RegisterScreen.Inputemail.setText("")
    
    def clear_input_login(self):
        self.LoginScreen.InputUsername.setText("")
        self.LoginScreen.InputPassword.setText("")
    

def main():
    global Windows
    app = QApplication(sys.argv)
    Windows = Windows()
    Windows.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()