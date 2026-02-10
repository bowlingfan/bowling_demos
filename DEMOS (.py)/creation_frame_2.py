# title:   happy birthday gift
# author:  g scape
# desc:    happy birthday demo for friend, no music.
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
import random
import math

#offsetted by 2.5 seconds
class Scene1():
 def __init__(self):
  self.end_t=10.5*sec_t
class Scene2():
 def __init__(self):
  self.end_t=18.5*sec_t
  self.arrow=Arrow()
class Scene3():
 def __init__(self):
  self.end_t=26.5*sec_t
class Scene4():
 def __init__(self):
  self.end_t=42.5*sec_t
class BranchDrawer():
 def __init__(self,sx=-1,sy=-1,minox=-15,maxox=15,minoy=-30,maxoy=-5,mint=30,maxt=70):
  self.t=0
  self.points=[] # (x, y, next_pos_tick)
  self.create_branches(sx,sy,minox,maxox,minoy,maxoy,mint,maxt)
 def create_branches(self,sx,sy,minox,maxox,minoy,maxoy,mint,maxt):
  sx=sx if sx != -1 else random.randint(0,window_w)
  sy=sy if sy != -1 else window_h+1
  self.points.append((sx,sy,0))
  for amt in range(random.randint(2,10)):
   last=self.points[len(self.points)-1]
   self.points.append((last[0]+random.randint(minox,maxox),last[1]+random.randint(minoy,maxoy),last[2]+random.randint(mint,maxt)))
 def draw_branches(self):
  for bindex in range(len(self.points)-1):
   pa=self.points[bindex]
   pb=self.points[bindex+1]
   end_time=pb[2]-pa[2]
   for t in range(end_time-(pb[2]-self.t)-1):
    pos=self.l_draw(pa, pb, t, end_time)
    pix(int(pos[0]),int(pos[1]),1)
 def l_draw(self, pa, pb, t, e_t):
  m=(pb[1]-pa[1])/(pb[0]-pa[0])
  x=pa[0]+(t/e_t)*(pb[0]-pa[0])
  return (x,m*(x-pa[0])+pa[1])
