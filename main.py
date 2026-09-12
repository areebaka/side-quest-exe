import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("WE'RE MAKING A GAME HAHA")

running = True

player_x = 400
player_y = 300

player_speed = 10

collected = False
escaped = False
font = pygame.font.Font(None, 36)
quest_item = pygame.Rect(600, 400, 20, 20)
door = pygame.Rect(700, 500, 40, 60)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x = min(player_x + player_speed, 760)

    if keys[pygame.K_LEFT]:
        player_x = max(player_x - player_speed, 0)

    if keys[pygame.K_UP]:
        player_y = max(player_y - player_speed, 0)

    if keys[pygame.K_DOWN]:
        player_y = min(player_y + player_speed, 560)

    screen.fill((200, 160, 220))

    player = pygame.Rect(player_x, player_y, 40, 40)
    pygame.draw.rect(screen, (50, 50, 50), player)

    if not collected:
        pygame.draw.rect(screen, (255, 200, 50), quest_item)

        if player.colliderect(quest_item):
            collected = True
    if collected:
        text = font.render("Quest Item Collected!", True, (255, 255, 255))
        screen.blit(text, (250, 50))
        if not escaped:
            pygame.draw.rect(screen, (0, 255, 0), door)

            if player.colliderect(door):
                escaped = True
    if escaped:
        text = font.render("You Escaped!", True, (255, 255, 255))
        screen.blit(text, (300, 100))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()