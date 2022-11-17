# ICS3U - Computer Science CPT

### Game Title
Describe your game here.

My game is a game of cosmic elements. This game is like the popular game of It takes two. It's a two-player game. The game requires two players to play against each other. The story is set in a vast universe. Because the universe is short of energy in 2077. Many spacecraft go out into space to compete for the few resources available. But because of various problems, there are only two of the most powerful spacecraft left in the universe. Each player controls a spaceship. You need to shoot lasers to defeat the opposing spacecraft. He became the only king in the universe. Game Settings: the game of the spacecraft can be left or right straight flight, up and down flight, oblique flight. Spaceships can also fire in bursts (note: due to the game's Settings, only 5 lasers can be fired at one time). The red line in the middle of the map is boder. This prevents the player from reaching another player's territory. This forces the player to shoot from a distance. There are also two green lines on the map, and the area behind these two green lines is the Cure Area. When a spaceship enters the Cure area it will restore 1 shield value and will not regenerate. When the player leaves the area within the green line, that point of shield value disappears. It will not recover until the player re-enters the Cure Area. Player control: The player on the left controls the spaceship with the W,A,S,D keys, and shoots the blue laser with the E key. The player on the right controls the spaceship by going up, down, left, and right keys. Shoot the red laser with the Rutern key. Each ship has an initial shield value of 10 points. The first to run out of Shield players lose.

### Group members:
- member 1 Charlie Cao (Individul)
- member 2
- etc...


---

### Groups

Being in a group means having a cohesive game theme and story. It **does not** mean using other team member's code and repurposing it as your own. Each person's contributions must be utterly unique.

There are things that are allowed to be copied. These are exampled of things that will not be marked as part of your contribution:
- Images and game assets
- The drawing of specific game characters or scenery

If you do copy someone else's code in this regard, you *must* give them an attribution with a comment as follows.

```python
# Written by Dave D.
# dave_cpt.py
for x in range(100, 500, 50):
    pygame.draw.rect(....)
# ------------------
```

## Requirements
- Variables
- If statements
    - `if/elif/else`
    - Boolean statement
    - Boolean operator
    - Comparison operator
    - condition
- Loops
    - Iterate
    - condition
    - loop/counter/accumulator variable
    - break
    - continue
- Lists
    - initialize
    - append
    - iterate/traverse
    - element
    - index
- Functions
    - parameter
    - argument
    - return (type)
    - annotation
    - docstring
    - global/local/parameter variables
- Formatting and naming conventions

## Submission
If you are in a group, only one person will sumbit on behalf of the entire group.

#King of universe game
import pygame
import os
pygame.font.init()

#introduce
print("Universe two versus game")
print("Fight your opponent in the vastness of the universe.")
print("Defeat the enemy and become the ultimate king.")



#set the size of the game
WIDTH, HEIGHT = 1000, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

#color setting
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
GREEN = (0,255,0)




#font setting
SHIELD_FONT = pygame.font.SysFont('comicsans', 30) 
WINNER_FONT = pygame.font.SysFont('comicsans', 90)
INTRO_FONT = pygame.font.SysFont('comicsans', 30)
CURE_FONT = pygame.font.SysFont('comicsans', 15)
TITLE_FONT = pygame.font.SysFont('comicsans', 25)

#The variables needs for game #Variables
FPS = 60 #The frams per second
VEL = 6 #velocity
LASER_VEL = 8
MAX_LASERS = 5 #Limite the Laser can shoot one time.

#Set the players' size
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40

PLAYER_L_HIT = pygame.USEREVENT + 1
PLAYER_R_HIT = pygame.USEREVENT + 2

