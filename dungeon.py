# import the pygame module, so you can use it
import pygame
import random

#pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
display_width = 800
display_height = 600

hitpoints = 100
attack = 5
hit_chance = 72
armor = 10
level = 1
special = {1: "slash", 2: "fire bolt", 3: "sprectral touch"}
exp = 0
pig_hp = 25

# define a main function
def main():
    x=50
    y=50
    v_x=700
    v_y=500
    move_rate = 10
    hitpoints = 100
    attack = 5
    hit_chance = 72
    armor = 10
    level = 1
    special = {1: "slash", 2: "fire bolt", 3: "sprectral touch"}
    exp = 0
    pig_hp = 25
    result=0
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("Pig Dungeon")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((display_width,display_height))

    image = pygame.image.load("hero.png")
    villian = pygame.image.load("villian.png")
    transColor = villian.get_at((0,0))
    image.set_colorkey(transColor)
    villian.set_colorkey(transColor)
    encounter = pygame.image.load("fight.png")
    villian.set_colorkey((255,255,255))
    screen.blit(image, (x,y))
    screen.blit(villian, (v_x,v_y))
    pygame.display.flip()
    pygame.mixer.music.load('scary.mp3')
    pygame.mixer.music.play(-1)
    caught = pygame.mixer.Sound('caught.wav')
    oink = pygame.mixer.Sound('oink.wav')
    yay = pygame.mixer.Sound('Victory.wav')
    sad = pygame.mixer.Sound('Trombone.wav')
    pig_alive = True

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
                # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x=x-move_rate
                if event.key == pygame.K_RIGHT:
                    x=x+move_rate
                if event.key == pygame.K_UP:
                    y=y-move_rate
                if event.key == pygame.K_DOWN:
                    y=y+move_rate
                screen.fill((0,0,0))
                screen.blit(image, (x,y))
                if pig_alive:
                    if x < v_x:
                        v_x -= move_rate
                    if x > v_x:
                        v_x += move_rate
                    if y < v_y:
                        v_y -= move_rate
                    if y > v_y:
                        v_y += move_rate
                    screen.blit(villian, (v_x,v_y))
                else:
                    v_x = -100
                    v_y = -100

                pygame.display.flip()
                if abs(v_x-x) <= 40 and abs(v_y-y) <= 40:
                    screen.blit(encounter, (175,0))
                    myfont = pygame.font.SysFont("Arial", 16)
                    choice = myfont.render("a: attack d: defend 1: slice ",0,(255,255,255))
                    screen.blit(choice,(200,100))
                    pygame.display.flip()
                    caught.play()
                    move_rate = 0
                    if event.type == pygame.KEYDOWN:
                        allowed_acions = ['a','d','1']
                        if level >= 2:
                            allowed_acions += '2'
                        if level == 3:
                            allowed_acions += '3'
                        action = chr(event.key)
                        if action not in allowed_acions:
                            continue
                        else:
                            if result == 0:
                                zz=fight(pig_hp,hitpoints,hit_chance,attack,armor,action)
                                print(zz)
                                hitpoints=zz[0]
                                pig_hp=zz[1]
                                result=zz[2]
                                myfont = pygame.font.SysFont("Arial", 16)
                                damage = myfont.render(str(zz[0]) + "     " + str(zz[1]),0,(255,0,0))
                                screen.blit(damage,(x,y-20))
                                pygame.display.flip()
                            elif result == 1:
                                myfont = pygame.font.SysFont("Arial", 16)
                                victory = myfont.render("You have slain the villianous pig!",0,(255,0,0))
                                screen.blit(victory,(v_x-25,v_y-20))
                                pygame.display.flip()
                                pig_alive = False
                                move_rate = 10
                                yay.play()
                            else:
                                myfont = pygame.font.SysFont("Arial", 16)
                                dead = myfont.render("You Have Died. The Pig has his revenge for eating all that bacon.",0,(255,0,0))
                                screen.blit(dead,(v_x-25,v_y-20))
                                pygame.display.flip()
                                sad.play()

                elif abs(v_x-x) <= 120 and abs(v_y-y) <= 120:
                    myfont = pygame.font.SysFont("Arial", 12)
                    warning = myfont.render("Oink, I'm coming for you, my tasty truffle!",0,(255,0,0))
                    screen.blit(warning,(v_x-25,v_y-20))
                    pygame.display.flip()
                    oink.play()
 
def fight(pig_hp,hitpoints,hit_chance,attack,armor,action):
    result=0
    pig_attack = random.randint(3, 12)
    hitpoints -= pig_attack
    if random.randint(0,100) >= hit_chance:
        player_attack = 0
    else:
        player_attack = random.randint(3, attack)
    if action == '3':
        hitpoints -= (player_attack+1 / 2)
        pig_hp -= (player_attack * 3)
    if action == '2':
        hitpoints -= ((player_attack+1) / 4)
        pig_hp -= (player_attack * 2)
    if action == '1':
        pig_hp -= (player_attack * 1.5)
    if action == 'a':
        pig_hp -= (player_attack)
    if action == 'd':
        hitpoints += (player_attack * 1.5)
    if pig_hp <= 0:
        result = 1
    if hitpoints <= 0:
        result = 2
    return(hitpoints, pig_hp, result)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()