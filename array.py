import pygame
import sys

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ARRAY_WIDTH = 600
ARRAY_HEIGHT = 400
ITEM_WIDTH = 100
ITEM_HEIGHT = 40
BACKGROUND_COLOR = (255, 255, 255)
ARRAY_COLOR = (200, 200, 200)
ITEM_COLOR = (100, 200, 100)
TEXT_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Array Visualization")
font = pygame.font.Font(None, 36)

# Array Initialization
array = []
max_size = ARRAY_WIDTH // ITEM_WIDTH

def draw_array(array):
    # Draw the array rectangle
    pygame.draw.rect(screen, ARRAY_COLOR, (100, 100, ARRAY_WIDTH, ARRAY_HEIGHT), 0)
    
    # Draw each item in the array
    for index, item in enumerate(array):  # Display items from left to right
        item_x = 100 + index * ITEM_WIDTH + 10  # x position of the item
        item_y = 120  # y position of the item
        pygame.draw.rect(screen, ITEM_COLOR, (item_x, item_y, ITEM_WIDTH, ITEM_HEIGHT), 0)
        text_surface = font.render(str(item), True, TEXT_COLOR)
        screen.blit(text_surface, (item_x + 10, item_y + 10))  # Center text in item

def add_item(value):
    if len(array) < max_size:
        array.append(value)

def remove_item(index):
    if 0 <= index < len(array):
        array.pop(index)

# Game Loop
while True:
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Add item on 'A' key press
                add_item(len(array) + 1)  # Add the next number
            elif event.key == pygame.K_r:  # Remove item on 'R' key press
                if array:
                    remove_item(len(array) - 1)  # Remove the last item

    draw_array(array)
    
    # Display instructions
    instruction_surface = font.render("Press 'A' to Add Item, 'R' to Remove Last Item", True, TEXT_COLOR)
    screen.blit(instruction_surface, (100, 20))

    pygame.display.flip()
    pygame.time.delay(100)

