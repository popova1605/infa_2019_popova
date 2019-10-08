from graph import*
from math import*


def draw_man(x, y, height, k=1, angry=0):
    '''Рисует эскимоса с координатами головы x и y,
        высотой тела h
        при k=1 палка слева, при k=-1 - справа'''
    color(235, 235, 235)
    ellipse(x, y, 0.583*height, 0.383*height)               # Капюшон
    color(186, 142, 98)
    ellipse(x, 1.083*height + y, 0.583*height, height)                                      # Тело
    ellipse(k*0.583*height + x, 0.633*height + y, 0.417*height, 0.133*height, k*3.14/6)     # Рука без палки
    ellipse(-k*0.583*height + x, 0.583*height + y, 0.417*height, 0.133*height)              # Рука с палкой
    color(206, 162, 118)           
    ellipse(x, y, 0.45*height, 0.266*height)                                # Голова       
    face(x, 0.033*height + y, 0.7*height, 0.4*height, angry)                # Лицо   
    color(255, 255, 255)
    rectangle(-k*0.667*height + x, 1.2*height + y, k*0.667*height + x, 2.25*height + y)
    color(186, 142, 98)
    ellipse(-k*0.25*height + x, 1.25*height + y, 0.167*height, 0.367*height)        # Ноги
    ellipse(k*0.25*height + x, 1.25*height + y, 0.167*height, 0.367*height) 
    ellipse(-k*0.383*height + x, 1.617*height + y, 0.217*height, 0.083*height)      # Ступни
    ellipse(k*0.383*height + x, 1.617*height + y, 0.217*height, 0.083*height)
    color(156, 112, 68)
    rectangle(-k*0.083*height + x, 0.267*height + y, k*0.083*height + x, 1.167*height + y)  # Мех
    rectangle(-k*0.583*height + x, 1.2*height + y, k*0.583*height + x, 1.417*height + y)
    penColor("black")
    line(-k*0.933*height + x, -0.5*height + y, -k*0.933*height + x, 1.617*height + y)       # Палка
    
def draw_cat(x, y, length, hungry=0):
    """Рисует кошку с координатами центра тела x и y,
       длиной тела 2*lenth"""
    cat = []
    color(205, 219, 210)
    cat.append(ellipse(x, y, length, 0.3*length))																			# Drawing body
    cat.append(ellipse(0.75*length + x, 0.5*length + y, 0.575*length, 0.125*length, 3.14/5.5))		# Задние лапы  
    cat.append(ellipse(1.125*length + x, 0.25*length + y, 0.575*length, 0.125*length, 3.14/6.5))			
    cat.append(ellipse(-1.25*length + x, 0.075*length + y, 0.575*length, 0.125*length, -3.14/20))	# Передние лапы
    cat.append(ellipse(-0.75*length + x, 0.325*length + y, 0.575*length, 0.125*length, -3.14/7.5))				
    cat.append(ellipse(1.625*length + x, -0.425*length + y, 0.875*length, 0.175*length, -3.14/7))	# Хвост
    if hungry == 0:
        cat += draw_fish(-length + x, -0.275*length + y, 0.75*length, 0.2*length, 3.14/6)
    cat += head_of_cat(x-0.7*length, y-length/2, 5/6*length)
    return cat

def draw_house(x, y, height):
    """Рисует юрту
       высотой height
       с координатами центра основания x,y"""
    penColor("black")
    brushColor(247, 247, 249)
    ellipse(x, y, 2/3*height, height/2)
    ellipse(x, y, 4/9*height, height/2)
    ellipse(x, y, 2/9*height, height/2)
    color(255, 255, 255)
    rectangle(-height*2/3 + x, y, height*2/3 + x, height/2 + y)
    penColor("black")
    line(-height*2/3 + x, y, height*2/3 + x, y)
    line(-height/2 + x, -up_ell_pair(height/2, 2/3*height, height/2) + y,
         height/2 + x, -up_ell_pair(height/2, 2/3*height, height/2) + y)
    line(-height/3 + x, -up_ell_pair(height/3, 2/3*height, height/2) + y,
         height/3 + x, -up_ell_pair(height/3, 2/3*height, height/2) + y)
    line(-height*15/24 + x, -up_ell_pair(height*15/24, 2/3*height, height/2) + y,
         height*15/24 + x, -up_ell_pair(height*15/24, 2/3*height, height/2) + y)


