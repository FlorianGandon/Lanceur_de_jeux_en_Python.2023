from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget

from MiningGame import MiningGame
from PoliceGame import PoliceGame
from SpaceGame import SpaceGame
from VillageGame import VillageGame

class SelectScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        self.proposegames = [["Mining Game", "./images/MiningGame.ico"], ["Police Game", "./images/PoliceGame.ico"], ["Space Game", "./images/SpaceGame.ico"], ["Village Game", "./images/VillageGame.ico"]]
        self.games = {"Mining Game": MiningGame(), "Police Game": PoliceGame(), "Space Game": SpaceGame(), "Village Game": VillageGame()}
        self.main_game = 0
        self.nb_game = 4
        
        self.setObjectName("Form")
        self.resize(800, 530)
        self.setStyleSheet("* {\n"
"background-color: #424242;\n"
"font: 10pt \"3ds\";\n"
"font-weight: bold;\n"
"border:none;\n"
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
        self.MainGame = QtWidgets.QLabel(parent=self)
        self.MainGame.setFixedSize(210, 210)
        self.MainGame.setPixmap(QtGui.QPixmap("D:\\Projet Python\\ui\\../../Omega Games/images/MiningGame.ico"))
        self.MainGame.setScaledContents(True)
        #self.gridLayout.addWidget(self.MainGame, 1, 2, 1, 1,QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.DataGame = QtWidgets.QFrame(parent=self)
        self.DataGame.setFixedWidth(400)
        self.DataGame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.DataGame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DataGame)
        self.GameTitle = QtWidgets.QLabel(parent=self.DataGame)
        self.GameTitle.setFixedHeight(40)
        self.GameTitle.setStyleSheet("QLabel {\n"
"font: 12pt;\n"
"}")
        self.GameTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.GameTitle)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.DataGame)
        self.scrollArea.setFixedWidth(380)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("border: 1px solid white;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 357, 256))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(2, 2, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.LegendGame = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.LegendGame.setStyleSheet("QLabel {\n"
"font: 8pt;border:none;\n"
"}")
        self.LegendGame.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.verticalLayout_2.addWidget(self.LegendGame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.PlayButton = QtWidgets.QPushButton(parent=self.DataGame)
        self.PlayButton.setFixedHeight(40)
        self.verticalLayout.addWidget(self.PlayButton)
        #self.gridLayout.addWidget(self.DataGame, 2, 2, 1, 1)
        self.ImageLeftGame = QtWidgets.QLabel(parent=self)
        self.ImageLeftGame.setMinimumSize(QtCore.QSize(150, 150))
        self.ImageLeftGame.setMaximumSize(QtCore.QSize(150, 150))
        self.ImageLeftGame.setPixmap(QtGui.QPixmap("D:\\Projet Python\\ui\\../../Omega Games/images/icon.ico"))
        self.ImageLeftGame.setScaledContents(True)
        #self.gridLayout.addWidget(self.ImageLeftGame, 1, 1, 1, 1)
        self.LeftButton = QtWidgets.QPushButton(parent=self)
        self.LeftButton.setFixedSize(60,200)
        self.LeftButton.setStyleSheet("QPushButton {\n"
"background:none;\n"
"color: #3C8F90;\n"
"border: 2px solid #3C8F90;\n"
"font: 60pt;\n"
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
        self.LeftButton.setAutoRepeat(True)
        #self.gridLayout.addWidget(self.LeftButton, 1, 0, 1, 1)
        self.Head = QtWidgets.QFrame(parent=self)
        self.Head.setFixedHeight(55)
        self.Head.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Head.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Head)
        self.LabelWelcome = QtWidgets.QLabel(parent=self.Head)
        self.LabelWelcome.setFixedHeight(40)
        self.LabelWelcome.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.LabelWelcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.LabelWelcome.setIndent(30)
        self.horizontalLayout.addWidget(self.LabelWelcome)
        #self.ImageSettings = QtWidgets.QLabel(parent=self.Head)
        #self.ImageSettings.setFixedSize(40,40)
        #self.ImageSettings.setPixmap(QtGui.QPixmap("D:\\Projet Python\\ui\\../../gears.ico"))
        #self.ImageSettings.setScaledContents(True)
        #self.horizontalLayout.addWidget(self.ImageSettings)
        
        self.ImageSettings = QtWidgets.QPushButton(self.Head)
        self.ImageSettings.setFixedSize(40,40)
        icon = QtGui.QIcon()
        icon.addFile("images\gears.ico", QtCore.QSize())
        self.ImageSettings.setIcon(icon)
        self.ImageSettings.setIconSize(QtCore.QSize(40, 40))
        
        self.horizontalLayout.addWidget(self.ImageSettings)
        
        
        #self.gridLayout.addWidget(self.Head, 0, 0, 1, 5)
        self.ImageRightGame = QtWidgets.QLabel(parent=self)
        self.ImageRightGame.setFixedSize(150,150)
        self.ImageRightGame.setPixmap(QtGui.QPixmap("D:\\Projet Python\\ui\\../../Omega Games/images/icon.ico"))
        self.ImageRightGame.setScaledContents(True)
        #self.gridLayout.addWidget(self.ImageRightGame, 1, 3, 1, 1)
        self.RightButton = QtWidgets.QPushButton(parent=self)
        self.RightButton.setFixedSize(60,200)
        self.RightButton.setStyleSheet("QPushButton {\n"
"background:none;\n"
"color: #3C8F90;\n"
"border: 2px solid #3C8F90;\n"
"font:60pt;\n"
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
        self.RightButton.setAutoRepeat(True)
        #self.gridLayout.addWidget(self.RightButton, 1, 4, 1, 1)

        self.setText()
        self.init_button()
        self.setGames()
        
        self.setTabOrder(self.PlayButton, self.LeftButton)
        self.setTabOrder(self.LeftButton, self.RightButton)
        self.setTabOrder(self.RightButton, self.scrollArea)
        
        
        self.gridLayout.addWidget(self.LeftButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.ImageLeftGame, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.MainGame, 1, 2, 1, 1,QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout.addWidget(self.ImageRightGame, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.RightButton, 1, 4, 1, 1)
        
        self.gridLayout.addWidget(self.DataGame, 2, 2, 1, 1)        
        self.gridLayout.addWidget(self.Head, 0, 0, 1, 5)
        
        
    def setText(self):
        self.GameTitle.setText("Mining Game")
        self.LegendGame.setText("<html><head/><body><p>MiningGame est comme sont nom l\'indique un jeu de</p><p>minage !</p><p>Rejoin l\'aventure !</p><p><br/></p><p><br/></p><p>Fait par Amtarius</p><p>Le 24/02/2023</p><p>Dernière mise à jour je 24/03/2023</p></body></html>")
        self.PlayButton.setText("Play !")
        self.PlayButton.setShortcut("Return")
        self.LeftButton.setText("<")
        self.LeftButton.setShortcut("Left")
        self.LabelWelcome.setText("Welcome {username}")
        self.RightButton.setText(">")
        self.RightButton.setShortcut("Right")
        
    def init_button(self):
        self.RightButton.clicked.connect(self.turn_right)
        self.LeftButton.clicked.connect(self.turn_left)
        
    def turn_right(self):
        self.main_game -= 1
        self.setGames()
        
    def turn_left(self):
        self.main_game += 1
        self.setGames()
        
    def setGames(self):
        if self.main_game >= self.nb_game:
            self.main_game = 0
        elif self.main_game == -1:
            self.main_game = 3
        self.MainGame.setPixmap(QtGui.QPixmap(self.proposegames[self.main_game][1]))
        if self.main_game == self.nb_game-1:
            self.ImageRightGame.setPixmap(QtGui.QPixmap(self.proposegames[0][1]))
        else:
            self.ImageRightGame.setPixmap(QtGui.QPixmap(self.proposegames[self.main_game+1][1]))
        if self.main_game == 0:
            self.ImageLeftGame.setPixmap(QtGui.QPixmap(self.proposegames[self.nb_game-1][1]))
        else:
            self.ImageLeftGame.setPixmap(QtGui.QPixmap(self.proposegames[self.main_game-1][1]))
        self.GameTitle.setText(self.proposegames[self.main_game][0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = SelectScreen()
    windows.show()
    sys.exit(app.exec())