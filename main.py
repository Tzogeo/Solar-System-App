import pygame as pg
from sys import exit
from  random import randint,shuffle
from webbrowser import open as wopen
from math import sin,cos,atan2,atan,sqrt,pi
from datetime import datetime, timedelta
#from missions import *
pg.init()
screen = pg.display.set_mode((720, 720))
pg.display.set_caption("The Solar System")
pg.display.flip()
font=pg.font.Font(None,50)
dot_color = [(255, 255, 255),(255,4,5), (255,255,0)]
dots = []

class Planets():
    planetlist=[]
    def __init__(self,name,g,aktina,color,a,e,speed,minap,angle):
        self.name=name
        self.g=float(g)*9.8
        self.aktina=aktina
        self.color=color
        self.a=float(a)#maximum distance from the center of the ellipse
        self.e=float(e)#eccentri
        self.planetlist.append(self)
        self.speed=speed
        self.minap=minap#minimum distance from the sun
        self.angle=2*pi-angle*pi/180#rotation from x axis
        self.missions=0
    def ellipses(self,sint):#calculates the ellipse of the planet
        self.d=self.minap-self.a
        self.b=self.a*sqrt(1-self.e**2)
        ellipse_surface= pg.Surface((2*sint*self.a,2*self.b*sint),pg.SRCALPHA)
        pg.draw.ellipse(ellipse_surface,self.color,(0,0,2*self.a*sint,2*self.b*sint),width=1)
        self.ellipse= pg.transform.rotate(ellipse_surface, 180*self.angle/pi).convert_alpha()
        self.ellipse_rect = self.ellipse.get_rect(center=(360+self.d*sint*cos(self.angle) , 360+self.d*sint*sin(self.angle)))    
        return self.ellipse, self.ellipse_rect
        
#                         name,       g,      radius,color,a,               e,        speed, minap.   angle
Mercury=Planets("Mercury",0.38,2439.7,"grey",0.387098,0.2056,47.89,0.307499,174.796)
Venus=Planets("Venus",0.9,6051.8,"peru",0.723332,0.006772,35.02,0.718433822,230.115)
Earth=Planets("Earth",1,6371.0, "springgreen",1.0000010181,0.0167086,29.783,0.9832913418,200)
Mars=Planets("Mars",0.37,3389.5,"red",1.52368055,0.0934,24.07,1.381404789,75)
Jupiter=Planets("Jupiter",2.5,69911,"khaki",5.2038,0.0489,13.07,4.9511388871,100)
Saturn=Planets("Saturn",1.06,58232,"gold",9.5826,0.0565,9.68,9.0230135547,182)
Uranus=Planets("Uranus",0.8,25362,"lightblue",19.19126,0.04717,6.8,18.282333942,260)
Neptune=Planets("Neptune",1.14,24662,"turquoise",30.07,0.008678,5.43,29.811607848,130)

