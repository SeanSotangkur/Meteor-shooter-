import pygame
import random
import string
import datetime
import sys
import time
timetime=0
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont('freesans',32)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
meteor=pygame.image.load('C:\\Users\\seans\\OneDrive\\Documents\\codes\\image.png')
meteor=pygame.transform.scale(meteor,(125,125))
meteor=pygame.transform.rotate(meteor,135)
clicked_meteor=pygame.image.load('C:\\Users\\seans\\OneDrive\\Documents\\codes\\download.png')
clicked_meteor=pygame.transform.scale(clicked_meteor,(125,125))
clicked_meteor=pygame.transform.rotate(clicked_meteor,135)
class Ball():

  def __init__(self,f):
    self.x =0
    self.y=random.randint(0,480)
    self.color=(255,0,0)
    self.radius=20
    self.xmovement=random.uniform(1,4)
    self.ymovement=10
    self.factor=f
    self.visible=1
    self.b=pygame.draw.circle(screen,self.color,(self.x,self.y),1)
  def display_ball(self):
    if self.visible==1:
      self.b=pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
      if self.color==(255,0,0):
        screen.blit(meteor,(self.x-105,self.y-88))
      else:
        screen.blit(clicked_meteor,(self.x-105,self.y-88))
      show_text(str(self.factor),self.x-15,self.y-15,(0,0,0))
  def move_ball(self):
    global lives
    self.x=self.x+self.xmovement
    if self.x>650:
      self.color=(255,0,0)
      print(obj_sel,selected)
      obj_sel.remove(self)
      selected.remove(self.factor)
      lives=lives-1
      self.factor=random.choice(factors)
      self.xmovement=random.randint(3,7)
      self.x=0
if __name__=="__main__":
  name=sys.argv[1]
  start=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(start)
  pygame.init()
  screen=pygame.display.set_mode((640,480))
  pygame.display.set_caption("pygame")
  L=[20,24,28,32,36,40,42,45,48,50,56]
  l2=[36]
  number=random.choice(L)
  factors=[]
  bg=pygame.image.load('C:\\Users\seans\Downloads\\aa-Pygame-Background-Image-Tutorial-Complete-Guide.jpg.webp')
  bg=pygame.transform.scale(bg,(640,480))
  lives=3
  for i in range(1,number+1):# finding factors
    if number%i==0:
      factors.append(i)
  print(factors)
  score=0
  group=[]
  selected=[]
  obj_sel=[]

  for j in range(4):
    if len(factors)%2==0:
      factor1=factors[:len(factors)//2]
      factor2=factors[len(factors)//2:]
      print(factor1)
      print(factor2)
    else:
      factor1=factors[:len(factors)//2+1]
      factor2=factors[len(factors)//2:]
      print(factor1)
      print(factor2)
  factor2=list(reversed(factor2))
  for j in range(4):
    r=random.randint(0,len(factor1)-1)
    ball=Ball(factor1[r])
    print(factor1[r])
    group.append(ball)
    ball=Ball(factor2[r])
    print(factor2[r])
    group.append(ball)
  # for j in range(10):
  #   ball=Ball(random.choice(factors))
  #   group.append(ball)
  T=time.time()
  while True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

      if event.type== pygame.MOUSEBUTTONDOWN:
        if event.button==1:
          for k in group:
            if k.b.collidepoint(event.pos)==True:# check to see if you clicked on a circle
              if k.color==(255,0,0):# select
                if len(selected)<=1:
                  k.color=(0,255,0)

                  selected.append(k.factor)
                  obj_sel.append(k)
                  print(selected)
                if len(selected)==2:
                  if selected[0]*selected[1]==number:
                    obj_sel[0].x=-50
                    obj_sel[1].x=-50
                    obj_sel[0].color=(255,0,0)
                    obj_sel[1].color=(255,0,0)
                    obj_sel[0].y=random.randint(10,480)
                    obj_sel[1].y=random.randint(10,480)
                    r=random.randint(0,len(factor1)-1)
                    obj_sel[0].factor=factor1[r]
                    score=score+100
                    obj_sel[1].factor=factor2[r]
                    selected=[]
                    obj_sel=[]
                  
              elif k.color==(0,255,0):# deselect
                k.color=(255,0,0)
                if k.factor in selected:
                  obj_sel.remove(k)
                  selected.remove(k.factor)
    show_text(str(number),300,0,(0,0,255))
    show_text(str(lives),600,0,(255,0,0))
    for j in group:
      j.display_ball()
      j.move_ball()
    if lives<=0:
      f=open(name,"a")
      f.write("score: ")
      score=str(score)
      f.write(score)
      score=int(score)
      f.write("   ")
      f.write("time: ")
      # start=str(start)
      f.write(start+" ")
      f.write("time played(sec): ")
      f.write(str(int(time.time()-T)))
      f.write("\n")
      f.close()
      print("you lost")
      pygame.quit()
      exit()
    timetime=timetime+1
    if timetime%150==0:
      r=random.randint(0,len(factor1)-1)
      ball=Ball(factor1[r])
      print(factor1[r])
      group.append(ball)
      ball=Ball(factor2[r])
      print(factor2[r])
      group.append(ball)
    pygame.time.delay(30)
    pygame.display.update()