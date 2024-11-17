import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Connect 4")
clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Comic Sans MS', 100)

x, y = 300, 50
amount = 0
i, j = 0, 0

ColorChoice = 0
colors = [[255, 200, 100], [200, 200, 200], [100, 200, 150], [0, 0, 0]]
red_color = [255, 0, 0]
yellow_color = [230, 220, 175]
ballcolor = red_color

# Initialize game board (7 columns x 6 rows)
board = [[None for _ in range(6)] for _ in range(7)]

Row1 = [0]
Row2 = [0]
Row3 = [0]
Row4 = [0]
Row5 = [0]
Row6 = [0]
Row7 = [0]

balls = []

def createboard():
    global i, j
    i, j = 0, 0
    while i < 800:
        pygame.draw.rect(screen, [0, 0, 255], [i, j, 100, 100], 1)
        i += 100
        if i == 800 and j != 800:
            j += 100
            i = 0

def ChangeColors():
    global ColorChoice, ballcolor
    ballcolor = red_color if ColorChoice % 2 == 0 else yellow_color

def place_circle(choice):
    col = choice - 1
    row_index = [Row1, Row2, Row3, Row4, Row5, Row6, Row7][col][0]
    if row_index < 6:  # Check if column is not full
        x_pos = 50 + col * 100
        y_pos = 650 - (row_index * 100)
        balls.append([x_pos, y_pos, ballcolor])
        board[col][row_index] = ballcolor  # Update the board with the color
        [Row1, Row2, Row3, Row4, Row5, Row6, Row7][col][0] += 1
        if check_win(col, row_index, ballcolor):  # Check for a win
            if(ballcolor == [230, 220, 175]):
                print("We have a winner, Yellow!")
            else:
                print("We have a winner, Red!")
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

def check_win(col, row, color):
    def count_consecutive(dx, dy):
        count = 0
        x, y = col, row
        while 0 <= x < 7 and 0 <= y < 6 and board[x][y] == color:
            count += 1
            x += dx
            y += dy
        return count

    # Check vertical, horizontal, and both diagonal directions
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dx, dy in directions:
        if count_consecutive(dx, dy) + count_consecutive(-dx, -dy) - 1 >= 4:
            return True
    return False

# Main game loop
while True:
    screen.fill((200, 200, 200))
    createboard()
    ChangeColors()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_7:
                place_circle(event.key - pygame.K_0)
                ColorChoice += 1

    for ball in balls:
        pygame.draw.circle(screen, ball[2], (ball[0], ball[1]), 40)

    pygame.display.update()
    clock.tick(30)


