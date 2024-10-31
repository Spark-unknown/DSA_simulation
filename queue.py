import pygame
import sys
from collections import deque

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
QUEUE_WIDTH = 600
QUEUE_HEIGHT = 400
ITEM_WIDTH = 50
ITEM_HEIGHT = 40
BACKGROUND_COLOR = (255, 255, 255)
QUEUE_COLOR = (200, 200, 200)
ITEM_COLOR = (100, 200, 100)
TEXT_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Queue Visualization")
font = pygame.font.Font(None, 36)

# Queue Initialization
queue = deque()
max_size = QUEUE_WIDTH // ITEM_WIDTH

def draw_queue(queue):
    # Draw the queue rectangle
    pygame.draw.rect(screen, QUEUE_COLOR, (100, 100, QUEUE_WIDTH, QUEUE_HEIGHT), 0)
    
    # Draw each item in the queue
    for index, item in enumerate(queue):
        item_x = 100 + index * ITEM_WIDTH + 10  # x position of the item
        item_y = 120  # y position of the item
        pygame.draw.rect(screen, ITEM_COLOR, (item_x, item_y, ITEM_WIDTH, ITEM_HEIGHT), 0)
        text_surface = font.render(str(item), True, TEXT_COLOR)
        screen.blit(text_surface, (item_x + 15, item_y + 10))  # Center text in item

def enqueue():
    if len(queue) < max_size:
        new_item = len(queue) + 1  # Create a new item based on the current queue size
        queue.append(new_item)

def dequeue():
    if queue:
        queue.popleft()

# Game Loop
while True:
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:  # Enqueue on 'E' key press
                enqueue()
            elif event.key == pygame.K_d:  # Dequeue on 'D' key press
                dequeue()

    draw_queue(queue)
    
    # Display instructions
    instruction_surface = font.render("Press 'E' to Enqueue, 'D' to Dequeue", True, TEXT_COLOR)
    screen.blit(instruction_surface, (100, 20))

    pygame.display.flip()
    pygame.time.delay(100)

