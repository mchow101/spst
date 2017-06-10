__author__ = 'Bhagat'
import pygame
import os
import time
import speech
from pygame.locals import *
from Compare import compare
from Linear_Regression import line
from Input_Data import input_data
from library import create_dataset
pygame.init()
width=800
height=600
display = pygame.display.set_mode((width,height),RESIZABLE)
def button(x,y,lengthX,lengthY,text,rect,textX,textY,textSize=4.0,color=(0,0,0)):
    pos = pygame.mouse.get_pos()
    picture=None
    if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y:
        if type(rect)==tuple:
            if rect[0]<246:
                rect1=rect[0]+50
            else:
                rect1=rect[0]-50
            if rect[1]<246:
                rect2=rect[1]+50
            else:
                rect2=rect[1]-50
            if rect[2]<246:
                rect3=rect[2]+50
            else:
                rect3=rect[2]-50
            rect=(rect1,rect2,rect3)
    if type(rect)==str:
        picture=pygame.image.load(rect)
        picture = pygame.transform.scale(picture,(lengthX,lengthY))
        if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y:
            if type(rect)==str:
                dark = pygame.Surface((picture.get_width(), picture.get_height()), flags=pygame.SRCALPHA)
                dark.fill((30, 30, 30, 0))
                picture.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        display.blit(picture, (x,y))
    else:
        rectangle=pygame.Rect(x,y,lengthX,lengthY)
        pygame.draw.rect(display, rect, rectangle)
    messageOnScreen(text,textX,textY, color ,textSize)
    if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y and (pygame.mouse.get_pressed()[2]==1 or pygame.mouse.get_pressed()[0] == 1):
        return True
    else:
        return False
def messageOnScreen(msg,x,y,color,size=4.0):
    font =  pygame.font.SysFont(None,int(size*10))
    text =  font.render(msg,True,color)
    display.blit(text,[x,y])
def screen_type(x,y,color=(0,0,0),size=4,string='none',but=False,msg=''):
    enter = False
    s=msg+''
    caps=False
    keys = [273,276,275,274,9,301,304,301,27,306,311,308,286,0,311,316]
    while enter == False:
        display.fill((255,255,255))
        if but:
            if button(width/2-100,height/2-70,200,50,"Best-Fit-Graph",(0,255,0),width/2-100, height/2-55):
                graph_section()
            if button(width/2-100,height/2-10,200,50,'Compare Diseases',(0,255,0),width/2-90,height/2+5,textSize=3.0):
                compare_stuff()
            if button(width/2-100,height/2+50,200,50,"Input Data",(0,255,0),width/2-80, height/2+65):
                input_data()
            if button(width/2-100,height/2+230,200,50,"Delete Data",(255,0,0),width/2-80, height/2+245):
                try:
                    os.remove(name+'xs.txt')
                    os.remove(name+'ys.txt')
                except WindowsError:
                    pass
            if button(width/2-100,height/2+110,200,50,"How is the future?",(255,0,0),width/2-80, height/2+125,textSize=3.0):
                future()
            if button(width/2-100,height/2+170,200,50,"Predict",(255,0,0),width/2-80, height/2+185):
                predict()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 304:
                     caps = True
                if event.key == 8:
                    temp=""
                    for weu in range(len(s)-1):
                        temp+=s[weu]
                    s=temp
                elif event.key == 13:
                    enter=True
                else:
                    if string=='none':
                        if event.key not in keys:
                            if caps:
                                s+=chr(event.key-32)
                            else:
                                s+=chr(event.key)
                    elif string == 'num':
                        if event.key>=48 and event.key<=57:
                            s+=chr(event.key)
            elif event.type == 3:
                 if event.key == 304:
                     caps = False
        messageOnScreen(s,x,y,color,size)
        pygame.display.update()
    return s
def graph_section(graphq=True):
    display.fill((0,0,0))
    global year
    global graph
    file = open('D:\MyPrograms\spst-master\spst-master\\text.txt','r')
    name = file.read()
    file.close()
    try:
        xsss = open('D:\MyPrograms\spst-master\spst-master\\'+name+'xs.txt','r')
        xss=xsss.read()
        if xss=='[]' or xss=='':
            raise IOError
    except IOError:
        messageOnScreen('There is no data for this disease please input some',40/80*width,height/2-height*15/600,(255,0,0),4.5)
        pygame.display.update()
        time.sleep(3)
        return None
    xs=[]
    ysss = open('D:\MyPrograms\spst-master\spst-master\\'+name+'ys.txt','r')
    yss = ysss.read()
    ys=[]
    start = 0
    end = -1
    for x in range(len(xss)):
        if xss[x]==',' or xss[x]==']':
            end = x
            xs.append(int(xss[start+1:end]))
            start = end
    start = 0
    end = -1
    for y in range(len(yss)):
        if yss[y]==',' or yss[y]==']':
            end = y
            ys.append(int(yss[start+1:end]))
            start = end
    xsss.close()
    ysss.close()
    xs = [int(x) for x in xs]
    ys = [int(y) for y in ys]
    if not len(ys) == len(xs):
        messageOnScreen('There is no valid data for this disease',1/2*width,height/2-height*15/600,(255,0,0),4.5)
        pygame.display.update()
        time.sleep(3)
        return None
    graph = line(xs,ys,year)
    if graphq:
        graph.graph()
def input_name():
    global name
    speech.say("Say the name")
    name = speech.input('')
    speech.stoplistening()
    file = open('D:\MyPrograms\spst-master\spst-master\\text.txt','w')
    file.write(name)
    file.close()
def predict():
    display.fill((255,255,255))
    global year
    global graph
    pygame.display.update()
    year = float(screen_type(10,10,string='num',msg = 'Year: ')[6:])
    graph_section(False)
    display.fill((255,255,255))
    messageOnScreen(str(int(graph.predict(year))),10,10,(0,0,0))
    pygame.display.update()
    time.sleep(3)