def info():#displays information about the planets
    sfont=pg.font.Font(None,34)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range (8):
                        if globals()[f'p{i}_rect'].collidepoint(event.pos):planet_info(i)#shows information about a specific planet when its name is clicked
                        if  globals()[f'p{i}_image_rect'].collidepoint(event.pos):web_searching(i)#opens the wikipedia article of the planet when its image is clicked
        screen.fill("black")
        for i in range (3): pg.draw.line(screen, "white", (0,   (i+1)*180), (720 , (i+1)*180), 2)
        pg.draw.line(screen, "white", (360, 0), (360 , 720), 2)
        for i in range (8):
            globals()[f'p{i}_text']=font.render(Planets.planetlist[i].name, True, (255,255,255))
            globals()[f'p{i}_rect']=globals()[f'p{i}_text'].get_rect(topleft=(360*(i//4)+3,180*(i%4)+3))
            globals()[f'p{i}_image']=pg.image.load(Planets.planetlist[i].name+".png").convert_alpha()
            globals()[f'p{i}_image_rect']=globals()[f'p{i}_image'].get_rect(topleft=(360*(i//4)+3,180*(i%4)+40))
            globals()[f'p{i}_text2']=sfont.render("g="+str("{:.3f}".format(Planets.planetlist[i].g))+"m/(s^2)", True, (255,255,255))
            globals()[f'p{i}_text3']=sfont.render("r="+str(Planets.planetlist[i].aktina)+"km", True, (255,255,255))
            globals()[f'p{i}_rect2']=globals()[f'p{i}_text2'].get_rect(topleft=(360*(i//4)+133,180*(i%4)+83))
            globals()[f'p{i}_rect3']=globals()[f'p{i}_text2'].get_rect(topleft=(360*(i//4)+133,180*(i%4)+83+font.get_height()))
            screen.blit(globals()[f'p{i}_text'],globals()[f'p{i}_rect'])
            screen.blit(globals()[f'p{i}_image'],globals()[f'p{i}_image_rect']) 
            screen.blit(globals()[f'p{i}_text2'],globals()[f'p{i}_rect2'])
            screen.blit(globals()[f'p{i}_text3'],globals()[f'p{i}_rect3'])

        pg.display.update()
def planet_info(number):#displays info about a specific planet that its being clicked
    sfont=pg.font.Font(None,34)
    i=0
    screen.fill("black")
    with open(Planets.planetlist[number].name+".txt", 'r') as file:
        lines=file.readlines()
        for line in lines:
            globals()[f'p{i}_text']=font.render(line[:-1], True, (255,255,255))
            globals()[f'p{i}_rect']=globals()[f'p{i}_text'].get_rect(topleft=(40,40+i*(sfont.get_height()+4)))
            screen.blit(globals()[f'p{i}_text'],globals()[f'p{i}_rect'])
            i+=1
    file.close()
    Planet=pg.image.load(Planets.planetlist[number].name+".png").convert_alpha()
    Planetrect=Planet.get_rect(topleft=(600,100))
    screen.blit(Planet,Planetrect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                       if  Planetrect.collidepoint(event.pos):web_searching(number)#opens the wikipedia article of the planet when its image is clicked
        pg.display.update()                                                                          

def web_searching(number):#opens the wikipedia article of the planet when its image is clicked
    if number!=0:wopen("https://en.wikipedia.org/wiki/"+Planets.planetlist[number].name)
    else:wopen("https://en.wikipedia.org/wiki/"+Planets.planetlist[number].name+"_Planet")
    return 0

def free_fall():#simulates a free fall of the same distance in each planet
    clock=pg.time.Clock()
    y=[40 for i in range (8)]
    t=0
    movement=0
    sfont=pg.font.Font(None,34)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0
                if event.key ==pg.K_SPACE:
                    movement=(movement+1)%2
                if event.key==pg.K_r:
                    t=0
        screen.fill((0,0,0))
        for i in range(0,8,1):
            y[i]=Planets.planetlist[i].g*t*t/2
            pg.draw.line(screen, "white", (90*i, 0), (90*i , 720), 2)
            globals()[f'pb{i}_image']=pg.image.load("L"+Planets.planetlist[i].name+".png").convert_alpha()
            globals()[f'pb{i}_image_rect']=globals()[f'pb{i}_image'].get_rect(topleft=(90*i,0))
            globals()[f'p{i}_image']=pg.image.load("rocket.png").convert_alpha()
            globals()[f'p{i}_image_rect']=globals()[f'p{i}_image'].get_rect(topleft=(90*i+20,y[i]))
            screen.blit(globals()[f'pb{i}_image'],globals()[f'pb{i}_image_rect']) 
            screen.blit(globals()[f'p{i}_image'],globals()[f'p{i}_image_rect']) 
            
        pg.display.update()
        if movement==1:t=t+0.2
        clock.tick(20)

def planet_movement(n,t=0):#shows the movement of the planets in scale
    xxsfont=pg.font.Font(None,16)
    clock = pg.time.Clock()
    movement=0
    al=0
    epistrofi=0
    ft=[0,0,0,0,0,0,0,0]
    arx=[140,85,175,2,-130,-75,-145,-90]
    xt=[]
    yt=[]
    ry=[0 for i in range (8)]
    rx=[0 for i in range (8)]
    rry=[0 for i in range (8)]
    rrx=[0 for i in range (8)]
    for item in ry:xt.append(item)
    for item in rx:yt.append(item)
    if n==4:sint=160
    else:sint=10    
    colors=["grey","peru","springgreen","red","khaki","gold","lightblue","turquoise"]
    for i in range (n):#draws the elipses
        globals()[f'p{i}_ellipse'],globals()[f'p{i}_ellipse_rect']=Planets.planetlist[i].ellipses(sint)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 1
                if event.key ==pg.K_SPACE:#starts or pauses the movment
                    movement=(movement+1)%2
                if event.key==pg.K_r:#returns to the initial day
                    t= initial_day()
                if event.key==pg.K_n:#asks the user for a day
                    new_date=input("input the date you want in dd/mm/yyyy format")
                    t=starting_date(new_date)
            if event.type==pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if n==8 and globals()[f'p{4}_ellipse_rect'].collidepoint(event.pos): epistrofi=planet_movement(4,t)
        screen.fill("black")
        if epistrofi==1:
            for i in range (4): globals()[f'p{i}_ellipse'],globals()[f'p{i}_ellipse_rect']=Planets.planetlist[i].ellipses(10)
            epistrofi=0
        for i in range (n):
            a=Planets.planetlist[i].a
            ec=Planets.planetlist[i].e
            d=Planets.planetlist[i].minap-a
            b=a*sqrt(1-ec**2)
            th=Planets.planetlist[i].angle
            u=Planets.planetlist[i].speed
            screen.blit(globals()[f'p{i}_ellipse'],globals()[f'p{i}_ellipse_rect'])
            ft[i] = atan2(2* b* sin(-u/ b * t), 2*a * cos(-u / b * t))#calculates new position
            xt[i] =a * cos(ft[i]-th+pi*arx[i]/180)#on the x axis
            yt[i] =b * sin(ft[i]-th+pi*arx[i]/180)#on the y axis
            if n==4:#draws the sun in the inner planets simulation
                pg.draw.circle(screen,"yellow",(360,360),5)
            rx[i],ry[i]=(sint*(xt[i]+d)),+sint*yt[i]
            rrx[i]=360+rx[i]*cos(th)-ry[i]*sin(th)
            rry[i]=360+ry[i]*cos(th)+rx[i]*sin(th)
            pg.draw.circle(screen,colors[i],(rrx[i],rry[i]),5)
            globals()[f'p{i}_ptext']=xxsfont.render(Planets.planetlist[i].name,True, colors[i])
            globals()[f'p{i}_ptext_rect']=globals()[f'p{i}_ptext'].get_rect(topleft=(rrx[i]-20,rry[i]-30))
            screen.blit(globals()[f'p{i}_ptext'],globals()[f'p{i}_ptext_rect'])
        #pg.draw.rectangle(screen,colors[4],
        smfont=pg.font.Font(None, 37)
        ddate=str(date_calculator(t))
        maintext=smfont.render(ddate , True, (255,255,255))
        maintextrect=maintext.get_rect(topleft=(10,30))
        screen.blit(maintext,maintextrect)
        if movement==1:
            if n==4:t=t-0.019
            t=t+0.02#changes time
        clock.tick(10)
        pg.display.flip()

def quiz(difficulty=None):
    sfont=pg.font.Font(None,24)
    quizlist=[]
    score=0
    onoma_arxeiou='questions.txt'
    if difficulty=="hard":
        onoma_arxeiou='dquestions.txt'
        boos=0
    ##if os.path.exists(onoma_arxeiou):print("tobriskei")
    with open(onoma_arxeiou, 'r') as file:
        lines=file.readlines()
        for line in lines:quizlist.append((line[0:-2],line[-2]))
        shuffle(quizlist)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return 0
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range (8):
                        if  globals()[f'p{i}_image_rect'].collidepoint(event.pos):
                            if i==int(quizlist[0][1])-1:
                                print("congrats")
                                score=score+1
                            else:
                                print("booo")
                                if difficulty=="hard":
                                    boos=boos+1
                                    if boos==3:
                                        print("BOOOOOOOOOO!!!!Exases")
                                        return 0
                            quizlist=quizlist[1:]
        screen.fill("black")
        try:quiztext=sfont.render(quizlist[0][0]+"       "+str(score), True, (255,255,255))
        except: return score
        quizrect=quiztext.get_rect(topleft=(40,40))
        for i in range (8):
            globals()[f'p{i}_image']=pg.image.load(Planets.planetlist[i].name+".png").convert_alpha()
            globals()[f'p{i}_image_rect']=globals()[f'p{i}_image'].get_rect(topleft=(360*(i//4)+3,180*(i%4)+80))
            screen.blit(globals()[f'p{i}_image'],globals()[f'p{i}_image_rect'])
        screen.blit(quiztext,quizrect)
        pg.display.update() 

                            
def date_calculator(t):#returns the date in a given time in the simulation
    current_date=int(t*149597871/86400)
    start_date = '01/01/2024'
    start_datetime = datetime.strptime(start_date, '%d/%m/%Y')
    result_datetime = start_datetime + timedelta(days=current_date)
    return result_datetime.strftime('%d/%m/%Y')

def initial_day():#finds the t equivalent of the current date
    start_date = '01/01/2024'
    today_date = datetime.today()
    diff=date_difference_to_virtual_days(today_date,start_date,1)
    return(diff*86400/149597871)

def starting_date(newdate):#finds the t equibalent of a date given by user
    start_date='01/01/2024'
    diff=date_difference_to_virtual_days(newdate,start_date,0)
    return(diff*86400/149597871)

def date_difference_to_virtual_days(end_date, start_date,today):
    start_datetime = datetime.strptime(start_date, '%d/%m/%Y')
    if today==1:end_datetime=end_date
    else:end_datetime = datetime.strptime(end_date, '%d/%m/%Y')
    delta = end_datetime - start_datetime
    return delta.days
    
for _ in range(100):  # makes 100 random points(starts)
    x = randint(0, 720)
    y = randint(0, 720)
    dots.append((x, y))
    max_score=0
    last_score=0
    
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key == pg.K_1:info()
            if event.key == pg.K_2:free_fall()
            if event.key==pg.K_3:planet_movement(8,initial_day())
            if event.key==pg.K_4:planet_movement(4,initial_day())
            if event.key==pg.K_5:last_score=quiz()
            if event.key==pg.K_6:quiz("hard")
    screen.fill((0,0,0))
    if last_score>max_score:max_score=last_score
    smfont=pg.font.Font(None, 37)
    textlist=["Press 1 for information about the Planets,","2 to watch a free fall simulation on different Planets,","3 to watch the orbits of the Planets in scale" ,"4 to watch the orbits of the inner Planets" ,"5 to take a quiz. Max score="+str(max_score),"6 to take a quiz with 'hard' difficulty"]
    for i in range (1,6,1):
        globals()[f"maintext{i}"]=smfont.render(textlist[i-1] , True, (255,255,255))   
        globals()[f"maintextrect{i}"]=globals()[f"maintext{i}"].get_rect(topleft=(10,30+(i-1)*font.get_height()))
        screen.blit(globals()[f"maintext{i}"],globals()[f"maintextrect{i}"])

    for dot in dots:
        pg.draw.circle(screen, dot_color[randint(0,2)], dot, 2)

    pg.display.flip()
      
