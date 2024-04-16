import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

class Food:
    def __init__(self, x, y, weight, time):
        self.x = x
        self.y = y
        self.weight = weight
        self.time = time

def generate_food():
    x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    weight = random.randint(1, 4)  
    return Food(x, y, weight, time.time())

def draw_food(food):
    size = snake_block + food.weight * 5  
    pygame.draw.rect(dis, green, [food.x, food.y, size, size])

def Your_score(score, level):
    score_level = score_font.render("Score: " + str(score) + "   Level: " + str(level), True, yellow)
    dis.blit(score_level, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def gameLoop(snake_speed):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    food = generate_food()

    level = 1

    food_eaten = 0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(red)  

        draw_food(food)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)

        pygame.display.update()

        if x1 <= food.x + food.weight * 5 and x1 >= food.x and y1 <= food.y + food.weight * 5 and y1 >= food.y:
            Length_of_snake += food.weight
            food = generate_food()  
            food_eaten += 1 
        if time.time() - food.time > 5: 
            food = generate_food()  

        
        if food_eaten == 2:
            level += 1
            snake_speed +=10 
            food_eaten = 0 
        clock.tick(snake_speed)

    pygame.quit()
    quit()

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2, dis_height / 2 - mesg.get_height() / 2])

gameLoop(snake_speed)