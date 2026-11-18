from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import math,json,base64
ROOT=Path(__file__).parent
OUT=ROOT/'assets'
OUT.mkdir(exist_ok=True)
BG=(13,16,22); WHITE=(245,245,247); MUTED=(156,163,178); RED=(242,52,86)
def f(n,b=False,m=False): return ImageFont.truetype('C:/Windows/Fonts/'+('consola.ttf' if m else 'segoeuib.ttf' if b else 'segoeui.ttf'),n)
def t(d,xy,s,n=28,c=WHITE,b=False,m=False): d.text(xy,s,font=f(n,b,m),fill=c)
def canvas(w,h,g=(.88,.3)):
 im=Image.new('RGB',(w,h),BG); p=im.load()
 for y in range(h):
  for x in range(w):
   q=math.exp(-(((x-w*g[0])/(w*.34))**2+((y-h*g[1])/(h*.75))**2)*2)*.16
   p[x,y]=tuple(int(BG[k]+RED[k]*q) for k in range(3))
 d=ImageDraw.Draw(im);d.rounded_rectangle((1,1,w-2,h-2),25,outline=(46,49,60),width=2)
 return im,d
def line(d,x,y,w=60,c=RED): d.line((x,y,x+w,y),fill=c,width=4)
def arrow(d,x,y,c=WHITE,s=25):
 d.line((x,y+s,x+s,y),fill=c,width=3);d.line((x+2,y,x+s,y,x+s,y+s-2),fill=c,width=3)
def pill(d,x,y,s,n=21):
 w=d.textbbox((0,0),s,font=f(n,True))[2]+32
 d.rounded_rectangle((x,y,x+w,y+42),12,fill=(27,30,40),outline=(57,53,65));t(d,(x+16,y+6),s,n,RED,True)
 return w
def cta(d,x,y,s,w=280):
 d.rounded_rectangle((x,y,x+w,y+60),12,fill=RED);t(d,(x+21,y+12),s,23,WHITE,True);arrow(d,x+w-44,y+18,s=20)
im,d=canvas(1600,620)
for x in range(1040,1600,60):d.line((x,0,x,620),fill=(29,28,37))
for y in range(0,620,60):d.line((1040,y,1598,y),fill=(29,28,37))
line(d,66,62,40);t(d,(124,45),'SMIT PATIL / DEVELOPER',23,MUTED,True,True)
t(d,(62,101),'SMIT',124,WHITE,True);t(d,(62,222),'PATIL.',124,RED,True)
t(d,(70,378),'Frontend Development Specialist',37,WHITE,True)
t(d,(70,434),'AI & Software Developer',30,MUTED)
line(d,70,505,865,(46,49,60));t(d,(70,537),'VADODARA, INDIA',20,MUTED,True,True)
t(d,(398,537),'3RD YEAR / MSU BARODA',20,MUTED,True,True)
cx,cy=1286,290
for r in [208,162,117]:d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(77,34,50),width=2)
d.arc((cx-208,cy-208,cx+208,cy+208),230,326,fill=RED,width=8)
d.arc((cx-162,cy-162,cx+162,cy+162),28,115,fill=(162,47,74),width=5)
d.rounded_rectangle((1160,164,1410,414),45,fill=(23,22,32),outline=(125,44,66),width=2)
t(d,(1183,207),'S/P',90,WHITE,True);d.ellipse((1444,145,1460,161),fill=RED)
pill(d,1100,500,'DESIGN + ENGINEERING',22)
im.save(OUT/'hero.png',optimize=True)
cards=[('wellnest','CONNECTED HEALTHCARE','01','WellNest','One ecosystem. Connected care.',
 ['Seven dedicated portals, connected records,','and consent-based healthcare workflows.'],
 ['7 ROLE-BASED PORTALS','DIGITAL HEALTH ID','CONSENT-BASED ACCESS'],['React','TypeScript','Supabase']),
 ('vistara','AI WEBSITE INTELLIGENCE','02','Vistara Studio','Analyze. Understand. Present.',
 ['Turn a public website URL into evidence,','structured insights, and presentations.'],
 ['WEBSITE INTELLIGENCE','EVIDENCE VALIDATION','PRESENTATION GENERATION'],['React','TypeScript','OpenAI API'])]