def compare_stuff():
    lines = []
    colors = []
    names=[]
    print 'Put Quit as the disease to stop'
    while True:
        namee = raw_input("Enter in the disease: ")
        if namee=='Quit':
            break
        names.append(namee)
        lines.append(object_creater(names[len(names)-1]))
        colors.append(raw_input('Enter in the color of this line: '))
    compare(lines,colors)
def object_creater(name):
    try:
        xsss = open('D:\MyPrograms\spst-master\spst-master\\'+name+'xs.txt','r')
        xss=xsss.read()
        if xss=='[]' or xss=='':
            raise IOError
    except IOError:
        messageOnScreen('There is no data for this disease please input some',40/80*width,height/2-height*15/600,(255,0,0),4.5)
        pygame.display.update()
        time.sleep(3)
        return None
    xs = []
    ysss = open('D:\MyPrograms\spst-master\spst-master\\'+name+'ys.txt','r')
    yss = ysss.read()
    ys=[]
    start = 0
    end = -1
    for x in range(len(xss)):
        if xss[x]==',' or xss[x]==']':
            end = x
            xs.append(int(xss[start+1:end]))
            start = end
    start = 0
    end = -1
    for y in range(len(yss)):
        if yss[y]==',' or yss[y]==']':
            end = y
            ys.append(int(yss[start+1:end]))
            start = end
    xsss.close()
    ysss.close()
    xs = [int(x) for x in xs]
    ys = [int(y) for y in ys]
    if not len(ys) == len(xs):
        messageOnScreen('There is no valid data for this disease',1/2*width,height/2-height*15/600,(255,0,0),4.5)
        pygame.display.update()
        time.sleep(3)
        return None
    graph = line(xs,ys)
    return graph
def future():
    global graph
    running = True
    running2 = True
    while running or running2:
        display.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                pygame.quit()
            if event.type == 5:
                running = False
            if event.type == 6:
                running2 = False
        m=graph.get_m()
        r_squared = graph.get_r_squared()
        if m>10:
            messageOnScreen(name+' is getting worse. It is affecting more people as time is going on.',10,10,(0,0,0),3)
        elif m<-10:
            messageOnScreen(name+' is getting better. Less people are getting affected by it as time goes on.',10,10,(0,0,0),3)
        else:
            messageOnScreen(name+' is not really getting better or worse, it is staying about the same',10,10,(0,0,0),3)
        messageOnScreen('This data is '+str(r_squared*100)+' percent accurate',30,70,(0,0,0),size=2.7)
        pygame.display.update()
        if not running2 and running:
            running2=False
def music(s):
    pygame.mixer.music.load(s)
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(1)
music('D:\\MyPrograms\\spst-master\\spst-master\\Nature_Sounds.mp3')
paused=False
nameFile = open('D:\\MyPrograms\\spst-master\\spst-master\\text.txt','r')
xs,ys = create_dataset(40,20,2,True)
graph = line(xs,ys)
name = nameFile.read()
nameFile.close()
#icon = pygame.image.load("D:\\MyPrograms\\spst-master\\spst-master\\Earth.jpg")
pygame.display.set_caption("D:\\MyPrograms\\spst-master\\spst-master\\Disease Data Analysis")
#pygame.display.set_icon(icon)
year=0.0

while True:
    display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == 12:
            quit()
            pygame.quit()
        if event.type==16:
            surface = pygame.display.set_mode((event.w,event.h),RESIZABLE)
            height = display.get_height()
            width = display.get_width()
        if event.type==2:
            if event.key == 27:
                quit()
                pygame.quit()
    if button(width/2-150,height/2-125,3000,50,name,(255,255,255),width/2-130,height/2-110,color=(0,0,255)):
        name = screen_type(width/2-130,height/2-110,but=True)
        file = open('D:\\MyPrograms\\spst-master\\spst-master\\text.txt' , 'w')
        file.write(name)
        file.close()
    if button(width/2-200,height/2-125,50,50,'',(0,0,255),0,0):
        input_name()
    if button(width/2-200,height/2 - 60,50,50,'||',(0,0,255),width/2-180,height/2-45):
        if paused:
            paused=False
            pygame.mixer.music.unpause()
        else:
            paused=True
            pygame.mixer.music.pause()
    #mic = pygame.image.load('D:\\MyPrograms\\spst-master\\spst-master\\mic.png')
    #mic = pygame.transform.scale(mic, (50,50))
    #display.blit(mic,(width/2-200,height/2-125))
    if button(width/2-100,height/2-70,200,50,"Best-Fit-Graph",(0,255,0),width/2-100, height/2-55):
        graph_section()
    if button(width/2-100,height/2-10,200,50,'Compare Diseases',(0,255,0),width/2-90,height/2+5,textSize=3.0):
        compare_stuff()
    if button(width/2-100,height/2+50,200,50,"Input Data",(0,255,0),width/2-80, height/2+65):
        input_data()
    if button(width/2-100,height/2+230,200,50,"Delete Data",(255,0,0),width/2-80, height/2+245):
        try:
            os.remove('D:\\MyPrograms\\spst-master\\spst-master\\'+name+'xs.txt')
            os.remove('D:\\MyPrograms\\spst-master\\spst-master\\'+name+'ys.txt')
        except WindowsError:
            pass
    if button(width/2-100,height/2+110,200,50,"How is the future?",(255,0,0),width/2-80, height/2+125,textSize=3.0):
        future()
    if button(width/2-100,height/2+170,200,50,"Predict",(255,0,0),width/2-80, height/2+185):
        predict()
    pygame.display.update()
