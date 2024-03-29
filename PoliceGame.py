import pygame


class PoliceGame:
    def __init__(self):
        pass

    def init(self, user):
        pygame.init()
        
        # définir la fenêtre
        self.window = pygame.display.set_mode((1000, 750))
        pygame.display.set_caption('Police Game')
        icon = pygame.image.load('./images/PoliceGame.png') # pas de .ico
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
        self.window.fill("blue")
        
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.hangling_event()
            self.update()
            self.display()

                    
if __name__ == '__main__':
    game = PoliceGame()
    game.init()
    game.run()

