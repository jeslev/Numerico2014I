###############
#MODELO 3
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
                if self.pos(self.lonx+self.px, self.lony+self.py,car.px,car.py) < 20:
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
#MODELO 3
###############
pista1a = Pista(325,125,7,180,150,9,50,True,[])
pista1b = Pista(475,125,7,180,150,9,50,True,[])
pista1c = Pista(630,125,7,180,155,9,50,True,[])
pista3a = Pista(170,475,7,0,155,9,50,True,[])
pista3b = Pista(325,475,7,0,150,9,50,True,[])
pista3c = Pista(475,475,7,0,150,9,50,True,[])
pista2a = Pista(175,150,7,90,75,20,50,True,[])
pista2b = Pista(175,225,7,90,150,20,50,True,[])
pista2c = Pista(175,375,7,90,75,20,50,True,[])
pista4a = Pista(625,450,7,270,75,20,50,True,[2])
pista4b = Pista(625,375,7,270,150,20,50,True,[2])
pista4c = Pista(625,225,7,270,75,20,50,True,[2])
pista5 = Pista(325,0,7,90,100,20,50,True,[2])
pista6 = Pista(150,225,7,180,150,20,50,True,[2])
pista7 = Pista(0,375,7,0,150,20,50,True,[2])
pista8 = Pista(325,500,7,90,100,20,50,True,[2])
pista9 = Pista(475,600,7,270,100,9,50,True,[])
pista10 = Pista(650,375,7,0,150,9,50,True,[])
pista11 = Pista(800,225,7,180,150,9,50,True,[])
pista12 = Pista(475,100,7,270,100,9,50,True,[])


#pista.append(pista6)
#pista.append(pista5)
#pista.append(pista2c)
pista.append(pista4a)
pista.append(pista4b)
pista.append(pista4c)
pista.append(pista1c)
pista.append(pista1b)
pista.append(pista1a)
pista.append(pista3c)
pista.append(pista3b)
pista.append(pista3a)
pista.append(pista10)
pista.append(pista11)
pista.append(pista12)
pista.append(pista2c)
pista.append(pista2b)
pista.append(pista2a)
pista.append(pista5)    
pista.append(pista6)
pista.append(pista7)
pista.append(pista9)
pista.append(pista8)
def update():
    for road in pista:
        #if point.started:
        road.update()

def draw():
    for road in pista:
        pygame.draw.lines(screen,(30,30,30),False, [(road.px,road.py),(road.px+road.lonx,road.py+road.lony)],road.width)
        x=road.px
        y=road.py
        tot = road.lon/30
        for i in range(tot/2+1):
            pygame.draw.lines(screen, (255,255,255), False,[(x,y), (x+road.lonx/tot,y+road.lony/tot)],4)
            if abs(road.lonx)>0.1: x=x+(abs(road.lonx)/road.lonx)*50
            if abs(road.lony)>0.1: y=y+(abs(road.lony)/road.lony)*50
        
        ###############
        #MODELO 3
        ###############
        #pygame.draw.lines(screen, (30,30,30), False,[(150,375), (200,375)],4)
        pygame.draw.lines(screen, (30,30,30), False,[(170,150), (170,101)],40)
        pygame.draw.lines(screen, (0,255,0), False,[(130,150), (130,101)],40)
        
        #pygame.draw.lines(screen, (30,30,30), False,[(625,451), (625,500)],50)
        #pygame.draw.lines(screen, (30,30,30), False,[(170,150), (170,101)],40)        
        
        
        
        
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
    pygame.draw.lines(screen, (30,30,30), False,[(625,451), (625,500)],50)
    pygame.draw.lines(screen, (30,30,30), False,[(630,150), (630,101)],40)
    pygame.draw.lines(screen, (30,30,30), False,[(175,451), (175,500)],50)
    #pygame.draw.lines(screen, (30,30,30), False,[(170,450), (170,500)],40)
    
    
    
    
    if pygame.time.get_ticks() - last_fps > FPS:
        last_fps = pygame.time.get_ticks()
        draw()
        pygame.display.flip()
        update()
        
        
        
        
