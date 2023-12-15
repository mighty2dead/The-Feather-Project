import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the color of the circle
WHITE = (255, 255, 255)

# Define the radius of the circle
RADIUS = 50

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position
    x, y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle at the mouse position
    pygame.draw.circle(screen, WHITE, (x, y), RADIUS)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()