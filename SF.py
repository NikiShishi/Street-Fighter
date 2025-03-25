import pyxel,time

pyxel.init(300, 200)

global x0, y0, x1, y1, v, v1, sur_sol, sur_sol1, sol, gravite, HP_0, HP_1, gameover,gameover1,cd,last_time,last_time1

x0: int = 10
y0: int = 120
x1: int = 250
y1: int = 120 
gravite: int = 0.5
sol: int = 120
v: int = 0
v1: int = 0
sur_sol: int =  True
sur_sol1: int = True
HP_0: int = 46
HP_1: int = 46
gameover:bool = False
gameover1:bool = False
longueur: int = 46
largeur:int = 70
cd:int = 0.5
last_time = None
last_time1 = None

pyxel.load("res.pyxres")

def hit(x0 , y0) -> bool :
    pyxel.rect(x0 + 20, y0 + 10 , 40, 10, 11)
    pyxel.blt(x0,y0,0,0,74,66,70)
    if (x0 + longueur + 20 <= x1 + longueur and  x0 + longueur + 20  >= x1) and x0 + longueur + 20 >= y1 + largeur:
        
        return True
    
def hit1(x1,y1) -> bool :
    pyxel.rect(x1 - 20, y1 + 10, 40, 10, 8)
    pyxel.blt(x1 - 20,y1,0,103,82,-67,70)
    if (x1 -20 >= x0 and x1 -20 <= x0 + longueur)  :
        return True

def update():
    global x0, y0, x1, y1, v, v1, sur_sol, sur_sol1, sol, gravite, HP_0, HP_1,gameover,gameover1,longueur, largeur,cd,last_time,last_time1
    
#Déplacement horizontal du player 1
    if pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTX) > 2000:
            x0 = x0 + 2
    elif pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTX) < -2000:
        x0 = x0 - 2
        
#Déplacement vertical

    #Saut
    if sur_sol and pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTY) < -2000:
        v = -7
        sur_sol = False
    #Chute
    if not sur_sol:
        v = v + gravite
    #L'action du Saut
    y0 = y0 + v
    #réinitialisation des valeurs
    if y0 >= sol:
        y0 = sol
        sur_sol = True
    
#déplacement horizontal du 2nd joueur
    if pyxel.btn(pyxel.KEY_D) :
        x1 = x1 + 2
    elif pyxel.btn(pyxel.KEY_Q):
        x1 = x1 - 2
#la gravité
    #condition du saut
    if sur_sol1 and pyxel.btn(pyxel.KEY_Z):
        v1 = -7
        sur_sol1 = False
    #comdition de la chute
    if not sur_sol1:
        v1 = v1 + gravite
    #L'action
    y1 = y1 + v1
    #réinitialisation des valeurs
    if y1 >= sol:
        y1 = sol
        sur_sol1 = True
    

    #Les bords 
    if x0 < 0:
        x0 = 0
    elif x0 > 280:
        x0 = 280
    if x1 < 0:
        x1 = 0
    elif x1 > 280:
        x1 = 280
    

def draw():
    global x, y, x1, y1, v, v1, sur_sol, sur_sol1, sol, gravite, HP_0, HP_1, x0, y0 ,gameover,gameover1,longueur, largeur,cd,last_time,last_time1
    if gameover :
        pyxel.cls(11)
        if pyxel.btn(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
            x0 = 10
            y0 = 120
            x1 = 250
            y1 = 120 
            HP_0 = 46
            HP_1 = 46
            gameover = False
            gameover1 = False

    elif gameover1 :
        pyxel.cls(4)
        if pyxel.btn(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
            x0 = 10
            y0 = 120
            x1 = 250
            y1 = 120 
            HP_0 = 100
            HP_1 = 100
            gameover = False
            gameover1 = False
    else:
        pyxel.cls(1)
        pyxel.rectb(x0, y0, longueur, largeur, 1)
        pyxel.rectb(x1, y1, longueur, largeur, 4)
        pyxel.blt(x0,y0,0,0,0,46,70)
        pyxel.blt(x1,y1,0,103,2,-46,70)
        pyxel.rect(x0, y0 - 30 ,HP_0, 10, 3)
        pyxel.rectb(x0, y0 - 30 ,longueur, 10, 3)
        pyxel.rect(x1, y1 - 30, HP_1, 10, 4)
        pyxel.rectb(x1, y1 - 30 ,longueur, 10, 4)

        #if pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTY) > 2000:
        #    y0 = y0 + 10
        #    sur_sol = True
        # Attaque manette
        
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            current_time = time.time()
            if last_time == None or (current_time - last_time) > cd:
                last_time = current_time
                if hit(x0 , y0):
                    HP_1 = HP_1 - 8
                    pyxel.rect(x1, y1 - 30 ,HP_1, 10, 4)
                    print(HP_1)
                if HP_1 <= 0 :
                    gameover = True
        # Attaque clavier   
                
        if pyxel.btnp(pyxel.KEY_SPACE):
            current_time1 = time.time()
            if last_time1 == None or (current_time1 - last_time1) > cd:
                last_time1 = current_time1
                if hit1(x1, y1):
                    HP_0 = HP_0 - 8

                    print(HP_0)
                if HP_0 <= 0 :
                    gameover1 = True
        
    
    
pyxel.run(update, draw)