#BORDER Settinging
BORDER = pygame.Rect(WIDTH//2 - 5,0,8,HEIGHT)
#CURELINE Setting
CURE_LINE_L = pygame.Rect(WIDTH//2 - 300,0,8,HEIGHT)
CURE_LINE_R = pygame.Rect(WIDTH//2 + 300,0,8,HEIGHT)
#The way to load the image (player and background) #attribute online loadimage method
PLAYER_L_IMAGE = pygame.image.load(os.path.join('materials', 'New_spaceship_blue.png'))
PLAYER_L = pygame.transform.rotate(pygame.transform.scale(PLAYER_L_IMAGE,(PLAYER_WIDTH, PLAYER_HEIGHT)),270) #rotate the image

PLAYER_R_IMAGE = pygame.image.load(os.path.join('materials', 'spaceship_red.png'))
PLAYER_R = pygame.transform.rotate(pygame.transform.scale(PLAYER_R_IMAGE,(PLAYER_WIDTH, PLAYER_HEIGHT)),270) 

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('materials', 'space3.png')),(WIDTH, HEIGHT))


def draw_window(player_r, player_l,player_r_lasers, player_l_lasers, player_r_health, player_l_health): #draw the background
    SCREEN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(SCREEN, RED, BORDER) #Draw the border
    pygame.draw.rect(SCREEN , GREEN, CURE_LINE_L)
    pygame.draw.rect(SCREEN, GREEN, CURE_LINE_R)
    
    if player_l.x < CURE_LINE_L.x:
        player_l_health += 1
    if player_r.x > CURE_LINE_R.x:
        player_r_health += 1
    


    player_r_health_text = SHIELD_FONT.render("Shiled: " + str(player_r_health), 1, GREEN)
    player_l_health_text = SHIELD_FONT.render("Shiled: " + str(player_l_health), 1, GREEN)
    cure1_text = CURE_FONT.render("This is the cure area ~ ~ ~" ,1, RED)
    cure2_text = CURE_FONT.render("This is the cure area ~ ~ ~" ,1, RED)
    title_text = TITLE_FONT.render("The king of the universe",1,WHITE)
    #Change Text color when the value is low
    if player_r_health <= 5:
        player_r_health_text = SHIELD_FONT.render("Shiled: " + str(player_r_health), 1, RED)
    if player_l_health <= 5:
        player_l_health_text = SHIELD_FONT.render("Shiled: " + str(player_l_health), 1, RED)
        
        
    

    SCREEN.blit(player_r_health_text,(WIDTH - player_r_health_text.get_width() - 10,10))
    SCREEN.blit(player_l_health_text,(10,10))

    SCREEN.blit(cure1_text,(WIDTH - cure1_text.get_width() - 10,50))
    SCREEN.blit(cure2_text,(10,50))

    SCREEN.blit(title_text,(WIDTH - cure1_text.get_width() - 455,15))

   


    SCREEN.blit(PLAYER_L, (player_l.x, player_l.y))
    SCREEN.blit(PLAYER_R, (player_r.x,player_r.y))
    #draw the bullet
    for laser in player_r_lasers:
        pygame.draw.rect(SCREEN,RED,laser)
    
    for laser in player_l_lasers:
        pygame.draw.rect(SCREEN,BLUE,laser)
    
    pygame.display.update()

   
    
# Don't let player move out the screen and accross the border
def player_l_movement(keys_pressed,player_l):
    if keys_pressed[pygame.K_a] and player_l.x - VEL > 0: #LEFT
         player_l.x -= VEL
    if keys_pressed[pygame.K_d] and player_l.x + VEL + player_l.width < BORDER.x:  #RIGHT
         player_l.x += VEL
    if keys_pressed[pygame.K_w] and player_l.y - VEL > 0: #UP 
         player_l.y -= VEL
    if keys_pressed[pygame.K_s] and player_l.y + VEL < HEIGHT - 15: #DOWN 
         player_l.y += VEL       

def player_r_movement(keys_pressed,player_r):
    if keys_pressed[pygame.K_LEFT] and player_r.x - VEL > BORDER.x + BORDER.width:#LEFT
         player_r.x -= VEL
    if keys_pressed[pygame.K_RIGHT]and player_r.x + VEL + player_r.width < WIDTH: #RIGHT
         player_r.x += VEL
    if keys_pressed[pygame.K_UP] and player_r.y - VEL > 0: #UP 
         player_r.y -= VEL
    if keys_pressed[pygame.K_DOWN]and player_r.y + VEL < HEIGHT - 15: #DOWN
         player_r.y += VEL    



def lasers_movement(player_l_lasers, player_r_lasers, yellow, red):
    for laser in player_l_lasers:
        laser.x += LASER_VEL
        if red.colliderect(laser): #attribute Online
            pygame.event.post(pygame.event.Event(PLAYER_R_HIT))
            player_l_lasers.remove(laser)
        elif laser.x > WIDTH:
            player_l_lasers.remove(laser)
    
    for laser in player_r_lasers:
        laser.x -= LASER_VEL
        if yellow.colliderect(laser): #attribute Online
            pygame.event.post(pygame.event.Event(PLAYER_L_HIT))
            player_r_lasers.remove(laser)
        elif laser.x < 0:
            player_r_lasers.remove(laser)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    SCREEN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2)) #The function to put the text on the  screen
    pygame.display.update()
    pygame.time.delay(2500) #delay setting
    


    

