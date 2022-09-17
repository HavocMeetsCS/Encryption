import pygame, sys
from pygame import mixer
from Binary import *
# Imports ^^^^

action = False
Start = True
Menu = False
Binary = False
Text_Mode = False
Binary_Decode = False
Text_Mode_Decode = False
#Setup

pygame.init()
clock = pygame.time.Clock()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))



#Sprites

class button(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,picture):
        super().__init__() 
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.clicked = False

    def draw(self,simage):
        action = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): 
            simage.draw(screen)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                mouse_down.play()
                self.clicked = True
                action = True
                print("CLICKED")
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return(action)

# Audio

mouse_down = mixer.Sound("Audio_Assets/mixkit-video-game-retro-click-237.wav")
n = 32
m = 20
base_font = pygame.font.Font(None,n)
base_font1 = pygame.font.Font(None,m)
user_text = "D"
binary_output = " "
# Audio ^

class misc(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,picture):
        super().__init__() 
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

#Groups ---

size_buttonp1 = button(20,475,"Assets\z.png")
size_buttonpg = pygame.sprite.Group()
size_buttonpg.add(size_buttonp1)

size_buttonp2 = button(20,475,"Assets\z-pixilart.png")
size_buttonpg1 = pygame.sprite.Group()
size_buttonpg1.add(size_buttonp2)

minus_buttonp1 = button(40,475,"Assets\z-pixilart (1).png")
minus_buttonpg = pygame.sprite.Group()
minus_buttonpg.add(minus_buttonp1)

minus_buttonp2 = button(40,475,"Assets\z-pixilart (2).png")
minus_buttonpg1 = pygame.sprite.Group()
minus_buttonpg1.add(minus_buttonp2)


# Starting button Groups

start_button1 = button(250,250,"Assets/pixilart-drawing (88).png")
start_buttong = pygame.sprite.Group()
start_buttong.add(start_button1)

start_button2 = button(250,250,"Assets/playbuttonu-pixilart.png")
start_buttong1 = pygame.sprite.Group()
start_buttong1.add(start_button2)

# Menu Button Groups

binary_buttonu = button(250,115,"Assets/binary_button.png")
binary_buttong = pygame.sprite.Group()
binary_buttong.add(binary_buttonu)

binary_buttonu2 = button(250,115,"Assets/binary-button-pixilart.png")
binary_buttong2 = pygame.sprite.Group()
binary_buttong2.add(binary_buttonu2)

# To Menu Button Groups

binary_buttonz = button(470,470,"Assets/menu-pixilart.png")
binary_buttonz1 = pygame.sprite.Group()
binary_buttonz1.add(binary_buttonz)

binary_buttonz2 = button(470,470,"Assets/menu-pixilart1.png")
binary_buttonz22 = pygame.sprite.Group()
binary_buttonz22.add(binary_buttonz2)

# Binary Encode Groups 

encode_button = button(250,235,"Assets/binare.png")
encode_buttong = pygame.sprite.Group()
encode_buttong.add(encode_button)

encode_button2 = button(250,235,"Assets/binaree.png")
encode_buttong2 = pygame.sprite.Group()
encode_buttong2.add(encode_button2)

# Binary Decode Groups 

decode_button = button(250,400,"Assets/binardec.png")
decode_buttong = pygame.sprite.Group()
decode_buttong.add(decode_button)

decode_button2 = button(250,400,"Assets/binardec2.png")
decode_buttong2 = pygame.sprite.Group()
decode_buttong2.add(decode_button2)

# Misc Groups

Title = pygame.sprite.Group()
title = misc(250,50,"Assets/pixilart-drawing (8).png")
Title.add(title)

TitleB = pygame.sprite.Group()
title2 = misc(250,50,"Assets/binar_title.png")
TitleB.add(title2)

Wall_Trigger = pygame.sprite.Group()


color2 = (255,0,0)

x = 0
#Groups ---

