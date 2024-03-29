import pygame

class VillageGame:
    def __init__(self):
        pass
    
    def init(self, user):
        pygame.init()
        
        # définir la fenêtre
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Village Game')
        icon = pygame.image.load('./images/VillageGame.png') # pas de .ico
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
        self.window.fill("#2c6f1d")
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.hangling_event()
            self.update()
            self.display()


if __name__ == '__main__':
    game = VillageGame()
    game.init()
    game.run()

