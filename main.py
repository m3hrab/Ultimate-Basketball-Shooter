import pygame 
from constants import *
from scripts.menuState import MenuState
from scripts.settingsState import SettingsState

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Basketball Shooter')


    # MenuState object
    menu_state = MenuState(screen)
    # SettingsState object
    settings_state = SettingsState(screen)


    current_state = menu_state

    while True:

        # Handle events
        events = pygame.event.get()

        next_state = current_state.handle_events(events)
        if next_state == 'menu':
            current_state = menu_state
        elif next_state == 'game':
            pass 
        elif next_state == 'instructions':
            pass
        elif next_state == 'settings':
            current_state = settings_state
    
        current_state.update()
        current_state.draw()

        pygame.display.flip()

if __name__ == '__main__':
    main()
