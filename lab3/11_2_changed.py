from graph import*
from math import*

def ellips(x,y,A,B,rotation):
    A=int(A)
    list_of_points=[]
    for i in range(-A,A,1):
        list_of_points.append((i,B*(1-i*i/A/A)**0.5))
    for i in range(A,-A,-1):
        list_of_points.append((i,-B*(1-i*i/A/A)**0.5))
    phi=rotation
    p=list_of_points
    for i in range(len(p)):
        list_of_points[i]=(p[i][0]*cos(phi)-p[i][1]*sin(phi),p[i][0]*sin(phi)+p[i][1]*cos(phi))
    for i in range(len(p)):
        list_of_points[i]=(p[i][0]+x,p[i][1]+y)
    polygon(list_of_points)

def draw_man(x,y,k):
    if k<0:
        t=-k
    else:
        t=k
    brushColor(238,212,162)
    penColor(238,212,162)
    ellips(x,y,t*35,t*23,0) 
    brushColor(186,142,98)
    penColor(186,142,98)
    ellips(x,t*(400-335)+y,t*35,t*60,0)                         
    ellips(k*(385-350)+x,t*(373-335)+y,t*25,t*8,k/t*3.14/6)     
    ellips(k*(315-350)+x,t*(370-335)+y,t*25,t*8,0)              
    brushColor(206,162,118)
    penColor(206,162,118)           
    ellips(x,y,t*27,t*16,0)          
    brushColor(255,250,250)         
    penColor(255,250,250)           
    ellips(x,t*(337-335)+y,t*21,t*12,0)    
    brushColor(255,255,255)
    penColor(255,255,255)
    rectangle(k*(310-350)+x,t*(407-335)+y,k*(390-350)+x,t*(470-335)+y)
    brushColor(186,142,98)
    penColor(186,142,98)
    ellips(k*(335-350)+x,t*(410-335)+y,t*10,t*22,0)     
    ellips(k*(365-350)+x,t*(410-335)+y,t*10,t*22,0)     
    ellips(k*(327-350)+x,t*(432-335)+y,t*13,t*5,0)  
    ellips(k*(373-350)+x,t*(432-335)+y,t*13,t*5,0)  
    penColor(156,112,68)
    brushColor(156,112,68)
    rectangle(k*(345-350)+x,t*(351-335)+y,k*(355-350)+x,t*(405-335)+y)  
    rectangle(k*(315-350)+x,t*(407-335)+y,k*(385-350)+x,t*(420-335)+y)  
    penColor("black")
    penSize(t)
    line(k*(294-350)+x,t*(305-335)+y,k*(294-350)+x,t*(432-335)+y)
    line(k*(-7)+x,t*(0)+y,k*(-15)+x,t*(-4)+y)       
    line(k*(5)+x,t*(0)+y,k*(14)+x,t*(-4)+y)       
    line(k*(345-350)+x,t*(341-335)+y,k*(355-350)+x,t*(341-335)+y) 
    penSize(1)     


