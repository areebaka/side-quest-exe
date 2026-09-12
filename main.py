import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("WE'RE MAKING A GAME HAHA")

running = True

player_x = 400
player_y = 300

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x = min(player_x + 5, 760)

    if keys[pygame.K_LEFT]:
        player_x = max(player_x - 5, 0)

    if keys[pygame.K_UP]:
        player_y = max(player_y - 5, 0)

    if keys[pygame.K_DOWN]:
        player_y = min(player_y + 5, 560)

    screen.fill((200, 160, 220))
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (player_x, player_y, 40, 40)
    )
    pygame.display.flip()
    clock.tick(60)

pygame.quit()