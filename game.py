import pygame
import time
import random
pygame.font.init()

WIDTH , HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space doge")

BG = pygame.transform.scale (pygame.image.load("bg.webp"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
STAR_WIDTH = 10  # Define the width of a star
STAR_HEIGHT = 20 # Define the height of a star
STAR_VEL = 5     # Define the velocity of a star

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player , elapsed_time , stars):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"time :{round(elapsed_time)}s" , 1, "white")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, "red", player)
    
    for star in stars:
        pygame.draw.rect(WIN, "yellow", star)
    
    pygame.display.update()
    
    
def main():
    run = True
    
    player = pygame.Rect(100, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    
    start_time = time.time()
    elapsed_time = 0
    
    stars = []  # Initialize the stars list
    hit = False
    
    star_add_increment = 2000 # milliseconds
    star_count = 0    
    
    while run:
        star_count += clock.tick(65)
        elapsed_time = time.time() - start_time
        
        
        if star_count >= star_add_increment:
            for _ in range(5):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50) # Increase the interval for adding stars    
            star_count = 0        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: 
            player.x -= PLAYER_VEL 
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH: 
            player.x += PLAYER_VEL 
            
        for star in stars[:]:
            star.y += STAR_VEL  
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star) 
                hit = True
                break  # Exit the loop if a star is hit
                
        if hit:
            lost_text = FONT.render("You lost!" , 1, "white")
            WIN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2 - lost_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(4000) 
            break # Wait for 2 seconds before quitting
        
        draw(player , elapsed_time , stars)    
            
    pygame.quit()

if __name__ == "__main__":
    main()
    
    
    
    
        
            
            
