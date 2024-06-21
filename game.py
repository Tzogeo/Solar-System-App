import pygame as pg
from sys import exit
from  random import randint,shuffle
from time import sleep

def dot_places():#makes 120 dots to represent stars
    dots=[]
    for _ in range(120):  
        x = randint(0, 720)
        y = randint(0, 720)
        dots.append((x, y))
    return dots
    
class Levels():
    Levellist=[]#contains all the levels
    def __init__(self,number,question,speed,answers,planets=2,special_level=None):
        self.number=number
        self.question=question
        self.answers=answers
        self.speed=speed
        self.errors=0
        self.correct=0
        self.planets=planets
        self.special_level=special_level
        Levels.Levellist.append(self)
    def mouse_touched(self,planet):
        if planet in self.answers:
            if self.special_level is not None: self.check_special(planet)
            self.correct+=1
        else: self.errors+=1
        return self.check_result()
    def surface_touched(self,planet):
        if planet in self.answers:self.errors+=1
        return self.check_result()
    def check_result(self):
        if self.errors==3:
            print("try again")
            self.level_restart()
            return -1
        if self.correct==self.number:
            print("next level")
            return 1
        return 0
    def level_restart(self):
        self.errors=0
        self.correct=0
        if self.special_level=='OneTime' or self.special_level=='InOrder' : self.answers=[0,1,2,3,4,5,6,7]
    def check_special(self,planet):
        if self.special_level=='InOrder':
            self.answers[0]+=1
        if self.special_level =='OneTime':
            self.answers.remove(planet)
class Planets():
    Planetlist=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    def __init__(self,number,yposition=0):
        self.number=number
        self.xposition=randint(1,630)
        self.yposition=yposition
        self.image=pg.image.load(Planets.Planetlist[self.number]+'.png')

def game():
    pg.init()
    screen = pg.display.set_mode((720, 720))
    pg.display.set_caption("The Solar System Game")
    pg.display.flip()
    font=pg.font.Font(None,50)
    dot_color = [(255, 255, 255),(255,4,5), (255,255,0)]
    dots = []
    dots=dot_places()
    Level0=Levels(3,"Earth",15,[2],3)
    Level1=Levels(10,"Gas Giants",15,[4,5,6,7])
    Level2=Levels(10,"Look at the stars",20,[3],planets=3,special_level="red")
    Level3=Levels(10,"Planets who haven't won Miss Universe",20,[0,1,3,4,5,6,7])
    Level4=Levels(10,"Planets with more that one moon",25,[3,4,5,6,7],special_level="don'ttouchit")
    Level5=Levels(15,"Earth and Neptune",30,[2,7])
    Level6=Levels(8,"All in order from closest to farthest to the Sun",35,[0],special_level="InOrder")
    Level7=Levels(15,"Planets with mount Olympus",31,[2,3],3)
    Level8=Levels(10,"Take off into SPACE",45,[],planets=5,special_level="Space")
    Level9=Levels(10,"So many stars. Not a single moon",25,[0,1],4)
    Level10=Levels(15,"Members of SUN",35,[5,6,7])
    Level11=Levels(10,"Mercury the fast god",35,[0],special_level="fast god")
    Level12=Levels(10,"The closest and the farthest from the Sun", 35,[0,7],3)
    Level13=Levels(10,"All of them",35,[0,1,2,3,4,5,6,7])
    Level14=Levels(8,"All but each only one time",26,[0,1,2,3,4,5,6,7],special_level="OneTime")
    Level15=Levels(10,"[...]nus",40,[1,6],3)
    Level16=Levels(10,"Earth",45,[2],4)
    Level17=Levels(15,"All except Venus",40,[0,2,3,4,5,6,7])

    Venus1=Planets(1)
    Saturn1=Planets(5,-360)
    plannum=2
    InGamePlanets=[Venus1,Saturn1]
    cln=0
    clock=pg.time.Clock()
    smfont=pg.font.Font(None, 37)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button ==1:
                    for planet in InGamePlanets:
                        if globals()[f'{planet}rect'].collidepoint(event.pos):
                            currentLevel.mouse_touched(planet.number)
                            InGamePlanets.remove(planet)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if currentLevel.special_level=="Space":
                        currentLevel.level_restart
                        dots=dot_places()
                        dots.extend(dot_places())
                        dots.extend(dot_places())
                        dots.extend(dot_places())
                        cln+=1
                        continue
                    #else:cln=int(input("pick a level")) for going to specific levels
                if event.key == pg.K_ESCAPE:
                    return 0
        try:currentLevel=Levels.Levellist[cln]
        except:
            pg.quit()
            print("you won!!!!")
            exit()
        if currentLevel.correct==currentLevel.number:
            dots=dot_places()
            cln+=1
            continue
        screen.fill((0,0,0))
        for dot in dots:
            if currentLevel.special_level=="red":pg.draw.circle(screen, (255,0,0), dot, 2)
            else:pg.draw.circle(screen, dot_color[randint(0,2)], dot, 2)

        
        maintext=smfont.render(currentLevel.question , True, (255,255,255))
        maintextrect=maintext.get_rect(topleft=(10,30))
        score=smfont.render("score:"+str(currentLevel.correct)+"/"+str(currentLevel.number) , True, (255,255,255))
        errors=smfont.render("mistakes:"+str(currentLevel.errors) , True, (255,255,255))
        scorerect=score.get_rect(topright=(710,30))
        errorrect=errors.get_rect(topright=(710,50))
        screen.blit(maintext,maintextrect)
        screen.blit(score,scorerect)
        screen.blit(errors,errorrect)
        if len(InGamePlanets)<currentLevel.planets:
            globals()['f Planet{plannum+1}']=Planets(randint(0,7))
            InGamePlanets.append(globals()['f Planet{plannum+1}'])
            plannum+=1
        for planet in InGamePlanets:
            globals()[f'{planet}rect']=planet.image.get_rect(topleft=(planet.xposition,planet.yposition))
            planet.yposition+=10
            if planet.number==0 and currentLevel.special_level=="fast god": planet.yposition+=5
            screen.blit(planet.image,globals()[f'{planet}rect'])
            if currentLevel.special_level=="don'ttouchit" and planet.number not in currentLevel.answers:
                planettext=smfont.render("don't touch it", True, (255,0,0))
                planettextrect=planettext.get_rect(topleft=(planet.xposition-30,planet.yposition))
                screen.blit(planettext,planettextrect)
            if planet.yposition==720:
                currentLevel.surface_touched(planet.number)
                InGamePlanets.remove(planet)
        clock.tick(currentLevel.speed)
        pg.display.flip()
        
