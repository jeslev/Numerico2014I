###############
#MODELO 1
###############


import sys,pygame,math
from random import randint

#Clase 
class Pieza:
    
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
            yy = py-3
            #if flow<0:
            #    xx = py+self.lonx
            #    yy = py+self.lony+width/4
            #    yy2 = py+self.lony-width/6    
            car = Flecha(xx,yy,flow*math.cos(math.radians(angle)),flow*math.sin(math.radians(angle)))
            self.cars.append(car)
        self.cars[0].started=True
        self.image = pygame.image.load('misc_26.png')
        self.image = pygame.transform.scale(self.image, (20,8))
        self.image = pygame.transform.rotate(self.image,-angle)
        

    def pos(self,xx,y,xxx,yy):
        return math.sqrt(math.pow(xx-xxx,2) + math.pow(y-yy,2))
        
    
    def update(self):
        x  = self.x
        
        if x==0:
            if self.pos(self.cars[self.sz-1].px,self.cars[self.sz-1].py,self.px,self.py)>30 or not self.cars[self.sz-1].started:
                self.cars[x].started=True
                self.x+=1
                
        if x>0 and x<self.sz and self.pos(self.cars[x-1].px,self.cars[x-1].py,self.px,self.py)>30:
            #print (self.pos(self.cars[x-1].px,self.cars[x-1].py)- self.pos(self.px,self.py))
            self.cars[x].started=True
            self.x+=1   
        for car in self.cars:
            if car.started:
                car.update()
                if abs(self.lony)<0.1: self.lony =0
                if abs(self.lonx)<0.1: self.lonx =0
                if self.pos(self.lonx+self.px, self.lony+self.py,car.px,car.py) < 22:
                    car.px=self.px
                    car.py=self.py
                    #car.started=False
                    car.cycle=True
                    self.x=0
               
        #if car[0] llego al final del tramo, Piezas adyacentes empiezan

#Clase flecha
class Flecha:
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
black = 51,0,102
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
last_fps = 0

#ACA SE DEFINEN LAS PiezaS CON SUS VARIABLES
piezas = []
###############
#MODELO 1
###############
pieza1 = Pieza(50,350,7,0,700,20,8,True,[])
pieza3 = Pieza(100,263,7,120,100,20,8,True,[2])
pieza2 = Pieza(700,263,7,180,600,20,8,True,[])
pieza4 = Pieza(100,263,7,60,100,20,8,True,[2])
pieza5 = Pieza(200,263,7,120,100,20,8,True,[2])
pieza6 = Pieza(200,263,7,60,100,20,8,True,[2])
pieza7 = Pieza(300,263,7,120,100,20,8,True,[2])
pieza8 = Pieza(300,263,7,60,100,20,8,True,[2])
pieza9 = Pieza(400,263,7,120,100,20,8,True,[2])
pieza10 = Pieza(400,263,7,60,100,20,8,True,[2])
pieza11 = Pieza(500,263,7,120,100,20,8,True,[2])
pieza12 = Pieza(500,263,7,60,100,20,8,True,[2])
pieza13 = Pieza(600,263,7,120,100,20,8,True,[2])
pieza14 = Pieza(600,263,7,60,100,20,8,True,[2])
pieza15 = Pieza(700,263,7,120,100,20,8,True,[2])
pieza16 = Pieza(700,263,7,60,100,20,8,True,[2])



piezas.append(pieza6)
piezas.append(pieza2)
piezas.append(pieza5)
piezas.append(pieza3)
piezas.append(pieza8)
piezas.append(pieza4)
piezas.append(pieza7)
piezas.append(pieza1)
piezas.append(pieza9)
piezas.append(pieza10)
piezas.append(pieza11)
piezas.append(pieza12)
piezas.append(pieza13)
piezas.append(pieza14)
piezas.append(pieza15)
piezas.append(pieza16)
myfont = pygame.font.SysFont("monospace", 30)
    
def update():
    for road in piezas:
        #if Flecha.started:
        road.update()

def draw():
    label = myfont.render("MECANICA Y ESTATICA EN MATRICES", 4, (255,255,0))
    screen.blit(label, (150, 100))
    for road in piezas:
        pygame.draw.lines(screen,(102,51,0),False, [(road.px,road.py),(road.px+road.lonx,road.py+road.lony)],road.width)
        #x=road.px
        #y=road.py
        #tot = road.lon/30
        #for i in range(tot/2+1):
        #    pygame.draw.lines(screen, (255,255,255), False,[(x,y), (x+road.lonx/tot,y+road.lony/tot)],4)
        #    if abs(road.lonx)>0.1: x=x+(abs(road.lonx)/road.lonx)*80
        #    if abs(road.lony)>0.1: y=y+(abs(road.lony)/road.lony)*80
        
        
        
        
        if road.show:
            #Actualizamos las Piezas adyacentes una ves que el carro 0 da 1 vuelta completa para dar la ilusion de flujo
            if road.cars[0].cycle:
                for a in road.adj:
                    piezas[a].show=True
            for car in road.cars:
                if car.started:
                    screen.blit(road.image, (car.px,car.py))
                    #pygame.draw.circle(screen, points[i].color, (points[i].px,points[i].py), points[i].rad)        


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    
    #wood = pygame.image.load('wood.jpg')    
    #screen.blit(wood,(50,350))
    pygame.draw.lines(screen, (153,76,0), False,[(50,350), (750,350)],4)
    pygame.draw.lines(screen, (153,76,0), False,[(100,263), (700,263)],4)
    pygame.draw.lines(screen, (153,76,0), False,[(50,350),(100,263),(150,350),(200,263),(250,350),(300,263),(350,350),(400,263),(450,350),(500,263),(550,350),(600,263),(650,350),(700,263),(750,350)],4)
    
    arrow1 = pygame.image.load('flecha.png')
    arrow1 = pygame.transform.scale(arrow1, (60,20))
    arrow2 = arrow1
    arrow3 = arrow1
    arrow4 = arrow1
    arrow5 = arrow1
    arrow6 = arrow1
    arrow7 = arrow1
    arrow1 = pygame.transform.rotate(arrow1,90)
    arrow3 = pygame.transform.rotate(arrow3,270)
    arrow4 = pygame.transform.rotate(arrow4,315)
    arrow5 = pygame.transform.rotate(arrow5,270)
    arrow6 = pygame.transform.rotate(arrow6,240)
    arrow7 = pygame.transform.rotate(arrow7,90)
    
    screen.blit(arrow1,(40,350))
    screen.blit(arrow2,(-8,343))
    screen.blit(arrow3,(92,203))
    screen.blit(arrow4,(254,213))
    screen.blit(arrow5,(492,203))
    screen.blit(arrow6,(692,208))
    screen.blit(arrow7,(740,350))
    
    if pygame.time.get_ticks() - last_fps > FPS:
        last_fps = pygame.time.get_ticks()
        draw()
        pygame.display.flip()
        update()
