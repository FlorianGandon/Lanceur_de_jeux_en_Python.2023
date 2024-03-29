import pygame

class SpaceGame:
    def __init__(self):
        pass
    
    def init(self, user):
        pygame.init()
        
        # définir la fenêtre
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Space Game')
        icon = pygame.image.load('./images/SpaceGame.png') # pas de .ico
        pygame.display.set_icon(icon)
        
        self.running = True
        self.user = user
        
    def hangling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.EnCours = False
                pygame.quit()
        
    def update(self):
        pass
        
    def display(self):
        self.window.fill("black")
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.hangling_event()
            self.update()
            self.display()

                    
if __name__ == '__main__':
    game = SpaceGame()
    game.init()
    game.run()

