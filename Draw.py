#V1.1
import pygame
import sys, os
os.system('clear')

pygame.init()
width, height = 1000, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw")

def vars():
    global mode, player_x, player_y, player_color, player_width, player_height, player_color_select
    global running, keys_pressed, player_speed, clock, color_change_delay, last_color_change_time
    global background_color, background_select, shape, trail_surface, normal_color
    mode = 0
    player_x = 1
    player_y = 60
    player_color = (255, 0, 0)
    normal_color = player_color
    player_width, player_height = 100, 100
    player_color_select = 1
    running = True
    keys_pressed = set()
    player_speed = 5  # Adjust the player's movement speed
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate
    color_change_delay = 200  # Delay in milliseconds
    last_color_change_time = pygame.time.get_ticks()
    background_color = (255, 255, 255) # Default background color
    background_select = 1
    shape = 1
    trail_surface = pygame.Surface((width, height), pygame.SRCALPHA)

vars()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)
        elif event.type == pygame.KEYUP:
            keys_pressed.discard(event.key)
    if pygame.K_ESCAPE in keys_pressed:
        pygame.quit()
        sys.exit()
    if pygame.K_a in keys_pressed:
        player_x -= player_speed
    if pygame.K_d in keys_pressed:
        player_x += player_speed
    if pygame.K_w in keys_pressed:
        player_y -= player_speed
    if pygame.K_s in keys_pressed:
        player_y += player_speed

    current_time = pygame.time.get_ticks()
    if mode == 1:
        if pygame.K_LEFT in keys_pressed and current_time - last_color_change_time > color_change_delay:
            player_color_select += 1
            last_color_change_time = current_time
            print(player_color_select)
        if pygame.K_RIGHT in keys_pressed and current_time - last_color_change_time > color_change_delay:
            player_color_select -= 1
            last_color_change_time = current_time
            print(player_color_select)
        if pygame.K_UP in keys_pressed and current_time - last_color_change_time > color_change_delay:
            player_width += 10
            player_height += 10
            last_color_change_time = current_time
            print(player_width, player_height)
        if pygame.K_DOWN in keys_pressed and current_time - last_color_change_time > color_change_delay:
            player_width -= 10
            player_height -= 10
            last_color_change_time = current_time
            print(player_width, player_height)
    elif mode == 2:
        if pygame.K_LEFT in keys_pressed and current_time - last_color_change_time > color_change_delay:
            background_select -= 1  # Change background to black
            last_color_change_time = current_time
            print("Background color changed to black")
        if pygame.K_RIGHT in keys_pressed and current_time - last_color_change_time > color_change_delay:
            background_select += 1  # Change background to white
            last_color_change_time = current_time
            print("Background color changed to white")
    elif mode == 3:
        if pygame.K_LEFT in keys_pressed and current_time - last_color_change_time > color_change_delay:
            shape -= 1
            last_color_change_time = current_time
            print(shape)
        if pygame.K_RIGHT in keys_pressed and current_time - last_color_change_time > color_change_delay:
            shape += 1
            last_color_change_time = current_time
            print(shape)
    if pygame.K_m in keys_pressed and current_time - last_color_change_time > color_change_delay:
        mode += 1
        last_color_change_time = current_time
        print(mode)
    if pygame.K_r in keys_pressed:
        trail_surface.fill((0, 0, 0, 0))  # Reset the trail surface

    if player_y <= 0:
        player_y = 1
    elif player_y >= 800:
        player_y = 799
    elif player_x <= 0:
        player_x = 1
    elif player_x >= 1000:
        player_x = 999
    #Player color
    if player_color_select == 1:
        player_color = (255, 0, 0)
        normal_color = player_color
    elif player_color_select == 2:
        player_color = (0, 255, 0)
        normal_color = player_color
    elif player_color_select == 3:
        player_color = (0, 0, 255)
        normal_color = player_color
    #player color limiter
    if player_color_select > 3:
        player_color_select = 1
    elif player_color_select < 1:
        player_color_select = 3
    #Background
    if background_select == 1:
        background_color = (255, 255, 255)
    elif background_select == 2:
        background_color = (0, 0, 0)
    elif background_select == 3:
        background_color = (255, 0, 0)
    elif background_select == 4:
        background_color = (0, 255, 0)
    elif background_select == 5:
        background_color = (0, 0, 255)
    elif background_select == 6:
        background_color = (255, 255, 0)
    elif background_select == 7:
        background_color = (255, 0, 255)
    elif background_select == 8:
        background_color = (0, 255, 255)
    #Background limiter
    elif background_select > 8:
        background_select = 1
    elif background_select <= 0:
        background_select = 8
    #shape limiter
    if shape <= 0:
        shape = 3
    elif shape > 3:
        shape = 1
    
    if player_width <= 0 and player_height <= 0:
        player_width = 10
        player_height = 10
    
    if mode > 3:
        mode = 1
    elif mode <= 0:
        mode = 3

    # Fill the background color each frame
    window.fill(background_color)

    # Blit the trail surface onto the window
    window.blit(trail_surface, (0, 0))

    # Draw the player on the trail surface
    if shape == 1:
        pygame.draw.rect(trail_surface, player_color, (player_x, player_y, player_width, player_height))
    elif shape == 2:
        pygame.draw.circle(trail_surface, player_color, (player_x, player_y), player_width)
    elif shape == 3:
        pygame.draw.ellipse(trail_surface, player_color, (player_x, player_y, player_width, player_height))
    
    pygame.display.flip()

    clock.tick(60)  # Limit the frame rate to 60 frames per second