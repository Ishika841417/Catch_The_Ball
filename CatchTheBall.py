#import modules
import pygame #library to build game
import random #to fall ball at random place
import sys #to close the program properly

# Initialize pygame
pygame.init() #to initialize the program

# Screen dimensions
WIDTH, HEIGHT = 600, 500 #in pixel
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set_mode build the screen
pygame.display.set_caption("Catch the Ball") #set_caption display text in title bar

# Colors #RGB (RED,GREEN,BLUE) VALUE OF EACH COLOR BETWEEN (0 TO 255)
WHITE = (255, 255, 255) #bg color
BLACK = (0, 0, 0) #score color
BALL_COLOR = (255, 0, 0) #red
PADDLE_COLOR = (0, 0, 255) #blue

# Fonts
font = pygame.font.SysFont(None, 36) #TO DISPLAY SCORE , size=36

# Paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT) #put on the bottom of screen
paddle_speed = 10 

# Ball
BALL_RADIUS = 15
ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS) #starts from random position
ball_y = 0 #start from up
ball_speed = 5 #speed of falling down

# Score
score = 0 #initial score is zero

# Clock
clock = pygame.time.Clock() #set clock() to control the frame rate of game

# Sound (optional)
try:
    catch_sound = pygame.mixer.Sound(pygame.mixer.Sound(pygame.mixer.Sound('catch.wav')))
except:
    catch_sound = None  # if sound file not found

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get(): #it checks user close the game window , if yes then game will be closed
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Move ball
    ball_y += ball_speed #it increase 5 pixel downwards in each frame

    # Ball reset or catch
    if ball_y >= HEIGHT - 50 and paddle.left < ball_x < paddle.right:
        score += 1 #if ball collid with paddle , then score increased by 1
        ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS) #then next ball will fall
        ball_y = 0
        if catch_sound:
            catch_sound.play() #it play the sound after collision of ball and paddle
    elif ball_y > HEIGHT:
        score -= 1 #here ball score decreased by 1
        ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        ball_y = 0 #then next ball will come

    # Draw paddle and ball
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Draw score , to show score at top left corner
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60) #game run on 60 frame per second

# Quit
pygame.quit() #to quit the game
sys.exit() #to exit pygame after coming from loop