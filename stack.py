import pygame
import sys

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
STACK_WIDTH = 200
STACK_HEIGHT = 400
ITEM_WIDTH = 150
ITEM_HEIGHT = 40
BACKGROUND_COLOR = (255, 255, 255)
STACK_COLOR = (200, 200, 200)
ITEM_COLOR = (100, 200, 100)
TEXT_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Stack Visualization")
font = pygame.font.Font(None, 36)

# Stack Initialization
stack = []
max_size = STACK_HEIGHT // ITEM_HEIGHT

def draw_stack(stack):
    # Draw the stack rectangle
    pygame.draw.rect(screen, STACK_COLOR, (300, 100, STACK_WIDTH, STACK_HEIGHT), 0)
    
    # Draw each item in the stack
    for index, item in enumerate(reversed(stack)):  # Reverse to display the top of the stack at the top
        item_x = 305  # x position of the item
        item_y = 100 + index * ITEM_HEIGHT  # y position of the item
        pygame.draw.rect(screen, ITEM_COLOR, (item_x, item_y, ITEM_WIDTH, ITEM_HEIGHT), 0)
        text_surface = font.render(str(item), True, TEXT_COLOR)
        screen.blit(text_surface, (item_x + 10, item_y + 10))  # Center text in item

def push():
    if len(stack) < max_size:
        new_item = len(stack) + 1  # Create a new item based on the current stack size
        stack.append(new_item)

def pop():
    if stack:
        stack.pop()

# Game Loop
while True:
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Push on 'P' key press
                push()
            elif event.key == pygame.K_o:  # Pop on 'O' key press
                pop()

    draw_stack(stack)
    
    # Display instructions
    instruction_surface = font.render("Press 'P' to Push, 'O' to Pop", True, TEXT_COLOR)
    screen.blit(instruction_surface, (300, 20))

    pygame.display.flip()
    pygame.time.delay(100)
    