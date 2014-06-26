###############
#MODELO 2
###############

import sys,pygame,math
from random import randint

#Clase pista
class Pista:
    
    def __init__(self, px,py,flow, angle,lon,sz,width,show,adj):
        self.px = px
        self.py = py
        self.flow = flow
        self.angle = angle
        self.lon = lon
        self.lonx = lon*math.cos(math.radians(angle))
        self.lony = lon*math.sin(math.radians(angle))
        self.sz = sz
        self.width = width
        self.show = show
        self.adj = adj
        self.cars = []
        self.x = 1
        
        for i in range(sz):
            xx = px
            yy = py-width/4
            yy2 = py+width/6
            #if flow<0:
            #    xx = py+self.lonx
            #    yy = py+self.lony+width/4
            #    yy2 = py+self.lony-width/6    
            car = Point(xx,yy,flow*math.cos(math.radians(angle)),flow*math.sin(math.radians(angle)))
            self.cars.append(car)
            car = Point(xx,yy2+randint(0,4),flow*math.cos(math.radians(angle)),flow*math.sin(math.radians(angle)))
            self.cars.append(car)
        self.cars[0].started=True
        self.image = pygame.image.load('car.png')
        self.image = pygame.transform.scale(self.image, (30,15))
        self.image = pygame.transform.rotate(self.image,-angle)
        

    def pos(self,xx,y,xxx,yy):
        return math.sqrt(math.pow(xx-xxx,2) + math.pow(y-yy,2))
        
    
    def update(self):
        x  = self.x
        
        if x==0:
            if self.pos(self.cars[self.sz-1].px,self.cars[self.sz-1].py,self.px,self.py)>randint(30,50) or not self.cars[self.sz-1].started:
                self.cars[x].started=True
                self.x+=1
                
        if x>0 and x<self.sz and self.pos(self.cars[x-1].px,self.cars[x-1].py,self.px,self.py)>randint(30,50):
            #print (self.pos(self.cars[x-1].px,self.cars[x-1].py)- self.pos(self.px,self.py))
            self.cars[x].started=True
            self.x+=1   
        vals = [-self.width/4,self.width/7]
        for car in self.cars:
            if car.started:
                car.update()
                if abs(self.lony)<0.1: self.lony =0
                if abs(self.lonx)<0.1: self.lonx =0
                if self.pos(self.lonx+self.px, self.lony+self.py,car.px,car.py) < 22:
                    car.px=self.px
                    car.py=self.py + vals[randint(0,1)] + randint(0,4)
                    car.started=False
                    car.cycle=True
                    self.x=0
               
        #if car[0] llego al final del tramo, pistas adyacentes empiezan

#Clase carro
class Point:
    def __init__(self,px,py,velx,vely):
        self.px = px
        self.py = py
        self.vx = velx
        self.vy = vely
        self.started = False
        self.cycle = False

    def update(self):
        self.px += self.vx
        self.py += self.vy



FPS = 60
pygame.init()
size = width, height = 800,600
black = 0,255,0
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
last_fps = 0

#SONIDO
try:
    pygame.mixer.music.load('music.ogg')
except:
    raise UseWarning, "No se cargo el archivo"

#ACA SE DEFINEN LAS PISTAS CON SUS VARIABLES
pista = []

        
###############
#MODELO 2
###############    
pista1 = Pista(400,140,7,270,150,9,80,True,[])
pista2 = Pista(0,300,7,0,200,20,80,True,[2])
pista3 = Pista(800,299,7,180,245,9,80,True,[])
pista4 = Pista(377,477,7,90,150,20,80,True,[2])
pista5 = Pista(400,108,7,136,280,9,80,True,[])
pista6 = Pista(200,300,7,45,250,20,80,True,[2])
pista7 = Pista(565,293,7,225,240,20,90,True,[2])
pista8 = Pista(377,477,7,315,260,20,80,True,[])

pista.append(pista6)
pista.append(pista2)
pista.append(pista5)
pista.append(pista3)
pista.append(pista8)
pista.append(pista4)
pista.append(pista7)
pista.append(pista1)


    
def update():
    for road in pista:
        #if point.started:
        road.update()

def draw():
    for road in pista:
        pygame.draw.lines(screen,(30,30,30),False, [(road.px,road.py),(road.px+road.lonx,road.py+road.lony)],road.width)
        x=road.px
        y=road.py
        tot = road.lon/40
        for i in range(tot/2+1):
            pygame.draw.lines(screen, (255,255,255), False,[(x,y), (x+road.lonx/tot,y+road.lony/tot)],5)
            if abs(road.lonx)>0.1: x=x+(abs(road.lonx)/road.lonx)*80
            if abs(road.lony)>0.1: y=y+(abs(road.lony)/road.lony)*80
        
        
        ###############
        #MODELO 2
        ###############
        # 30, 30, 30
        pygame.draw.lines(screen, (0,255,0), False,[(310,0), (310,100)],50)
        pygame.draw.lines(screen, (0,255,0), False,[(150,341), (150,440)],100)
        pygame.draw.lines(screen, (0,255,0), False,[(650,150), (650,250)],100)
        pygame.draw.lines(screen, (0,255,0), False,[(450,500), (450,600)],60)
        
        
        
        if road.show:
            #Actualizamos las pistas adyacentes una ves que el carro 0 da 1 vuelta completa para dar la ilusion de flujo
            if road.cars[0].cycle:
                for a in road.adj:
                    pista[a].show=True
            for car in road.cars:
                if car.started:
                    screen.blit(road.image, (car.px,car.py))
                    #pygame.draw.circle(screen, points[i].color, (points[i].px,points[i].py), points[i].rad)        


pygame.mixer.music.play(-1)   
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    
    
    #############
    #MODELO 2
    #############
    pygame.draw.lines(screen, (30,30,30), False,[(385,440), (535,288)],40)
    pygame.draw.lines(screen, (30,30,30), False,[(395,500), (550,340)],32)
    pygame.draw.lines(screen, (30,30,30), False,[(240,300), (400,144)],32)
    
    
    
    
    if pygame.time.get_ticks() - last_fps > FPS:
        last_fps = pygame.time.get_ticks()
        draw()
        pygame.display.flip()
        update()
        
        
        
        
