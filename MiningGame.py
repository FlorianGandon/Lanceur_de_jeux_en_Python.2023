import pygame
from time import time
from database_handler import DatabaseHandler_Game

class MiningGame:
    def __init__(self):
        pass
    
    def init(self, user):
        pygame.init()
        
        # définir la fenêtre
        self.window = pygame.display.set_mode((500, 750))
        pygame.display.set_caption('Mining Game')
        icon = pygame.image.load('./images/MiningGame.png') # pas de .ico
        pygame.display.set_icon(icon)
        
        self.running = True
        self.user = user
        
        self.start_time = time()
        self.database_handler = DatabaseHandler_Game("/databases/OmegaUsers.db", "UsersMiningGameTime")

    def hangling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming_time = int(round( time() -  self.start_time , 0))
                self.database_handler.add_time(self.user["id"], gaming_time)
                self.EnCours = False
                pygame.quit()
                
    def update(self):
        pass
        
    def display(self):
        self.window.fill("#582900")
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.hangling_event()
            self.update()
            self.display()

def main(debug : bool = False) -> None:
    user_exemple = {'id': 1, 'username': 'User', 'email': 'Exemple@gmail.com', 'grade': 'player'}
    game = MiningGame()
    if debug:
        game.init(user_exemple)
        game.run()
    else:
        try:
            game.init(user_exemple)
            game.run()
        except:
            print("End game")

if __name__ == '__main__':
    main(True)