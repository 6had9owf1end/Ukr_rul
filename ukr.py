import pygame 
import random
import time
back=0,0,0
pygame.init()
clock = pygame.time.Clock()
window_game = pygame.display.set_mode((800,533))   
window_game.fill((0, 0, 0))
#Создание игрового окна и заливка черного света
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color= back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window_game, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=14, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('helvetica', fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        window_game.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image =pygame.image.load(filename)

    def draw(self):
        window_game.blit(self.image, (self.rect.x, self.rect.y)) 
hp=1
hp_pl1=1
hp_pl2=1
hps=Picture('hp1.png',500,25,100,250)
bg=Picture('bg1.png',1,1,800,600)
gun=Picture('images.png',250,150,500,250)
but=Picture('fire.png',50,100,220,164)
butleft=Picture('fireleft.png',550,100,220,164)
hps_pl1=Picture('hp1.png',25,25,100,250)
hps_pl2=Picture('hp1.png',550,25,100,250)
boom=Picture('boom.png',315,150,220,164)
use=Picture('drag.png',25,250,250,250)

uselist=[pygame.image.load('drag1.png'),pygame.image.load('drag2.png'),          
pygame.image.load('drag3.png'),pygame.image.load('drag4.png'),                
pygame.image.load('drag5.png'),pygame.image.load('drag6.png')]
i=1
fire_left=False 
pl1=Picture('pl1.png',25,100,350,500)
pl2=Picture('pl2.png',450,100,350,500)
pl1orpl2=Picture('pl1orpl2.png',400,0,10,800)
cheats1=Picture('mistikdrag.png',575,200,250,250)
x1=Picture('x.png',625,425,50,50)
col=Picture('1x.png',700,425,50,50)
game=True

while game:
  hp=1
  hp_pl1=1
  hp_pl2=1  
  cheats_pl1=1 
  i=1
  bg.draw()
  pl1.draw()
  pl2.draw()
  pl1orpl2.draw()
  wait=20
  ass=random.randint(1,6)
  for event in pygame.event.get(): 
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if pl1.collidepoint(x,y):
            while True:
                bg.draw()
                but.draw()
                gun.draw()
                use.draw()
                cheats1.draw()
                x1.draw()
                col.draw()
                but.image=pygame.image.load('fire.png') 
                if wait==0:
                    use.image=pygame.image.load('drag.png')
                    wait=20
                else:
                    wait=wait-1
                if cheats_pl1==0:
                    col.image=pygame.image.load('0x.png')
                else:
                    col.image=pygame.image.load('1x.png')
                if hp==1:
                    hps.image=pygame.image.load('hp1.png')
                elif hp==0:
                    break
                hps.draw()
                for event in pygame.event.get(): 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if but.collidepoint(x,y):
                            but.image=pygame.image.load('fire1.png')
                            if i==ass:
                                wait = 10
                                hp-=1
                                boom.draw()    
                            elif i!=ass:
                                i+=1
                        if use.collidepoint(x,y):
                            ass=random.randint(1,6)
                            i=1
                        if cheats1.collidepoint(x,y):
                            if cheats_pl1>0:
                                if ass==1:
                                    use.image=pygame.image.load('drag1.png')
                                elif ass==2:
                                    use.image=pygame.image.load('drag2.png')
                                elif ass==3:
                                    use.image=pygame.image.load('drag3.png')
                                elif ass==4:
                                    use.image=pygame.image.load('drag4.png')
                                elif ass==5:
                                    use.image=pygame.image.load('drag5.png')
                                elif ass==6:
                                    use.image=pygame.image.load('drag6.png')
                                cheats_pl1=0
                pygame.display.update()
                clock.tick(40)
        elif pl2.collidepoint(x,y):
            while True:
                
                bg.draw()
                use.draw()
                but.draw()
                butleft.draw()
                gun.draw()
                
                but.image=pygame.image.load('fire.png') 
                but_left=pygame.image.load('fireleft.png')
                use.image=pygame.image.load('drag.png')
                
                if hp_pl1==1:
                    hps_pl1.image=pygame.image.load('hp1.png')
                elif hp_pl1==0:
                    break
                hps_pl1.draw() 
                
                
                if hp_pl2==1:
                    hps_pl2.image=pygame.image.load('hp1.png')
                elif hp_pl2==0:
                    break
                hps_pl2.draw() 


                for event in pygame.event.get(): 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos             
                        if but.collidepoint(x,y):
                            but.image=pygame.image.load('fire1.png')
                            if i==ass:
                                hp_pl1-=1                    
                                boom.draw() 
                            elif i!=ass:
                                i=i+1
                        elif butleft.collidepoint(x,y):
                            but_left=pygame.image.load('fire1_left.png')
                            if i==ass:
                                hp_pl2-=1
                                boom.draw()
                            elif i!=ass:
                                i=i+1 
                        if use.collidepoint(x,y):
                            ass=random.randint(1,6)
                            i=1
                pygame.display.update()
                clock.tick(40)
        elif pl1orpl2.collidepoint(x,y):
            game=False
  pygame.display.update()
  clock.tick(40)