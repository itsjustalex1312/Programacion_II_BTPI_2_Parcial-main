import pygame 
from player import Player
from config import Config
from ball import Ball
pygame.init()

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)

running = True

bg_color = [0,0,0]

clock =pygame.time.Clock()

player_1 = Player (
    screen,
      Config.PLAYER_BORDERDISTANCE,
        (Config.SCREEN_WIDTH/2) - (Config.PLAYER_HEIGHT/2),
        Config.PLAYER_WIDTH,
        Config.PLAYER_HEIGHT
      )
player_2 = Player (
    screen,
      Config.SCREEN_WIDTH - Config.PLAYER_BORDERDISTANCE - Config.PLAYER_WIDTH,
        (Config.SCREEN_WIDTH/2) - (Config.PLAYER_HEIGHT/2),
        Config.PLAYER_WIDTH,
        Config.PLAYER_HEIGHT
        )
ball = Ball(
     screen,
     (Config.SCREEN_WIDTH/2) - 15,
     (Config.SCREEN_HEIGHT/2) - 15, 
     30
)
    


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1.set_velocidad(Config.PLAYER_MAX_SPEED * -1)
            if event.key == pygame.K_s:
                player_1.set_velocidad(Config.PLAYER_MAX_SPEED)
            if event.key == pygame.K_UP:
                player_2.set_velocidad(Config.PLAYER_MAX_SPEED * -1)
            if event.key == pygame.K_DOWN:
                    player_2.set_velocidad(Config.PLAYER_MAX_SPEED)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_1.set_velocidad(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_2.set_velocidad(0)


    if ball.get_x()>= Config.SCREEN_WIDTH:
        ball.reiniciar_pos()

    if ball.get_x()<= 0:
        ball.reiniciar_pos()

    delta_time = clock.tick(60) / 1000
    player_1.move(delta_time)
    player_2.move(delta_time)
    ball.move(delta_time)


    screen.fill(bg_color)
    
    #pygame.draw.rect(screen, "white", (player_1_coord_x, player_1_coord_y, 25, 150))
    player_1.draw()
    player_2.draw()
    ball.draw()
    
    pygame.display.flip()
    
    

pygame.quit()