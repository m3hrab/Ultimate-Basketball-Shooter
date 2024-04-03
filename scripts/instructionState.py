import pygame
from scripts.button import Button
from scripts.gameState import GameState
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class InstructionState(GameState):
    """Settings menu of the Basketball shooter"""

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        # Load the background image and get its rect.
        self.background_img = pygame.image.load('assets/images/instructions.png')
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_img_rect = self.background_img.get_rect()

        # Get the screen rect
        self.screen_rect = screen.get_rect()
        self.background_img_rect.center = self.screen_rect.center


        # Buttons
        self.back_btn = Button(54, 50, 50, 50)

    
    def handle_events(self, events):

        # Call the parent class's handle_events method
        super().handle_events(events)

        # handle keyboard and mouse events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.back_btn.rect.collidepoint(mouse_pos):
                    return 'menu'
            
                
    def update(self):
        super().update()


    def draw(self):
        # Draw the background image
        self.screen.blit(self.background_img, self.background_img_rect)
        # self.back_btn.draw(self.screen)