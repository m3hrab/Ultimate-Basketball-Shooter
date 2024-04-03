import pygame
from scripts.button import Button
from scripts.gameState import GameState
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class MenuState(GameState):
    """Main menu of the Basketball shooter"""

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        # Load the background image and get its rect.
        self.background_img = pygame.image.load('assets/images/menu.png')
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_img_rect = self.background_img.get_rect()

        # Get the screen rect
        self.screen_rect = screen.get_rect()
        self.background_img_rect.center = self.screen_rect.center


        # Buttons
        self.start_button = Button(self.screen_rect.centerx - 67, self.screen_rect.centery + 54 , 130, 48)
        self.settings_button = Button(self.screen_rect.right - 80, 49 , 47, 48)
        self.instructions_button = Button(self.screen_rect.right - 80, 115, 47, 48)

    
    def handle_events(self, events):

        # Call the parent class's handle_events method
        super().handle_events(events)

        # handle keyboard and mouse events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.start_button.rect.collidepoint(mouse_pos):  
                    return 'game'
                elif self.instructions_button.rect.collidepoint(mouse_pos):
                    return 'instructions'
                elif self.settings_button.rect.collidepoint(mouse_pos):
                    return 'settings'
                
    def update(self):
        super().update()


    def draw(self):
        # Draw the background image
        self.screen.blit(self.background_img, self.background_img_rect)
        # self.start_button.draw(self.screen)
        # self.settings_button.draw(self.screen)
        # self.instructions_button.draw(self.screen)
        