class Arrow():
 def __init__(self):
  self.t=0
  self.w=10
 def draw(self):
  for o in range(1,self.w+1):
   line(window_w//2,window_h+o-self.t,0,window_h+o+30-self.t,4)
   line(window_w//2,window_h+o-self.t,window_w,window_h+o+30-self.t,4)
class StraightLineDrawer():
 def __init__(self):
  self.t=0
  self.radius=0
  self.color=random.randint(4,5)
  self.pos=[]  # (x, y, next_pos_tick)
  self.init_pos()

 def draw(self):
  for pindex in range(len(self.pos)-1):
   pa=self.pos[pindex]
   pb=self.pos[pindex+1]
   end_time=pb[2]-pa[2]
   for t in range(end_time-(pb[2]-self.t)+1):
    pix(pa[0]+int(((pb[0]-pa[0])/end_time)*t),pa[1]+int(((pb[1]-pa[1])/end_time)*t),self.color)

 def init_pos(self):
  xory=random.randint(0,1)
  r=random.randint(0,1)
  if xory==0:
   self.sx=random.randint(-self.radius,window_w)
   self.sy=r*(window_h)+self.radius if r==1 else r*(window_h)-self.radius
  else:
   self.sx=r*(window_w)+self.radius if r==1 else r*(window_w)-self.radius
   self.sy=random.randint(-self.radius,window_h)
  self.pos.append((self.sx,self.sy,0))
  rx,ry,d=self.new_rand_pos((self.sx,self.sy))
  self.pos.append((rx,ry,random.randint(70,120)))

  for p in range(5):
   last=self.pos[len(self.pos)-1]
   rx,ry,d=self.new_rand_pos((last[0],last[1]),d)
   self.pos.append((rx,ry,last[2]+random.randint(70,120)))
   if self.is_out_of_bounds((rx,ry)):
    break
   elif p==5:
    close=self.closest_exit((rx,ry))
    if close[0]=="x":
     if rx+close[1]>=window_w+self.radius:
      self.pos.append(rx+close[1],ry,last[2]+random.randint(70,120))
     else:
      self.pos.append(rx-close[1],ry,last[2]+random.randint(70,120))
    elif close[0]=="y":
     if ry+close[1]>window_h+self.radius:
      self.pos.append(rx,ry+close[1],last[2]+random.randint(70,120))
     else:
      self.pos.append(rx,ry-close[1],last[2]+random.randint(70,120))
 def alternate_direction(self, d):
  return "y" if d=="x" else "x" 
 
 def new_rand_pos(self, pos, d=""):
  # im sorry
  xory=random.randint(0,1)
  rx,ry=0,0
  if d=="x":
   rx=pos[0]+random.randint(25,100) if pos[0]<=40 else pos[0]-random.randint(25,100)
   ry=pos[1]
   d="x"
  elif d=="y":
   rx=pos[0]
   ry=pos[1]+random.randint(25,100) if pos[1]<=40 else pos[1]-random.randint(25,100)
   d="y"
  elif xory==0:
   rx=pos[0]+random.randint(25,100) if pos[0]<=40 else pos[0]-random.randint(25,100)
   ry=pos[1]
   d="x"
  else:
   rx=pos[0]
   ry=pos[1]+random.randint(25,100) if pos[1]<=40 else pos[1]-random.randint(25,100)
   d="y"
  return (rx,ry,self.alternate_direction(d))
 
 def is_out_of_bounds(self,pos):
  return pos[0] > window_w+self.radius or pos[0] < -self.radius or pos[1] < -self.radius or pos[1] > window_h+self.radius
 
 def closest_exit(self, pos):
  x=min(abs(pos[0]-(window_w+self.radius)),abs(pos[0]-self.radius))
  y=min(abs(pos[1]-self.radius),abs(pos[1]-(window_h+self.radius)))
  return ("x",x) if x<y else ("y",y)
class CircleOut():
 def __init__(self):
  self.sx=random.randint(0,window_w)
  self.sy=random.randint(0,window_h)
  self.t=5
 def draw(self):
  circb(self.sx,self.sy,self.t,6)
class ImproperGrid:
 def __init__(self):
  self.grid_size=20
  self.max_size=4
  self.cell_pix_size=45
  self.camera_x=self.cell_pix_size*self.grid_size
  self.camera_y=self.cell_pix_size*self.grid_size
  self.grid=[]
  self.colors=[1,7,8,9]
  self.spacing=2

  self.init_grid()
  self.fill_grid()

 def init_grid(self):
  for _ in range(self.grid_size):
   row=[]
   for _ in range(self.grid_size):
    row.append(-1)
   self.grid.append(row)

 def fill_grid(self):
  u_id=1
  for row_i in range(self.grid_size):
   for col_i in range(self.grid_size):
    if self.grid[row_i][col_i] != -1: continue;
    # account for if the value of the next few are already filled in
    max_width_size=self.max_size if abs(self.grid_size-1-col_i)>=self.max_size else abs(self.grid_size-1-col_i)
    max_height_size=self.max_size if abs(self.grid_size-1-row_i)>=self.max_size else abs(self.grid_size-1-row_i)
    width=random.randint(1,max_width_size) if max_width_size>1 else 1
    height=random.randint(1,max_height_size) if max_height_size>1 else 1
    for w in range(width):
     for h in range(height):
      self.grid[row_i+h][col_i+w]=u_id
    u_id+=1

 def draw(self):
  start_row=int((self.cell_pix_size*self.grid_size)-self.camera_y)//self.cell_pix_size
  start_col=int((self.cell_pix_size*self.grid_size)-self.camera_x)//self.cell_pix_size
  horizontal_amt=window_w//self.cell_pix_size+3
  vertical_amt=window_h//self.cell_pix_size+3
  by=self.cell_pix_size+self.spacing
  for row_i in range(start_row,min(start_row+vertical_amt,self.grid_size)):
   for col_i in range(start_col,min(start_col+horizontal_amt,self.grid_size)):
    x=self.camera_x-by-((self.grid_size-start_col)*by)+((col_i-start_col)*(by))
    y=self.camera_y-by-((self.grid_size-start_row)*by)+((row_i-start_row)*(by))
    n=self.grid[row_i][col_i]
    rect(int(x),int(y),self.cell_pix_size,self.cell_pix_size,self.colors[n%4])
class Firework:
 def __init__(self):
  self.t=0
  self.tick_e=0
  self.orad=3
  self.ox=random.randint(0,window_w)
  self.oy=window_h+self.orad
  self.ey=random.randint(0,window_h-36)
  self.ocolor=random.randint(11,12)
  self.et_di=abs(self.ey-self.oy) #endtick
 def update_t(self):
  self.t+=1
 def draw(self):
  self.draw_initial()
 def draw_initial(self):
  if self.t/self.et_di<0.6:
   circ(self.ox,self.oy-int(self.et_di*quint_out(self.t,self.et_di)),self.orad,self.ocolor)
  else:
   self.draw_final()
 def draw_final(self):
  raise BaseException("must implement or error.")
class Firework_COut(Firework):
 def __init__(self):
  super().__init__()
  self.end_tick=100
 def draw_final(self):
  circb(self.ox,self.oy-self.et_di,int(self.orad+50*quint_out(self.tick_e,self.end_tick)),self.ocolor)
  self.tick_e+=1
class Firework_CSpreadOut(Firework):
 def __init__(self):
  super().__init__()
  self.end_tick=100
  self.amt=random.randint(3,10)
  self.endpos=[]
  self.rad=2
  self.fill_endpos()
 def fill_endpos(self):
  for _ in range(self.amt):
   self.endpos.append((self.ox+random.randint(-30,30),self.oy-self.et_di+random.randint(-30,30)))
 def draw_final(self):
  for pos in self.endpos:
   m=(pos[1]-(self.oy-self.et_di))/(pos[0]-self.ox)
   x=(pos[0]-self.ox)*quint_out(self.tick_e,self.end_tick)
   y=m*x
   circ(self.ox+int(x),(self.oy-self.et_di)-int(y),self.rad,self.ocolor)
  self.tick_e+=2

# main vars
t=0
window_w=240
window_h=136
sec_t=60
scene1_d=Scene1()
scene2_d=Scene2()
scene3_d=Scene3()
scene4_d=Scene4()
branches=[]
lines=[]
c_outs=[]
grid=ImproperGrid()
fireworks=[]
fireworks_valid=[Firework_COut,Firework_CSpreadOut]
# UTIL
def msg_cen(txt,offy=0,c=2):
 w=print(txt,0,-6)
 print(txt,window_w//2-w//2,window_h//2+offy,c)
def wavy_cen_text(txt):
 x=window_w//2-print(txt,0,-6,0,False)//2
 l_i=0
 for l in txt:
  w=print(l,0,-6,0,False)
  print(l,x,window_h//2+int(7*math.sin((t+l_i)/5.5)),13+(t//5+l_i)%3,False)
  x += w
  l_i+=1

#SCENES
def scene_1():
 cls(0)

 if t==1:
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
 if t==sec_t*3:
  branches.append(BranchDrawer(0,22,0,25,-17,6,20,45))
  branches.append(BranchDrawer(241,88,-20,0,-10,10,15,50))
 for branch in branches:
  branch.t += 1
  branch.draw_branches()
 if t>8.25*sec_t:
  msg_cen("ready?",2,0)
  msg_cen("ready?")
def scene_2():
 cls(3)

 if t%(sec_t*2)==0:
  scene2_d.arrow = Arrow()
 if t%(sec_t)==0:
  lines.append(StraightLineDrawer())
 if t>15.8*sec_t and t%25==0:
  c_outs.append(CircleOut())
 scene2_d.arrow.t += (7-scene2_d.arrow.t*0.03) 
 scene2_d.arrow.draw()
 for line in lines:
  line.t += 1
  line.draw()
 for circle in c_outs:
  circle.t += 1
  circle.draw()
 if t>sec_t*14.5:
  wavy_cen_text("in 2026!")
 else:
  wavy_cen_text("happy birthday")
def scene_3():
 cls(0)

 grid.camera_x-=abs(1.5*math.sin(t/30))
 grid.camera_y-=abs(math.cos(t/60))
 grid.draw()

 if t>24.5*sec_t:
  wavy_cen_text("now enjoy the rest")
 elif t>22.5*sec_t:
  wavy_cen_text("i'll give you the spirit")
 elif t>20.5*sec_t:
  wavy_cen_text("and your growth")
 else:
  wavy_cen_text("cheers to wisdom")

def quint_out(t,et):
 return 1-(1-t/et)**5
def cubic_out(t):
 return 1-math.pow(1-(t/7),3)
def particles():
 spacing=50
 add=2.5
 y_move=spacing//2
 amt=100
 st=t*(11/200)
 y_o_t=max(window_h-window_h*cubic_out(st),0)*2
 for o in range(amt):
  x=math.sin(o+st)
  y=o+y_move*math.sin(st/3.5)
  pix(120+int(33*x),int(((window_h+spacing)//amt+add)*y)-spacing*2+int(y_o_t),1)
def hplus():
 st=t*(11/200)
 size=5 #even
 y=110
 for x in range(-1,11):
  xc=x*24+int(st*3)%25
  rxs=size*math.cos(st)
  rys=size*math.sin(st)
  line(rxs+xc,y+rys,-rxs+xc,y-rys,1)
  line(rys+xc,y-rxs,-rys+xc,y+rxs,1)
def vplus():
 st=t*(11/200)
 size=5 #even
 x=25
 for y in range(-1,7):
  yc=y*24+int(st*3)%25+12
  rxs=size*math.cos(st)
  rys=size*math.sin(st)
  line(x+rxs,yc+rys,x-rxs,yc-rys,1)
  line(x+rys,yc-rxs,x-rys,yc+rxs,1)
def fireworks_play():
 if t%30==0:
  fireworks.append(random.choice(fireworks_valid)())
 for firework in fireworks:
  firework.update_t()
  firework.draw()
  if firework.tick_e/firework.end_tick>0.75 and firework in fireworks:
   fireworks.remove(firework)
def scene_4():
 cls(10)
 #msg_cen("dream big.",0,13)
 particles()
 circ(window_w//2,window_h+25,78+int(7*math.cos(t*(11/700))),6)
 hplus()
 vplus()
 fireworks_play()
 if t>41:
  msg_cen("i hope the visual's nicer.", 0, 14)
 elif t>39.5:
  msg_cen("happy birthday again.", 0, 15)

# MAIN METHOD/RUNNER
def TIC():
 global t
 t+=1
 if t<90:
  cls(0)
 elif t<scene1_d.end_t:
  scene_1()
 elif t<scene2_d.end_t:
  scene_2()
 elif t<scene3_d.end_t:
  scene_3()
 elif t<scene4_d.end_t:
  scene_4()
