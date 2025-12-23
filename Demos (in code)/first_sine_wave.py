# title:   sine wave
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
import math
t=0

def yPos(o,p=0,r=5,s=7,n=False):
 if n:
  return o-int((math.sin((t+p)/r))*s)
 else:
  return o+int((math.sin((t+p)/r))*s)
 
def makeMessage(msg,x,y,r,s,c=False,n=False):
 x_s=x
 for i,l in enumerate(msg):
  c_s=(i+(t//5%16))if c else 3
  print(l,x_s,yPos(y,i+2,r,s,n),c_s,True)
  if i == 0:
   x_s+=5
  else:
   x_s+=6
def makeSineWave():
 x=0
 y=yPos(68,0,15,15)
 for i in range(240):
  pix(x,y,6)
  x+=1
  y=yPos(68,i,15,15)
def BOOT():
 pass
def TIC():
 global t
 cls()
 makeMessage("sine wave!",91,30,5,3.5,True,False)
 makeSineWave()
 makeMessage("isn't that cool?",71,106,5,3.5,False,True)
 t+=1
