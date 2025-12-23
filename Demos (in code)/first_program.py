# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python

c=2
t=60
w=None
def BOOT():
 global w
 w=print("hello!",0,-6)
def yPos(o=0):
 return (t+o)%148-10
def TIC():
 global t,c
 cls(7)
 rect(0,53,240,30,c)
 print("hello!",120-(w//2),yPos(-10),2)
 print("hello!",120-(w//2),yPos(0),6)
 print("hello!",120-(w//2),yPos(10),12)
 if not t%30:
  c=2
 if not t%60:
  c=6
 if not t%90:
  c=12
 t+=1