import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light Simulator")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Colors
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREY = (50,50,50)

# Traffic light positions
VERTICAL_LIGHT = (150, 50)
HORIZONTAL_LIGHT = (450, 250)
RADIUS = 20

# Traffic timing (seconds)
GREEN_TIME = 5 
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light Simulator")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Colors
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREY = (50,50,50)

# Traffic light positions
VERTICAL_LIGHT = (150, 50)
HORIZONTAL_LIGHT = (450, 250)
RADIUS = 20

# Traffic timing (seconds)
GREEN_TIME = 5
YELLOW_TIME = 2

# Car settings
vertical_cars = []
horizontal_cars = []
CAR_SPEED = 2

# State
state = "vertical_green"
timer = GREEN_TIME
pedestrian_request = False

def draw_light(pos, current, color_name):
    pygame.draw.circle(screen, RED if color_name=="red" and current else GREY, (pos[0], pos[1]), RADIUS)
    pygame.draw.circle(screen, YELLOW if color_name=="yellow" and current else GREY, (pos[0], pos[1]+30), RADIUS)
    pygame.draw.circle(screen, GREEN if color_name=="green" and current else GREY, (pos[0], pos[1]+60), RADIUS)

def spawn_cars():
    if random.random() < 0.02:
        vertical_cars.append([130, -30, 20, 30])
    if random.random() < 0.02:
        horizontal_cars.append([-30, 240, 30, 20])

def move_cars():
    # Vertical cars stop at y=150 if light is red
    for car in vertical_cars:
        if state in ["vertical_green", "vertical_yellow"] or car[1] > 150:
            car[1] += CAR_SPEED
    # Horizontal cars stop at x=350 if light is red
    for car in horizontal_cars:
        if state in ["horizontal_green", "horizontal_yellow"] or car[0] > 350:
            car[0] += CAR_SPEED
    # Remove off-screen cars
    vertical_cars[:] = [c for c in vertical_cars if c[1] < HEIGHT]
    horizontal_cars[:] = [c for c in horizontal_cars if c[0] < WIDTH]

running = True
while running:
    dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds
    timer -= dt

    screen.fill(BLACK)
    spawn_cars()
    move_cars()

    # Draw cars
    for car in vertical_cars:
        pygame.draw.rect(screen, BLUE, car)
    for car in horizontal_cars:
        pygame.draw.rect(screen, BLUE, car)

    # Draw traffic lights
    if state.startswith("vertical"):
        draw_light(VERTICAL_LIGHT, True, "green" if state=="vertical_green" else "yellow" if state=="vertical_yellow" else "red")
        draw_light(HORIZONTAL_LIGHT, True, "red")
    else:
        draw_light(HORIZONTAL_LIGHT, True, "green" if state=="horizontal_green" else "yellow" if state=="horizontal_yellow" else "red")
        draw_light(VERTICAL_LIGHT, True, "red")

    # Countdown
    timer_text = font.render(f"{int(timer)}s", True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pedestrian_request = True

    # State machine
    if timer <= 0:
        if state == "vertical_green":
            state = "vertical_yellow"
            timer = YELLOW_TIME
        elif state == "vertical_yellow":
            state = "horizontal_green"
            timer = GREEN_TIME
        elif state == "horizontal_green":
            state = "horizontal_yellow"
            timer = YELLOW_TIME
        elif state == "horizontal_yellow":
            state = "vertical_green"
            timer = GREEN_TIME

pygame.quit()




name = "Abdulllah"
Obtainedmarks = 0.6
age = 100
under18 = True
print(type(name))
print(type(age))
print(type(Obtainedmarks))
print(type(under18))


YELLOW_TIME = 2

# Car settings
vertical_cars = []
horizontal_cars = []
CAR_SPEED = 2

# State
state = "vertical_green"
timer = GREEN_TIME
pedestrian_request = False

def draw_light(pos, current, color_name):
    pygame.draw.circle(screen, RED if color_name=="red" and current else GREY, (pos[0], pos[1]), RADIUS)
    pygame.draw.circle(screen, YELLOW if color_name=="yellow" and current else GREY, (pos[0], pos[1]+30), RADIUS)
    pygame.draw.circle(screen, GREEN if color_name=="green" and current else GREY, (pos[0], pos[1]+60), RADIUS)

def spawn_cars():
    if random.random() < 0.02:
        vertical_cars.append([130, -30, 20, 30])
    if random.random() < 0.02:
        horizontal_cars.append([-30, 240, 30, 20])

def move_cars():
    # Vertical cars stop at y=150 if light is red
    for car in vertical_cars:
        if state in ["vertical_green", "vertical_yellow"] or car[1] > 150:
            car[1] += CAR_SPEED
    # Horizontal cars stop at x=350 if light is red
    for car in horizontal_cars:
        if state in ["horizontal_green", "horizontal_yellow"] or car[0] > 350:
            car[0] += CAR_SPEED
    # Remove off-screen cars
    vertical_cars[:] = [c for c in vertical_cars if c[1] < HEIGHT]
    horizontal_cars[:] = [c for c in horizontal_cars if c[0] < WIDTH]

running = True
while running:
    dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds
    timer -= dt

    screen.fill(BLACK)
    spawn_cars()
    move_cars()

    # Draw cars
    for car in vertical_cars:
        pygame.draw.rect(screen, BLUE, car)
    for car in horizontal_cars:
        pygame.draw.rect(screen, BLUE, car)

    # Draw traffic lights
    if state.startswith("vertical"):
        draw_light(VERTICAL_LIGHT, True, "green" if state=="vertical_green" else "yellow" if state=="vertical_yellow" else "red")
        draw_light(HORIZONTAL_LIGHT, True, "red")
    else:
        draw_light(HORIZONTAL_LIGHT, True, "green" if state=="horizontal_green" else "yellow" if state=="horizontal_yellow" else "red")
        draw_light(VERTICAL_LIGHT, True, "red")

    # Countdown
    timer_text = font.render(f"{int(timer)}s", True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pedestrian_request = True

    # State machine
    if timer <= 0:
        if state == "vertical_green":
            state = "vertical_yellow"
            timer = YELLOW_TIME
        elif state == "vertical_yellow":
            state = "horizontal_green"
            timer = GREEN_TIME
        elif state == "horizontal_green":
            state = "horizontal_yellow"
            timer = YELLOW_TIME
        elif state == "horizontal_yellow":
            state = "vertical_green"
            timer = GREEN_TIME

pygame.quit()




name = "Abdulllah"
Obtainedmarks = 0.6
age = 100
under18 = True
print(type(name))
print(type(age))
print(type(Obtainedmarks))
print(type(under18))

