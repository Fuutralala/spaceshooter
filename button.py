# lets pygame render text to screen
import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
# Initialize button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
# set dimensions and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
# "None" tells pygame to use standard font
        self.font = pygame.font.SysFont(None, 48)
# build buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
# button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
# turn message into rendered image and center text on button