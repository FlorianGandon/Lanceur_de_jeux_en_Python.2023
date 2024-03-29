import pygame as py

class digger(py.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.Image = py.image.load("./images/drill.png")
        self.Rect = self.Image.get_rect()
    
    def draw(self):
        screen.blit(self.Image, self.Rect)