def draw_fish(x, y, f_length, f_width, phi):
    """Рисует рыбу
       с координатами центра x,y,
       шириной f_width и длиной f_length,
       повёрнутую по часовой стрелке на phi радиан"""
    fish = []
    color(85,211,199)
    penColor("black")
    fish.append(ellipse(x, y, f_length/2, f_width/2, phi))
    fin1=[(0,  f_width/2), (f_width*0.75, f_width*1.5), (-f_width*0.75, f_width*1.5)]
    fin2=[(0,  -f_width/2), (f_width*0.75, -f_width*1.5), (-f_width*0.75, -f_width*1.5)]
    tail=[(f_length/2, 0), (f_length/2 + f_width, -f_width*0.75), (f_length/2 + f_width, f_width*0.75)]
    for i in range(3):
        fin1[i] = (fin1[i][0]*cos(phi) - fin1[i][1]*sin(phi) + x, fin1[i][0]*sin(phi) + fin1[i][1]*cos(phi) + y)   
        fin2[i] = (fin2[i][0]*cos(phi) - fin2[i][1]*sin(phi) + x, fin2[i][0]*sin(phi) + fin2[i][1]*cos(phi) + y)
        tail[i] = (tail[i][0]*cos(phi) - tail[i][1]*sin(phi) + x, tail[i][0]*sin(phi) + tail[i][1]*cos(phi) + y)
    brushColor("red")
    fish.append(polygon(fin1))
    fish.append(polygon(fin2))
    fish.append(polygon(tail))
    color(0, 0, 0)
    fish.append(circle(-0.7*f_length/2*cos(phi) + x, -0.7*f_length/2*sin(phi) + y, f_width/6))
    return fish

def head_of_cat(x, y, width):
    """Рисует голову кошки с координатами центра x и y
       шириной width"""
    cats_head = []
    color(255, 255, 255)
    cats_head.append(polygon([(x - width/4, y + 0.8*width/2),
                              (x-width*5/16, y + 0.5*width/2), (x - width*3/16, y + 0.5*width/2)]))
    cats_head.append(polygon([(x, y + width/2 - width/16),
                              (x - width*1/16, y + 0.5*width/2), (x + width*1/16, y + 0.5*width/2)]))
    color(205, 219, 210)
    cats_head.append(polygon([(x - width/4 - width/8, y - 0.5*width/4),
                              (x-width/4 + width/8, y - width/4), (x - width/4,y - width/2)]))
    cats_head.append(polygon([(x + width/4 - width/8, y - 0.5*width/4),
                              (x+width/4 + width/8, y - width/4), (x+width/4, y - width/2)]))
    cats_head.append(ellipse(x, y, width/2, 0.733*width/2))
    color(255, 255, 255)
    cats_head.append(circle(x - width/4, y - 0.5*width/4, width/10))
    cats_head.append(circle(x + width/4, y - 0.5*width/4, width/10))
    color(0, 0, 0)
    cats_head.append(circle(x - width/4 + width/20, y - 0.5*width/4, width/15))
    cats_head.append(circle(x + width/4 + width/20, y - 0.5*width/4, width/15))
    cats_head.append(circle(x - width/8, y + 0.733*width/6, width/18))
    return cats_head

def face(x, y, width, height, angry=0):
    """Рисует лицо эскимоса
       с координатами центра x,y,
       шириной width и высотой height"""
    color(255, 250, 250)         
    ellipse(x, y, width/2, height/2)
    penColor("black")
    line(x - width/4 - width/15, y - height/6, x - width/4 + width/12, y - height/6 + angry*height/7)
    line(x + width/4 - width/12, y - height/6 + angry*height/7, x + width/4 + width/15, y - height/6)
    line(x - width/12, y + height/6, x + width/12, y + height/6 + angry*height/12)


