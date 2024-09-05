import pygame 

pygame.init()

screen = pygame.display.set_mode((800,600), flags=pygame.SCALED, vsync=1)

running = True

pelota_coord_x = 390
pelota_coord_y = 290

pelota_speed_x = 200
pelota_speed_y = 200

bg_color = [0,0,0]

clock =pygame.time.Clock()

PLAYER_MAX_SPEED = 500

player_2_coord_x = 750
player_2_coord_y = 225
player_2_speed = 0


player_1_coord_x = 15
player_1_coord_y = 225
player_1_speed = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1_speed = -PLAYER_MAX_SPEED
            if event.key == pygame.K_s:
                player_1_speed = PLAYER_MAX_SPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_1_speed = 0
            if event.key == pygame.K_s:
                player_1_speed = 0
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_2_speed = -PLAYER_MAX_SPEED
            if event.key == pygame.K_DOWN:
                player_2_speed = PLAYER_MAX_SPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_2_speed = 0
            if event.key == pygame.K_DOWN:
                player_2_speed = 0



    delta_time = clock.tick(60) / 1000


    player_1_coord_y += player_1_speed * delta_time

    if player_1_coord_y < 0:
        player_1_coord_y = 0

    if player_1_coord_y > 450:
        player_1_coord_y = 450

    pelota_coord_y += pelota_speed_y * delta_time

    if pelota_coord_y > 580:
        pelota_coord_y = 580
    
    elif pelota_coord_y < 0:
        pelota_coord_y = 0

    if pelota_coord_y >= 580 or pelota_coord_y <= 0:
        pelota_speed_y *= -1

    pelota_coord_x += pelota_speed_x * delta_time

    screen.fill(bg_color)
    
    pygame.draw.rect(screen, "white", (player_1_coord_x, player_1_coord_y, 25, 150))
    pygame.draw.rect(screen, "white", (player_2_coord_x, player_2_coord_y, 25, 150))
    pygame.draw.rect(screen, "white",(pelota_coord_x, pelota_coord_y, 20, 20))
    pygame.display.flip()
    
    pygame.display.flip()

pygame.quit()