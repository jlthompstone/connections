import json
import pygame

file = open("data/puzzles.json", "r")
puzzle_data = json.load(file)

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Connections")

clock = pygame.time.Clock()
FPS = 60

BOX_COLOUR = (241, 243, 240)
SELECTED_BOX_COLOUR = (88, 89, 79)
BOX_WIDTH = 160
BOX_HEIGHT = 130
GAP = 30

total_grid_width = (BOX_WIDTH * 4) + (GAP * 3)
total_grid_height = (BOX_HEIGHT * 4) + (GAP * 3)

start_x = (WINDOW_WIDTH - total_grid_width) // 2
start_y = (WINDOW_HEIGHT - total_grid_height) // 2

def check_selection(selected_words):
    selected_categories = []

    for i in range(4):
        for j in range(4):
            if selected_words[i] in puzzle_data[0]["groups"][j]["words"]:
                selected_categories.append(puzzle_data[0]["groups"][j]["difficulty"])

    if selected_categories[0] == selected_categories[1] == selected_categories[2] == selected_categories[3]:
        return True
    else:
        return False

selection = []

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Connections")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for row in range(4):
        for col in range(4):
            x = start_x + col * (BOX_WIDTH + GAP)
            y = start_y + row * (BOX_HEIGHT + GAP)

            box_rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)

            pygame.draw.rect(screen, BOX_COLOUR, box_rect, border_radius=8)

    pygame.display.flip()
    
pygame.quit()