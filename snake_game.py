import pygame

# Define some colors
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SQUARE_SIZE = 20  # This sets the size of each square in the grid
GRID_SIZE = 30  # Set grid size (n * n squares)
MARGIN = 1

SIZE = MARGIN*2 + (GRID_SIZE*SQUARE_SIZE+MARGIN*GRID_SIZE)


# Set up starting snake position
head_loc = [13, 15]
head_dir = ''
tail_loc = [head_loc[0] + 6, head_loc[1]]
tail_dir = ['up', 'up', 'up', 'up', 'up', 'up']

speed = 5  # Snake move speed. Lower number is quicker
move_clock = 0  # Used to move snake at certain speed

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(GRID_SIZE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(GRID_SIZE):
        if column == 0 or column == GRID_SIZE - 1 or row == 0 or row == GRID_SIZE - 1:
            grid[row].append(1)  # Append a cell
        else:
            grid[row].append(0)  # Append a cell

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [SIZE, SIZE]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("SNAKE GAME (PyGame)")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Display head / tail locations on the grid
grid[head_loc[0]][head_loc[1]] = 1
grid[head_loc[0]+1][head_loc[1]] = 1
grid[head_loc[0]+2][head_loc[1]] = 1
grid[head_loc[0]+3][head_loc[1]] = 1
grid[head_loc[0]+4][head_loc[1]] = 1
grid[head_loc[0]+5][head_loc[1]] = 1
grid[tail_loc[0]][tail_loc[1]] = 1


def move_tail():
    # Removes tail square and sets new position for tail
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
                    head_dir = 'up'
                    move_clock = speed
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if(head_dir != 'right' and head_dir != 'left'):
                    head_dir = 'right'
                    move_clock = speed
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if(head_dir != 'down' and head_dir != 'up' and head_dir != ''):
                    head_dir = 'down'
                    move_clock = speed
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if(head_dir != 'left' and head_dir != 'right'):
                    head_dir = 'left'
                    move_clock = speed


    if move_clock < speed:
        move_clock += 1
    else:
        if(head_dir == 'left'):
            if grid[head_loc[0]][head_loc[1] - 1] == 1:
                print("OCUPPIED SQUARE COLLISION")
                done = True
            else:
                grid[head_loc[0]][head_loc[1] - 1] = 1
                move_tail()
                tail_dir.insert(0, 'left')
                head_loc[1] -= 1

        elif(head_dir == 'down'):
            if grid[head_loc[0] + 1][head_loc[1]] == 1:
                print("OCUPPIED SQUARE COLLISION")
                done = True
            else:
                grid[head_loc[0] + 1][head_loc[1]] = 1
                move_tail()
                tail_dir.insert(0, 'down')
                head_loc[0] += 1

        elif(head_dir == 'right'):
            if grid[head_loc[0]][head_loc[1] + 1] == 1:
                print("OCUPPIED SQUARE COLLISION")
                done = True
            else:
                grid[head_loc[0]][head_loc[1] + 1] = 1
                head_dir = 'right'
                move_tail()
                tail_dir.insert(0, 'right')
                head_loc[1] += 1

        elif(head_dir == 'up'):
            if grid[head_loc[0] - 1][head_loc[1]] == 1:
                print("OCUPPIED SQUARE COLLISION")
                done = True
            else:
                grid[head_loc[0] - 1][head_loc[1]] = 1
                head_dir = 'up'
                move_tail()
                tail_dir.insert(0, 'up')
                head_loc[0] -= 1

        move_clock = 0

    # Check for collision

    # Set the screen background
    screen.fill(WHITE)

    # Draw the grid
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if grid[row][column] == 1:
                color = BLACK
            else:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + SQUARE_SIZE) * column + MARGIN,
                              (MARGIN + SQUARE_SIZE) * row + MARGIN,
                              SQUARE_SIZE,
                              SQUARE_SIZE])

    # Limit to 60 frames per second
    clock.tick(60)

    # Update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
