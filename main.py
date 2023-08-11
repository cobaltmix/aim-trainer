import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Balls")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Store the dots
dots = []

class Dot:
    def __init__(self):
        self.radius = 30
        self.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = random.randint(self.radius, SCREEN_HEIGHT - self.radius)
        self.color = RED
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off the screen edges
        if self.x < self.radius or self.x > SCREEN_WIDTH - self.radius:
            self.speed_x = -self.speed_x
        if self.y < self.radius or self.y > SCREEN_HEIGHT - self.radius:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_click(self, click_pos):
        distance = ((self.x - click_pos[0]) ** 2 + (self.y - click_pos[1]) ** 2) ** 0.5
        return distance <= self.radius

def main():
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for dot in dots[:]:
                    if dot.check_click(pygame.mouse.get_pos()):
                        score += 1
                        dots.remove(dot)
                        break

        # Clear the screen
        screen.fill(WHITE)

        # Create new dots if needed
        if len(dots) < 5:
            dots.append(Dot())

        # Move and draw the dots
        for dot in dots:
            dot.move()
            dot.draw()

        # Display score
        font = pygame.font.Font(None, 60)
        score_text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(score_text, (700, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