def ellipse(x, y, A, B, rotation=0):
    """рисует эллипс с координатами центра x и y,
       горизонтальной полуосью A и вертикальной B
       и поворачивает его на rotation радиан по часовой стрелке"""
    A = int(A)
    list_of_points = []
    for i in range(- A, A, 1):
        list_of_points.append((i , B * (1 - i*i/A/A)**0.5))
    for i in range(A, -A, -1):
        list_of_points.append((i, - B * (1 - i*i/A/A)**0.5))
    phi=rotation
    p=list_of_points
    for i in range(len(p)):
        list_of_points[i] = (p[i][0]*cos(phi) - p[i][1]*sin(phi), p[i][0]*sin(phi) + p[i][1]*cos(phi))
    for i in range(len(p)):
        list_of_points[i] = (p[i][0] + x, p[i][1] + y)
    return polygon(list_of_points)

def color(r, g, b):
    """Измняет одновременно цвет контура и заливки"""
    penColor(r, g, b)
    brushColor(r, g, b)

def up_ell_pair(x, A, B):
    return B * (1 - (x/A)**2)**0.5


def falling_fish():
    """Анимация рыбы"""
    global t
    global fish_falling_time
    global fish_falled
    global fish_catched
    if fish_catched == 0:
        if yCoord(fish[0]) < 400 and t > 15:
            for i in fish:
                moveObjectBy(i, -2, fish_falling_time/8)
            fish_falling_time += 1
        else:
            fish_falled = 1

def running_cat():
    """Анимация кошки"""
    global t
    global fish_falling_time
    global fish_falled
    global fish_catched
    global hungry_cat
    global fished_cat
    global fish
    if fish_falled == 1:
        if fish_catched == 0:
            for i in hungry_cat:
                moveObjectBy(i, -2, 0)
            if xCoord(hungry_cat[-1]) < xCoord(fish[1]):
                for i in fish:
                    deleteObject(i)
                dx = xCoord(hungry_cat[-1]) - xCoord(fished_cat[-1])
                dy = yCoord(hungry_cat[-1]) - yCoord(fished_cat[-1])
                for i in fished_cat:
                    moveObjectBy(i, dx, dy)
                for i in hungry_cat:
                    deleteObject(i)
                draw_man(400, 250, 80, 1, 1)
                fish_catched = 1
        else:
            for i in fished_cat:
                moveObjectBy(i, -2, 0)
            if xCoord(fished_cat[-1]) < -100:
                for i in fished_cat:
                    deleteObject(i)
                draw_man(400, 250, 80, 1, 0)
                hungry_cat = draw_cat(700, 400, 40, 1)
                fished_cat = draw_cat(700, 400, 40, 0)
                fish = draw_fish(-0.933*height + x, -0.5*height + y, 40, 10, 0)
                fish_falling_time = 0
                fish_catched = 0
                fish_falled = 0
                t = 0

def timer():
    """Задержка"""
    global t
    t += 1


penColor(235, 230, 253)
brushColor(235, 230, 253)      # Небо
rectangle(0, 0, 1000, 205)

draw_house(50,220,44)
draw_house(260,250,55)
draw_house(150,260,110)
draw_house(70,290,77)
draw_house(170,300,66)

draw_man(380, 200, 23)
draw_man(460, 220, 23)
draw_man(405, 235, 23)
draw_man(375, 270, 23, -1)
draw_man(275, 285, 23, -1)
draw_man(320, 260, 23, -1)
draw_man(445, 277, 23)

draw_cat(210, 500, 30)
draw_cat(110, 570, 30)
draw_cat(0, 520, 30)
draw_cat(480, 600, 30)
                
x = 400
y = 250
height = 80
draw_man(x, y, height)
hungry_cat = draw_cat(700, 400, 40, 1)
fished_cat = draw_cat(700, 400, 40, 0)
fish = draw_fish(-0.933*height + x, -0.5*height + y, 40, 10, 0)
fish_falling_time = 0
fish_catched = 0
fish_falled = 0
t = 0
onTimer(falling_fish, 25)
onTimer(running_cat, 25)
onTimer(timer, 50)

run()