def draw_cat(x,y,k):
    if k<0:
        t=-k
    else:
        t=k
    penColor(97, 97, 97)
    brushColor(97, 97, 97)
    ellips(x,y,t*40,t*12,0)     
    ellips(k*(170-140)+x,t*(470-450)+y,t*23,t*5,k/t*3.14/5.5)   
    ellips(k*(185-140)+x,t*(460-450)+y,t*23,t*5,k/t*3.14/6.5)   
    ellips(k*(90-140)+x,t*(453-450)+y,t*23,t*5,-k/t*3.14/20)    
    ellips(k*(110-140)+x,t*(463-450)+y,t*23,t*5,-k/t*3.14/7.5)  
    ellips(k*(205-140)+x,t*(433-450)+y,t*35,t*7,-k/t*3.14/7)       
    penColor("black")
    brushColor(85,211,199)
    ellips(k*(100-140)+x,t*(439-450)+y,t*15,t*4,k/t*3.14/6) 
    polygon([(k*(113-140)+x,t*(447-450)+y),(k*(125-140)+x,k*(447-450)+y),(k*(122-140)+x,k*(455-450)+y)])
    brushColor("red")
    polygon([(k*(96-140)+x,t*(441-450)+y),(k*(91-140)+x,t*(448-450)+y),(k*(100-140)+x,t*(452-450)+y)])
    polygon([(k*(99-140)+x,t*(435-450)+y),(k*(95-140)+x,t*(426-450)+y),(k*(105-140)+x,t*(427-450)+y)])
    penColor("white")
    brushColor("white")
    polygon([[k*(-40 + (3 ** 0.5))+x,t*(-12 - 3)+y], [k*(-40 - (3 ** 0.5))+x,t*(-12 - 3)+y], [k*(-40)+x,t*(-10)+y]])
    polygon([[k*(-35 + (3 ** 0.5) / 1.75)+x,t*(-10 - 0.75)+y], [k*(-35 - (3 ** 0.5) / 1.75)+x,t*(-10 - 0.75)+y], [k*(-35)+x,t*(-10 + 2.5)+y]])    
    penColor(97, 97, 97)
    brushColor(97, 97, 97)
    penSize(2)
    ellips(k*(112-140)+x,t*(430-450)+y,t*15,t*11,0)     
    polygon([(k*(110-140)+x,t*(418-450)+y),(k*(113-140)+x,t*(414-450)+y),(k*(115-140)+x,t*(420-450)+y)])
    polygon([(k*(120-140)+x,t*(420-450)+y),(k*(123-140)+x,t*(416-450)+y),(k*(125-140)+x,t*(423-450)+y)])
    penSize(1)
    penColor("white")
    brushColor("white")
    circle(k*(113-140)+x,t*(428-450)+y,t*3) 
    circle(k*(101-140)+x,t*(427-450)+y,t*3) 
    penColor("black")
    brushColor("black")
    circle(k*(115-140)+x,t*(428-450)+y,t*2) 
    circle(k*(103-140)+x,t*(427-450)+y,t*2) 
    penSize(2)
    polygon([[k*(-36)+x,t*(-15)+y], [k*(-36 + 3 ** 0.5)+x,t*(-18)+y], [k*(-36 - 3 ** 0.5)+x,t*(-18)+y]])
    penSize(1)
    brushColor("blue")
    circle(k*(92-140)+x,t*(434-450)+y,t*2)
    brushColor("black")
    circle(k*(92-140)+x,t*(434-450 - 0.75)+y,t*1)
    brushColor("white")
    circle(k*(92-140)+x,t*(434-450 + 0.75)+y,t*0.5) 

def draw_house(x,y,k):
    penColor("black")
    brushColor(247,247,249)
    penSize(2)
    ellips(x,y,k*100,k*75,0) 
    penColor("white")
    brushColor("white")
    rectangle(k*(48-150)+x,k*(320-320)+y,k*(252-150)+x,k*(400-320)+y)
    penSize(1)
    penColor("black")
    line(k*(50-150)+x,y,k*(250-150)+x,y)
    line(-k*100*(1-25*25/75/75)**0.5+x,k*(295-320)+y,k*100*(1-25*25/75/75)**0.5+x,k*(295-320)+y)    
    line(-k*100*(1-45*45/75/75)**0.5+x,k*(275-320)+y,k*100*(1-45*45/75/75)**0.5+x,k*(275-320)+y)
    line(-k*100*(1-65*65/75/75)**0.5+x,k*(255-320)+y,k*100*(1-65*65/75/75)**0.5+x,k*(255-320)+y)
    line(k*(125-150)+x,k*(295-320)+y,k*(125-150)+x,y)               
    line(k*(80-150)+x,k*(295-320)+y,k*(80-150)+x,y)                 
    line(k*(175-150)+x,k*(295-320)+y,k*(175-150)+x,y)               
    line(k*(225-150)+x,k*(295-320)+y,k*(225-150)+x,y)
    line(k*(103-150)+x,k*(275-320)+y,k*(103-150)+x,k*(295-320)+y)
    line(x,k*(275-320)+y,x,k*(295-320)+y)
    line(k*(200-150)+x,k*(275-320)+y,k*(200-150)+x,k*(295-320)+y)
    line(k*(125-150)+x,k*(255-320)+y,k*(125-150)+x,k*(275-320)+y)
    line(k*(175-150)+x,k*(255-320)+y,k*(175-150)+x,k*(275-320)+y)
    line(x,k*(255-320)+y,x,k*(245-320)+y)

penColor(235,230,253)    
brushColor(200,200,255)  
rectangle(0,0,1000,265)  

draw_house(50,280,0.4)
draw_house(260,310,0.5)
draw_house(150,320,1)
draw_house(70,350,0.7)
draw_house(170,380,0.6)

draw_man(380,260,0.4)
draw_man(460,280,0.4)
draw_man(405,295,0.4)
draw_man(375,330,-0.4)
draw_man(275,375,-0.4)
draw_man(320,320,-0.4)
draw_man(445,337,0.4)
draw_man(400,400,1.1)

draw_cat(210,460,1.3)
draw_cat(110,530,0.8)
draw_cat(0,480,0.8)
draw_cat(290,590,0.8)
draw_cat(480,560,0.8)

run()