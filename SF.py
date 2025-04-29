import pyxel,time

pyxel.init(600, 400, title="My Pyxel App", fps=40)

global x0, y0, x1, y1, yp, yp1 
global v, v1, sur_sol, sur_sol1,screen, sol, gravite, HP_0, HP_1, gameover ,gameover1 ,cd ,DAMAGE ,shield1, VITESSE_PROJECTILE ,projectile , shield ,projectile1
global last_time ,last_time1, last_timep, last_timep1
x0: int = 100
y0: int = 230
x1: int = 450
y1: int = 230
yp: int = 0
yp1: int = 0
gravite: int = 0.5
sol: int = 300
v: int = 0
v1: int = 0    
VITESSE_PROJECTILE: int = 2
sur_sol: int =  True
sur_sol1: int = True
HP_0: int = 46
HP_1: int = 46
gameover:bool = False
gameover1:bool = False
longueur: int = 46
largeur:int = 70
cd:int = 0.3
last_time = None
last_time1 = None
last_timep = None
last_timep1 = None
DAMAGE: int = 6
projectile = []
projectile1 = []
shield: bool = False
shield1: bool = False
screen: bool = True

pyxel.load("re.pyxres")

def hit(x0,y0) -> bool :
    if shield1 == False:
        pyxel.rect(x0 + 20, y0 + 10 , 40, 10, 11)
        pyxel.blt(x0,y0,0,0,74,66,70)
        if shield == True:
            return False
        if (x0 + longueur + 20 <= x1 + longueur and  x0 + longueur + 20  >= x1) and y0 >= y1 :
                return True
    else:
        return False
    
def hit1(x1,y1) -> bool :
    if pyxel.btn(pyxel.KEY_T) == False:
        pyxel.rect(x1 - 20, y1 + 10, 40, 10, 8)
        pyxel.blt(x1 - 20,y1,0,103,82,-67,70)
        if shield1 == True:
            return False
        if (x1 -20 >= x0 and x1 -20 <= x0 + longueur) and y1 >= y0 :
                return True
    else:
        return False
    
def hitprojectile() -> bool :
    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) == False :
        if shield == True :
            return False 
        if (projectile[0] + 20 >= x1 )  :
            return True
    else :
        return False
        
def hitprojectile1() -> bool :
    if pyxel.btnp(pyxel.KEY_X) == False :
        if shield1 == True :
            return False 
        if (projectile1[0] <= (x0 + longueur) ) and (yp1 >= y0 and (yp1 <= (y0 + largeur))):
            return True
    else :
        return False
        


def update():
    global x0, y0, x1, y1, yp, yp1
    global v, v1, sur_sol, screen,sur_sol1, sol, gravite, HP_0, HP_1,gameover ,shield1,gameover1 ,longueur, largeur ,cd ,DAMAGE ,VITESSE_PROJECTILE ,projectile ,shield ,projectile1
    global last_time ,last_time1,last_timep, last_timep1
    shield = False
    shield1 = False

#Déplacement horizontal du joueur 1
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
    if sur_sol == False :
        v = v + gravite
    #L'action du Saut
    y0 = y0 + v
    #réinitialisation des valeurs
    if (y0 >= sol - largeur) and (x0 >= 80 - longueur):
        y0 = sol - largeur 
        sur_sol = True
    
#Déplacement horizontal du 2nd joueur
    if pyxel.btn(pyxel.KEY_D) :
        x1 = x1 + 2
    elif pyxel.btn(pyxel.KEY_Q):
        x1 = x1 - 2
#La gravité
    #Condition du saut
    if sur_sol1 and pyxel.btn(pyxel.KEY_Z):
        v1 = -7
        sur_sol1 = False
    #Condition de la chute
    if sur_sol1 == False:
        v1 = v1 + gravite
    #L'action
    y1 = y1 + v1
    #Réinitialisation des valeurs
    if (y1 >= sol - largeur) and (x1 <= 500):
        y1 = sol - largeur 
        sur_sol1 = True

    #Les bords 
    if x0 <= 80 - longueur:
        y0 = y0 + 7
    elif x0 >= 500:
        y0 = y0 + 7
    if x1 <= 24:
        y1 = y1 + 7
    elif x1 >= 500:
        y1 = y1 + 7


    if y0 >= 400:
        HP_0 = 0
        gameover1 = True
    elif y1 >= 400:
        HP_1 = 0
        gameover = True



    
    if pyxel.btn(pyxel.KEY_RETURN):
        screen = False 

    if pyxel.btn(pyxel.KEY_DOLLAR):
        HP_1 += 10

