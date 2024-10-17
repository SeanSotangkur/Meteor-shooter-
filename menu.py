import pygame
import random
import string
import os
import datetime
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont('freesans',32)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
name=""
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("pygame")
meteor=pygame.image.load('C:\\Users\\seans\\OneDrive\\Documents\\codes\\image.png')
meteor=pygame.transform.scale(meteor,(125,125))
meteor=pygame.transform.rotate(meteor,135)
while True:
  screen.blit(meteor,(0,100))
  show_text("player_name:",0,0,(0,0,255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button==1:
        if play.collidepoint((event.pos)):
          exists= os.path.isfile(name+str(".txt"))
          if not exists:
            f=open(name+".txt","w")
            f.close()
          os.system("C://Users/seans/AppData/Local/Programs/Python/Python311/python.exe c:/Users/seans/OneDrive/Documents/codes/project_game.py "+name+".txt")
          pygame.quit()
          exit()
    if event.type== pygame.KEYDOWN:
      if event.key==pygame.K_BACKSPACE:
        screen.fill((0,0,0))
        name=name[:-1]
        show_text(name,200,0,(255,0,0))
      else:
        print(chr(event.key))
        name=name+chr(event.key)
        show_text(name,200,0,(255,0,0))
  play=pygame.draw.rect(screen,(0,255,0),(220,140,200,100))
  show_text('play',220,140,(0,0,0),)
  pygame.time.delay(30)
  pygame.display.update()