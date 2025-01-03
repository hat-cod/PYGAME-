import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
PLAYER_COLOR = (0, 255, 0)  # Green player
ENEMY_COLOR = (255, 0, 0)  # Red enemies
BULLET_COLOR = (255, 255, 0)  # Yellow bullets
PLAYER_SIZE = 50
BULLET_SIZE = 10
ENEMY_SIZE = 50
ENEMY_SPEED = 3
BULLET_SPEED = 10

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Shooter Game")

# Player
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10
player_speed = 5

# Enemies
enemies = []
enemy_spawn_rate = 30  # Spawn an enemy every 30 frames
enemy_timer = 0

# Bullets
bullets = []

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to create an enemy
def create_enemy():
    enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy_y = -ENEMY_SIZE  # Spawn off the screen
    enemies.append([enemy_x, enemy_y])

# Function to move the enemies
def move_enemies():
    global enemies
    for enemy in enemies:
        enemy[1] += ENEMY_SPEED  # Move enemy down
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)  # Remove enemy if it goes off the screen

# Function to move the bullets
def move_bullets():
    global bullets
    for bullet in bullets:
        bullet[1] -= BULLET_SPEED  # Move bullet up
        if bullet[1] < 0:
            bullets.remove(bullet)  # Remove bullet if it goes off the screen

# Function to check collision between bullets and enemies
def check_collisions():
    global enemies, bullets
    for bullet in bullets:
        for enemy in enemies:
            if (bullet[0] >= enemy[0] and bullet[0] <= enemy[0] + ENEMY_SIZE) and \
               (bullet[1] >= enemy[1] and bullet[1] <= enemy[1] + ENEMY_SIZE):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - PLAYER_SIZE:
        player_y += player_speed

    # Handle shooting bullets
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player_y])

    # Move enemies, bullets and check for collisions
    move_enemies()
    move_bullets()
    check_collisions()

    # Create new enemies
    enemy_timer += 1
    if enemy_timer >= enemy_spawn_rate:
        create_enemy()
        enemy_timer = 0

    # Draw player, bullets, and enemies
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, (bullet[0], bullet[1], BULLET_SIZE, 20))

    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