def draw():
    global x0, y0, x1, y1, yp, yp1 
    global v, v1, sur_sol,screen, sur_sol1, sol, gravite, HP_0, HP_1, gameover ,gameover1 ,cd ,DAMAGE ,shield1, VITESSE_PROJECTILE ,projectile , shield ,projectile1
    global last_time ,last_time1,last_timep ,last_timep1
    if screen == True : 
        pyxel.cls(1)    
    else : 
        if gameover :
            pyxel.cls(11)
            pyxel.text(120, 100, "Victoire du joueur 1", 2 )

        # Mise à 0 des variables
            if pyxel.btn(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
                x0 = 100
                y0 = 230
                x1 = 450
                y1 = 230
                HP_0 = 46
                HP_1 = 46
                gameover = False
                gameover1 = False
                projectile = []
                projectile1 = []
                           

        elif gameover1 :
            pyxel.cls(4)
            pyxel.text(120, 100, "Victoire du joueur 2", 2 )

        # Mise à 0 des variables
            if pyxel.btn(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
                x0 = 100
                y0 = 230
                x1 = 450
                y1 = 230
                HP_0 = 46
                HP_1 = 46
                gameover = False
                gameover1 = False
                projectile = []
                projectile1 = []    
                
        else:
            pyxel.cls(0)
            pyxel.rectb(x0, y0, longueur, largeur, 1)
            pyxel.rectb(x1, y1, longueur, largeur, 4)
            pyxel.blt(x0,y0,0 ,0 ,0 ,46 ,70)
            pyxel.blt(x1,y1,0,103, 2,-46 ,70)
            pyxel.rect(x0, y0 - 20 ,HP_0, 10, 3)
            pyxel.rectb(x0, y0 - 20 ,longueur, 10, 3)
            pyxel.rect(x1, y1 - 20, HP_1, 10, 4)
            pyxel.rectb(x1, y1 - 20 ,longueur, 10, 4)
            pyxel.rect(80, sol ,430, 10, 2)

            if pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
                shield1 = True
                pyxel.rect(x0 + 46, y0 , 10,70, 10)
            
        
            if pyxel.btn(pyxel.KEY_T):
                shield = True
                pyxel.rect(x1 - 10, y1 , 10,70, 10)

            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) and shield1 == False:
                current_timep1 = time.time()
                if len(projectile) < 1 and (last_timep1 == None or (current_timep1 - last_timep1) > cd):
                    last_timep1 = current_timep1
                    projectile.append((x0 + longueur))
                    yp = y0
            for t in projectile:
                if projectile[0] < 600 :
                    projectile[0] += VITESSE_PROJECTILE
                    pyxel.rect(projectile[0], yp + 20, 20, 10 , 1)
                    pyxel.blt(projectile[0] , yp + 20 , 0 ,213,8,20,12)
                    if (shield == True and projectile[0] + 20 >= x1 -10 ):
                        projectile.remove(projectile[0])
                    if hitprojectile():
                        HP_1 -= (DAMAGE - 2)
                        projectile.remove(projectile[0])
                        if HP_1 <= 0 :
                            gameover = True       
                else :
                    projectile.remove(t)
            
            if pyxel.btnp(pyxel.KEY_X) and shield == False :
                current_timep1 = time.time()
                if len(projectile1) < 1 and (last_timep == None or (current_timep1 - last_timep) > cd):
                    last_timep = current_timep1
                    projectile1.append((x1 - 20))
                    yp1 = y1
            for tir in projectile1:
                if projectile1[0] > 0 :
                    projectile1[0] -= VITESSE_PROJECTILE
                    pyxel.rect(projectile1[0], yp1 + 20, 20, 10 , 1)
                    pyxel.blt(projectile1[0] , yp1 + 20 , 0 ,216,25,21,15)
                    if (shield1 == True and (projectile1[0] <= x0 + longueur + 20 )):
                        projectile1.remove(projectile1[0])
                    if hitprojectile1():
                        HP_0 -= (DAMAGE - 2)
                        projectile1.remove(projectile1[0])
                        if HP_0 <= 0 :
                            gameover1 = True   
                else :
                    projectile1.remove(tir)

            # Attaque 1 manette
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                current_time = time.time()
                if last_time == None or (current_time - last_time) > cd:
                    last_time = current_time
                    if hit(x0 , y0):
                        HP_1 = HP_1 - DAMAGE
                        pyxel.rect(x1, y1 - 30 ,HP_1, 10, 4)
                        print(HP_1)
                    if HP_1 <= 0 :
                        gameover = True
            # Attaque 1 clavier  
                    
            if pyxel.btnp(pyxel.KEY_SPACE):
                current_time1 = time.time()
                if last_time1 == None or (current_time1 - last_time1) > cd:
                    last_time1 = current_time1
                    if hit1(x1, y1):
                        HP_0 = HP_0 - DAMAGE
                        print(HP_0)
                    if HP_0 <= 0 :
                        gameover1 = True
        
   
pyxel.run(update, draw)