for name,kind,num,title,sub,desc,features,stack in cards:
 im,d=canvas(800,830,(.86,.21));t(d,(40,36),'FEATURED BUILD / '+num,20,MUTED,True,True)
 line(d,40,92,40);t(d,(101,77),kind,18,RED,True,True)
 d.rounded_rectangle((40,128,760,342),20,fill=(17,20,29),outline=(57,39,53),width=2)
 if name=='wellnest':
  for xx,yy in [(115,188),(236,268),(570,184),(672,267)]:
   d.line((400,235,xx,yy),fill=(107,40,59),width=2);d.ellipse((xx-9,yy-9,xx+9,yy+9),fill=RED)
  d.ellipse((326,161,474,309),fill=(47,24,37),outline=(178,50,78),width=2)
  d.rounded_rectangle((385,190,415,280),6,fill=WHITE);d.rounded_rectangle((355,220,445,250),6,fill=WHITE)
  t(d,(70,284),'HEALTH ID',16,MUTED,True,True);t(d,(578,147),'CONNECTED CARE',16,MUTED,True,True)
 else:
  for k in range(34):
   x=130+k*16;h=int(12+48*(.5+.5*math.sin(k*.43))**2)
   d.rounded_rectangle((x,235-h,x+5,235+h),3,fill=(125+int(k*3.3),40,76))
  t(d,(70,147),'URL > ANALYSIS > INSIGHT',18,MUTED,True,True);t(d,(546,300),'EVIDENCE FIRST',16,MUTED,True,True)
 t(d,(40,361),title,58,WHITE,True);t(d,(43,442),sub,27,RED,True)
 for i,s in enumerate(desc):t(d,(43,491+i*33),s,24,MUTED)
 for i,s in enumerate(features):
  yy=581+i*34;d.rectangle((45,yy+8,51,yy+14),fill=RED);t(d,(68,yy),s,18,WHITE,True,True)
 x=43
 for s in stack:x+=pill(d,x,699,s,18)+10
 t(d,(44,776),'EXPLORE LIVE WEBSITE',20,WHITE,True,True);arrow(d,700,777,RED,22)
 im.save(OUT/(name+'.png'),optimize=True)
im,d=canvas(1600,470,(.83,.68));t(d,(56,39),'03 / PERSONAL PORTFOLIO',21,MUTED,True,True)
t(d,(51,100),'Digital experiences.',69,WHITE,True);t(d,(51,178),'Beyond the ordinary.',69,RED,True)
t(d,(58,287),'Explore my work, skills, background, and approach.',27,MUTED)
cta(d,58,361,'OPEN MY PORTFOLIO',340);t(d,(446,378),'HTML / CSS / JAVASCRIPT',19,MUTED,True,True)
for i in range(3):
 xx=1130+i*37;yy=124-i*24;d.rounded_rectangle((xx,yy,xx+275,yy+254),24,fill=(26+i*3,21,32+i*2),outline=(99+i*26,37,57),width=2)
t(d,(1238,148),'</>',62,WHITE,True,True);line(d,1238,250,155)
for i,ww in enumerate([135,95,115]):d.rounded_rectangle((1238,279+i*22,1238+ww,285+i*22),3,fill=(95,52,66))
im.save(OUT/'portfolio.png',optimize=True)
im,d=canvas(1600,266,(.2,.2));t(d,(48,33),'THE TOOLKIT',22,RED,True,True)
t(d,(48,79),'Built with modern web technologies.',34,WHITE,True)
x=48
for s in ['React','TypeScript','JavaScript','HTML / CSS','Node.js','Express','Supabase','PostgreSQL','Git','Vercel']:x+=pill(d,x,157,s,19)+10
im.save(OUT/'toolkit.png',optimize=True)
im,d=canvas(1600,190,(.5,.2));t(d,(52,35),'Have an idea worth building?',42,WHITE,True)
t(d,(54,100),"LET'S CONNECT / FRONTEND, FULL-STACK & AI",22,MUTED,True,True);cta(d,1230,65,'LINKEDIN',300)
im.save(OUT/'connect.png',optimize=True)
print(json.dumps({'assets':[{'path':'assets/'+p.name,'content':base64.b64encode(p.read_bytes()).decode(),'bytes':p.stat().st_size} for p in sorted(OUT.glob('*.png'))]}))
