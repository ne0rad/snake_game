import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SQUARE_SIZE = 20  # This sets the size of each square in the grid
GRID_SIZE = 30  # Set grid size (n * n squares)
MARGIN = 1

WINDOW_SIZE_SIDE = MARGIN*2 + (GRID_SIZE*SQUARE_SIZE+MARGIN*GRID_SIZE)
WINDOW_SIZE = [WINDOW_SIZE_SIDE, WINDOW_SIZE_SIDE]


# Set up starting snake position
head_loc = [13, 15]
head_dir = ''
tail_loc = [head_loc[0] + 4, head_loc[1]]
tail_dir = ['up', 'up', 'up', 'up']

speed = 80  # Snake move speed. Lower number is quicker
move_clock = 0  # Used to move snake at certain speed

move_queue = '' # This being used to queue the next move

# Create a 2 dimensional array for our playing grid
grid = []
for row in range(GRID_SIZE):
    # Add an empty array that will hold each cell
    grid.append([])
    for column in range(GRID_SIZE):
        if column == 0 or column == GRID_SIZE - 1 or row == 0 or row == GRID_SIZE - 1:
            grid[row].append(1)  # Append a cell (Occupied cells for border)
        else:
            grid[row].append(0)  # Append a cell

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("SNAKE GAME (PyGame)")

# Loop until this is True
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Display head / tail locations on the grid
grid[head_loc[0]][head_loc[1]] = 3
grid[head_loc[0]+1][head_loc[1]] = 3
grid[head_loc[0]+2][head_loc[1]] = 3
grid[head_loc[0]+3][head_loc[1]] = 3
grid[tail_loc[0]][tail_loc[1]] = 3


def move_tail():

    grid[tail_loc[0]][tail_loc[1]] = 0
    if tail_dir[-1] == 'up':
        tail_loc[0] -= 1
    if tail_dir[-1] == 'down':
        tail_loc[0] += 1
    if tail_dir[-1] == 'left':
        tail_loc[1] -= 1
    if tail_dir[-1] == 'right':
        tail_loc[1] += 1
    tail_dir.pop()
    return


def increase_speed():
    global speed
    if speed > 5:
        speed -= 1
    else:
        speed = 5
    return

def generate_food():
    # Generates food in a random place on the grid
    x = random.randint(1, GRID_SIZE - 1)
    y = random.randint(1, GRID_SIZE - 1)
    if grid[x][y] == 0:
        grid[x][y] = 2
    else:
        generate_food()
        return
    return

generate_food() # Generates first food item
generate_food() 
generate_food() # Make it 3 foods

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:  # Quit if ESC key pressed
                done = True
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if(head_dir != 'up' and head_dir != 'down'):
                    move_queue = 'up'
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if(head_dir != 'right' and head_dir != 'left'):
                    move_queue = 'right'
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if(head_dir != 'down' and head_dir != 'up' and head_dir != ''):
                    move_queue = 'down'
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if(head_dir != 'left' and head_dir != 'right'):
                    move_queue = 'left'

    # Checks if it's time to move the snake
    # Depending on speed
    if move_clock < speed / 10:
        move_clock += 1
    else:
        if move_queue != head_dir:
            # Make queued move the new direction
            head_dir = move_queue
        if(head_dir == 'left'):
            if grid[head_loc[0]][head_loc[1] - 1] != 0: # Checks for collision
                if grid[head_loc[0]][head_loc[1] - 1] == 2: # if collision is food makes snake bigger
                    grid[head_loc[0]][head_loc[1] - 1] = 3
                    head_loc[1] -= 1
                    tail_dir.insert(0, 'left')
                    move_clock = 0
                    increase_speed()
                    generate_food()
                    continue
                else:
                    done = True
            else:
                grid[head_loc[0]][head_loc[1] - 1] = 3
                move_tail()
                tail_dir.insert(0, 'left')
                head_loc[1] -= 1

        elif(head_dir == 'down'):
            if grid[head_loc[0] + 1][head_loc[1]] != 0:
                if grid[head_loc[0] + 1][head_loc[1]] == 2:
                    grid[head_loc[0] + 1][head_loc[1]] = 3
                    head_loc[0] += 1
                    tail_dir.insert(0, 'down')
                    move_clock = 0
                    increase_speed()
                    generate_food()
                    continue
                else:
                    done = True
            else:
                grid[head_loc[0] + 1][head_loc[1]] = 3
                move_tail()
                tail_dir.insert(0, 'down')
                head_loc[0] += 1

        elif(head_dir == 'right'):
            if grid[head_loc[0]][head_loc[1] + 1] != 0:
                if grid[head_loc[0]][head_loc[1] + 1] == 2:
                    grid[head_loc[0]][head_loc[1] + 1] = 3
                    head_loc[1] += 1
                    tail_dir.insert(0, 'right')
                    move_clock = 0
                    increase_speed()
                    generate_food()
                    continue
                else:
                    done = True
            else:
                grid[head_loc[0]][head_loc[1] + 1] = 3
                head_dir = 'right'
                move_tail()
                tail_dir.insert(0, 'right')
                head_loc[1] += 1

        elif(head_dir == 'up'):
            if grid[head_loc[0] - 1][head_loc[1]] != 0:
                if grid[head_loc[0] - 1][head_loc[1]] == 2:
                    grid[head_loc[0] - 1][head_loc[1]] = 3
                    head_loc[0] -= 1
                    tail_dir.insert(0, 'up')
                    move_clock = 0
                    increase_speed()
                    generate_food()
                    continue
                else:
                    done = True
            else:
                grid[head_loc[0] - 1][head_loc[1]] = 3
                head_dir = 'up'
                move_tail()
                tail_dir.insert(0, 'up')
                head_loc[0] -= 1

        move_clock = 0  # Reset move clock / snake speed

    # Set the screen background
    screen.fill(WHITE)

    # Draw the grid
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if grid[row][column] == 1:
                color = GREY
            elif grid[row][column] == 2:
                color = GREEN
            elif grid[row][column] == 3:
                if speed <= 10:
                    color = RED
                elif speed < 30:
                    color = BLUE
                else:
                    color = BLACK
            else:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + SQUARE_SIZE) * column + MARGIN,
                              (MARGIN + SQUARE_SIZE) * row + MARGIN,
                              SQUARE_SIZE,
                              SQUARE_SIZE])

    # Limit to 30 frames per second
    clock.tick(30)

    # Update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