input_rect = pygame.Rect(20,100,140,32)
pygame.display.set_caption("ENCRYPTION")
background = pygame.image.load("Assets/decoderbg-pixilart.png")
color_active = pygame.Color("lightskyblue3")
color_passive = pygame.Color("grey15")
color = color_passive
listi = []
active1 = False
x = 0
print(ENCODEB)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active1 = True
            else:
                active1 = False   
        if active1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode
    base_font = pygame.font.Font(None,n)
    base_font1 = pygame.font.Font(None,m)
    if active1:
        color = color_active
    else:
        color = color_passive
    pos = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    if Text_Mode:
        if size_buttonp1.draw(size_buttonpg1):
            m = m + 5
        if minus_buttonp1.draw(minus_buttonpg1): 
            m = m - 5
        if m >= 55:
            m = m - 1
        pygame.draw.rect(screen,color,input_rect,2)
        try:
            text_surface = base_font.render(user_text,True,(100,150,100))
        except TypeError and IndexError:
            pass
        screen.blit(text_surface,(input_rect.x + 5,input_rect.y + 5,))
        input_rect.w = max(100,text_surface.get_width()+ 10)
        #Experimental code please edit >>
        listi.append(user_text)
        w = []
        listx = []
        listy = []
        q = str(user_text)
        # This below will be useless for a ingame translator not just terminal use
        #^^^^^^
        q = q.upper()
        q = q.split()
        y = len(q)

        for p in range(y):
            z = len(q[p])
            for i in range(z):
                listx.append(q[p][i])
            z = len(listx)
        if y >= 1:
            for i in range(z):
                try:
                    w.append((ENCODEB[listx[i]]))
                except IndexError and KeyError:
                    pass
                binary_output = str(w)
                text_surface1 = base_font1.render(binary_output,True,(100,100,100))
        screen.blit(text_surface1,(10,34))
        listi = []
    if not Text_Mode_Decode and n < 32:
        n = 32
    if not Text_Mode and m < 20:
        m = 20
    if Text_Mode_Decode:
        if size_buttonp1.draw(size_buttonpg1):
            n = n + 5
        if minus_buttonp1.draw(minus_buttonpg1):     # <--- Make a new subtraction button then fill this in <--- |COMPLETED|
            n = n - 5
        if n >= 47:
            n = n - 1
        pygame.draw.rect(screen,color,input_rect,2)
        w = []
        try:
            text_surface = base_font.render(user_text,True,(100,150,100))
        except TypeError:
            pass
        screen.blit(text_surface,(input_rect.x + 5,input_rect.y + 5,))
        input_rect.w = max(100,text_surface.get_width()+ 10)
        lengthD = len(user_text)
        listo = []
        
        if lengthD >= 8:
            US1 = user_text.split()
            US2 = len(US1)
            try:
                for i in range(US2):
                    w.append(DECODEB[US1[i]])
            except KeyError:
                pass
            binary_output = str(w)
            text_surface1 = base_font1.render(binary_output,True,(100,100,100))
            screen.blit(text_surface1,(10,34))
        ### Experinmental code please edit ^^
# Possibly solution to having a output based on what user inputs is adding a conformation button that starts false ever Loop of the while loop so it only confirms what the user wants to enter once not like 100 times?
    if Start or Menu:
        Title.draw(screen)

    if not Start and not Menu:
        if binary_buttonz.draw(binary_buttonz22):
            Menu = True
            action = False
            Binary = False
            Text_Mode = False
            Binary_Decode = False
            Text_Mode_Decode = False
    if Start:
        if start_button1.draw(start_buttong1):
            Start = False
            Menu = True
    if Menu:
        if binary_buttonu.draw(binary_buttong2):
            Menu = False    
            Binary = True
            print("Binary Mode")
    if Binary:
        TitleB.draw(screen)
        if encode_button.draw(encode_buttong2):
            Binary = False
            Text_Mode = True
            print("Binary Encode Mode")
            pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
        if decode_button.draw(decode_buttong2):
            Binary = False
            Binary_Decode = True
            Text_Mode_Decode = True
            print("Binary Decode Mode")
    #pygame.draw.rect(screen, color2, pygame.Rect(480, 0, 20, 500))
    pygame.display.flip()
    clock.tick(60)