def main():
    player_r= pygame.Rect(650,225,PLAYER_WIDTH,PLAYER_HEIGHT) #Position
    player_l= pygame.Rect(300,225,PLAYER_WIDTH,PLAYER_HEIGHT)
     
    #player health setting
    player_r_health = 10
    player_l_health = 10 

    player_r_lasers=[]
    player_l_lasers=[]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #control the FPS the game run， if its on the different divice, it's still the same FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
 
            #control the bullet
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_e and len(player_l_lasers) < MAX_LASERS: #The way to fire， set e to fire
                 laser = pygame.Rect(player_l.x + player_l.width, player_l.y+player_l.height//2 - 2, 10, 5)
                 player_l_lasers.append(laser)
                 
              if event.key == pygame.K_RETURN and len(player_r_lasers) < MAX_LASERS: #Limit the lasers number, set return to fire.
                 laser = pygame.Rect(player_r.x , player_r.y+ player_r.height//2 - 2, 10, 5) 
                 player_r_lasers.append(laser)
            
            if event.type == PLAYER_R_HIT: #Damage 
              player_r_health -= 1
              print(f"Right side player got hurt. Residual health value {player_r_health} ")
            
            if event.type == PLAYER_L_HIT:
              player_l_health -= 1
              print(f"Left side player got hurt. Residual health value {player_l_health} ")
        
    
        #Who win the game text
        winner_text = ""
        if player_r_health <=0:
            winner_text = "PLAYER_L Wins!"
            
        if player_l_health <= 0:
            winner_text = "PLAYER_R Wins!"
            
        if winner_text != "":
            draw_winner(winner_text)
            break
        

        
        
        
        keys_pressed = pygame.key.get_pressed()
        player_l_movement(keys_pressed, player_l)
        player_r_movement(keys_pressed, player_r)
        
        lasers_movement(player_l_lasers , player_r_lasers, player_l, player_r)

        draw_window(player_r, player_l, player_r_lasers, player_l_lasers,player_r_health, player_l_health) #draw the background

    main()




if __name__ == "__main__":
    main()



### Play-through Video
Each group is to submit one play-through video (Five minutes) and explain it.

### Code explanation video
Each group member is to submit a five minute explanation of their own code and how it works. You must find examples of each of the topics in the requirements. If you have too many to show, just show your best work. The video's filename *must* include your full name.

**Please note:** The code explanation video is supposed to be an explanation of your code and how it works. You must use technical language to show me you know what these concepts are. This is not a video where you only say "here is a function I wrote". See the sub-topics under the requirements for key words you should know and use.

### GitHub code
Be sure to constantly update your GitHub repository.
