import pygame
import math
import random
import sys
from constants import *

class BasketballGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("2D Basketball Game")
        self.clock = pygame.time.Clock()
        self.score = 0
        self.ball_radius = 20
        self.ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.ball_velocity = [0, 0]
        self.hoop_position = [SCREEN_WIDTH // 2 - 75, 50]  # Adjusted hoop position
        self.ground_height = SCREEN_HEIGHT - 20  # Height of the ground
        self.shooting = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.shooting = True
                    self.shot_strength = 0  # Reset shot strength when starting a new shot
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    self.shooting = False
                    # self.shoot_ball()

    def update(self):
        if self.shooting:
            mouse_pos = pygame.mouse.get_pos()
            dx = mouse_pos[0] - self.ball_position[0]
            dy = mouse_pos[1] - self.ball_position[1]
            self.ball_velocity = [dx / 10, dy / 10]  # Adjust speed range as needed
        self.ball_velocity[1] += GRAVITY  # Apply gravity
        self.ball_position[0] += self.ball_velocity[0]
        self.ball_position[1] += self.ball_velocity[1]

        # Check for ground collision
        if self.ball_position[1] + self.ball_radius >= self.ground_height:
            self.ball_position[1] = self.ground_height - self.ball_radius
            self.ball_velocity[1] = -self.ball_velocity[1] * 0.8  # Reverse and dampen vertical velocity

        # Check for score
        if self.ball_position[0] + self.ball_radius > self.hoop_position[0] and \
           self.ball_position[0] - self.ball_radius < self.hoop_position[0] + 150 and \
           self.ball_position[1] + self.ball_radius > self.hoop_position[1] and \
           self.ball_position[1] - self.ball_radius < self.hoop_position[1] + 20:
            self.score += 1
            self.reset_ball()

    def draw(self):
        self.screen.fill(WHITE)
        pygame.draw.circle(self.screen, BLACK, (int(self.ball_position[0]), int(self.ball_position[1])), self.ball_radius)
        pygame.draw.rect(self.screen, RED, (self.hoop_position[0], self.hoop_position[1], 150, 20))
        pygame.draw.rect(self.screen, BLACK, (0, self.ground_height, SCREEN_WIDTH, SCREEN_HEIGHT - self.ground_height))

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render("Score: " + str(self.score), True, BLACK)
        self.screen.blit(score_text, (10, 10))

        pygame.display.update()

    def reset_ball(self):
        self.ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]  # Reset ball position
        self.ball_velocity = [0, 0]  # Reset ball velocity

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = BasketballGame()
    game.run()
