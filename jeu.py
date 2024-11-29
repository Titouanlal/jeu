import pyxel, random #import c'est pour prendre des codes déjà fais pur les utiliser

class Jeu:
    """Voici la class de mon jeu
    Lancez en faisant Jeu()"""

    def __init__(self):# quand le jeu commence
        
        pyxel.init(128, 128, title="Nuit du c0de")# c'est la taille et le titre de la page
        self.score = 0 # le score au début du jeu
        self.vaisseau_x = 60 # l'endroit où le vaisseau vas apparaitre pour x
        self.vaisseau_y = 60 # l'endroit où le vaisseau vas apparaitre pour y
        self.vies = 5 # le nombre d vie au début du jeu
        self.tirs_liste = [] # la liste des tirs
        self.ennemis_liste = [] # la liste des ennemis
        self.explosions_liste = [] # la liste des explosions
        self.meteors_liste = []
        self.bonus_liste = []
        self.tirsbonus_liste = []
        self.tirsbonus2_liste = []
        self.tirsbonus3_liste = []
        self.bonus_active = False 
        self.coeursbonus_liste = []
        self.audiogameover = False
        
        pyxel.load("titouan.pyxres") # le nom du fichier où il doit chercher les dessin
         
        pyxel.run(self.update, self.draw)
    
    def coeursbonus_creation(self):
        if (pyxel.frame_count % 2000 == 0): 
            self.coeursbonus_liste.append([random.randint(0, 120),0])
   
    def coeursbonus_deplacement(self):
        for coeursbonus in self.coeursbonus_liste:
            coeursbonus[1] += 1
            if  coeursbonus[1]>128:
                self.coeursbonus_liste.remove(coeursbonus)
    
    def coeursbonus_activation(self):
        for coeursbonus in self.coeursbonus_liste:
            if coeursbonus[0] <= self.vaisseau_x+12 and coeursbonus[1] <= self.vaisseau_y+22 and coeursbonus[0]+8 >= self.vaisseau_x and coeursbonus[1]+8 >= self.vaisseau_y:
                if coeursbonus in self.coeursbonus_liste:
                    self.coeursbonus_liste.remove(coeursbonus)
                    self.vies += 1
   
    def bonus_creation(self):
        if (pyxel.frame_count % 1500 == 0): 
            self.bonus_liste.append([random.randint(0, 120),0])

    def bonus_deplacement(self):
        for bonus in self.bonus_liste:
            bonus[1] += 1
            if  bonus[1]>128:
                self.bonus_liste.remove(bonus)


    def bonus_activation(self):
        for bonus in self.bonus_liste:
            if bonus[0] <= self.vaisseau_x+12 and bonus[1] <= self.vaisseau_y+22 and bonus[0]+8 >= self.vaisseau_x and bonus[1]+8 >= self.vaisseau_y:
                if bonus in self.bonus_liste:
                    self.bonus_liste.remove(bonus)
                    self.bonus_active = True
                    pyxel.play(0, 5)

    def tirsbonus_creation(self):
        if  pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.bonus_active == True:
            self.tirsbonus_liste.append([self.vaisseau_x+4, self.vaisseau_y-4])

    def tirsbonus2_creation(self):
        if  pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.bonus_active == True:
            self.tirsbonus2_liste.append([self.vaisseau_x+4, self.vaisseau_y-4])

    def tirsbonus3_creation(self):
        if  pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.bonus_active == True:
            self.tirsbonus3_liste.append([self.vaisseau_x+4, self.vaisseau_y-4])


    def tirsbonus_deplacement(self):
        """tirs qui vas vers la gauche"""
        for tirsbonus in self.tirsbonus_liste:
            tirsbonus[0] -= 1
            tirsbonus[1] -= 1
            if tirsbonus[0]<0 or tirsbonus[1]<0:
                self.tirsbonus_liste.remove(tirsbonus)

    def tirsbonus2_deplacement(self):
        """tirs qui vas vers la droite"""
        for tirsbonus2 in self.tirsbonus2_liste:
            tirsbonus2[0] += 1
            tirsbonus2[1] -= 1
            if tirsbonus2[0]>120 or tirsbonus2[1]<0:
                self.tirsbonus2_liste.remove(tirsbonus2)

    def tirsbonus3_deplacement(self):
        """tirs" qui vas vers le haut"""
        for tirsbonus3 in self.tirsbonus3_liste:
            tirsbonus3[1] -= 1
            if tirsbonus3[1]<0:
                self.tirsbonus3_liste.remove(tirsbonus3) 
   
    def vaisseau_deplacement(self):# mouvement du vaisseau
        
        if pyxel.btn(pyxel.KEY_D) and self.vaisseau_x<120:
            self.vaisseau_x += 3 # touche du clavier pour aller à droite (D)
        
        if pyxel.btn(pyxel.KEY_Q) and self.vaisseau_x>0:
            self.vaisseau_x += -3 # touche du clavier pour aller à gauche (Q)
            
        if pyxel.btn(pyxel.KEY_S ) and self.vaisseau_y<120:
            self.vaisseau_y += 3 # touche du clavier pour aller vers le bas (S)
            
        if pyxel.btn(pyxel.KEY_Z ) and self.vaisseau_y>0:
            self.vaisseau_y += -3 # touche du clavier pour aller vers le haut (Z)
  
    def tirs_creation(self):
       
       if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.bonus_active == False:
           self.tirs_liste.append([self.vaisseau_x+4, self.vaisseau_y-4]) # touche pour tirer (clique gauche)
    
    def tirs_deplacement(self):
        for tir in self.tirs_liste:
            tir[1] -= 1
            if tir[1]<0:
                self.tirs_liste.remove(tir) # comment se déplacent les tirs (vers le haut)
    
    def meteors_creation(self) :
        if (pyxel.frame_count % 250 == 0): 
            self.meteors_liste.append([random.randint(0, 120),0])
              
    
    def meteors_deplacement(self) :
            for meteors in self.meteors_liste:
                meteors[1] += 1
                meteors[0] -= 1
                if meteors[1]>128 or meteors[0]<0:
                    self.meteors_liste.remove(meteors)
               
    
    def ennemis_creation(self):
        if (pyxel.frame_count % 10 == 0):
            self.ennemis_liste.append([random.randint(0, 120), 0]) # comment se craient les ennemis (1 par seconde)
    
    def ennemis_deplacement(self): 
           for ennemi in self.ennemis_liste:
            ennemi[1] += 1
            if  ennemi[1]>128:
                self.ennemis_liste.remove(ennemi) # comment se déplacent les ennemis (vers le bas)
  
    
    def vaisseau_suppression(self):   
        for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+12 and ennemi[1] <= self.vaisseau_y+22 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                    self.ennemis_liste.remove(ennemi)
                    self.vies -= 1 # moins une vie quand le vaisseau touche un ennemies
                    self.bonus_active = False
        for meteors in self.meteors_liste:
            if meteors[0] <= self.vaisseau_x+12 and meteors[1] <= self.vaisseau_y+22 and meteors[0]+16 >= self.vaisseau_x and meteors[1]+16 >= self.vaisseau_y:
                self.meteors_liste.remove(meteors) 
                self.vies -= 100000000
    
    def ennemis_suppression(self):
        for ennemi in self.ennemis_liste:
            if self.bonus_active == True:
                for tirsbonus in self.tirsbonus_liste:
                    if ennemi[0] <= tirsbonus[0]+7 and ennemi[0]+12 >= tirsbonus[0] and ennemi[1]+12 >= tirsbonus[1] and ennemi in self.ennemis_liste:   
                        self.ennemis_liste.remove(ennemi)
                        self.tirsbonus_liste.remove(tirsbonus)
                        self.explosions_creation(ennemi[0], ennemi[1])
                        self.score += 1
                        pyxel.play(0, 6)
                
                for tirsbonus in self.tirsbonus2_liste:
                    if ennemi[0] <= tirsbonus[0]+7 and ennemi[0]+12 >= tirsbonus[0] and ennemi[1]+12 >= tirsbonus[1] and ennemi in self.ennemis_liste:    
                        self.ennemis_liste.remove(ennemi)
                        self.tirsbonus2_liste.remove(tirsbonus)
                        self.explosions_creation(ennemi[0], ennemi[1])
                        self.score += 1
                        pyxel.play(0, 6)

                for tirsbonus in self.tirsbonus3_liste:
                    if ennemi[0] <= tirsbonus[0]+7 and ennemi[0]+12 >= tirsbonus[0] and ennemi[1]+12 >= tirsbonus[1] and ennemi in self.ennemis_liste:    
                        self.ennemis_liste.remove(ennemi)
                        self.tirsbonus3_liste.remove(tirsbonus)
                        self.explosions_creation(ennemi[0], ennemi[1])
                        self.score += 1
                        pyxel.play(0, 6)
           
            else:
                for tir in self.tirs_liste:
                    if ennemi[0] <= tir[0]+6 and ennemi[0]+12 >= tir[0] and ennemi[1]+12 >= tir[1]: 
                        self.ennemis_liste.remove(ennemi)
                        self.tirs_liste.remove(tir)
                        self.explosions_creation(ennemi[0], ennemi[1])
                        self.score += 1 # quand les ennemis doivent se détruire (quand ils sont touché par un tirs) et prendre plus 1 au score
                        pyxel.play(0, 6)
    
    def explosions_creation(self, x, y):
        self.explosions_liste.append([x, y, 0]) # comment se craient les explosion 
        
    def explosions_animation(self):
        for explosion in self.explosions_liste:
            explosion[2] +=1
            if explosion[2] == 12:
                self.explosions_liste.remove(explosion) # animation des explosion  
    
    def update(self):
        
        self.vaisseau_deplacement()
        self.tirs_creation()
        self.tirs_deplacement()
        self.ennemis_creation()
        self.ennemis_deplacement()
        self.ennemis_suppression()
        self.vaisseau_suppression()
        self.explosions_animation() # L79 à L87 c les mise à jours
        self.meteors_creation()
        self.meteors_deplacement()
        self.bonus_creation()
        self.bonus_deplacement()
        self.tirsbonus_creation()
        self.tirsbonus_deplacement()
        self.bonus_deplacement()
        self.tirsbonus2_deplacement()
        self.tirsbonus3_deplacement()
        self.tirsbonus2_creation()
        self.tirsbonus3_creation()
        self.bonus_activation()
        self.coeursbonus_creation()
        self.coeursbonus_deplacement()
        self.coeursbonus_activation()
        if pyxel.btnp(pyxel.KEY_Y):
            pyxel.quit()
        if self.vies <= 0:
            if not self.audiogameover:
                pyxel.play(0, 3) 
                self.audiogameover = True
    
    def draw(self): # les dessin
        pyxel.cls(0)
        
        if self.score > 0:
            nombre_de_caractere = len(str(self.score))
            pyxel.text(115 - nombre_de_caractere * 4,8, ':'+ str(self.score), 7) # le texte du score
            pyxel.blt(105 - nombre_de_caractere * 4,5, 0, 16, 40, 8, 8)
        
        if self.vies > 0:
            pyxel.text(15,8, ':'+ str(self.vies), 7)
            pyxel.blt(5,5, 0, 8, 8, 8, 8) # le texte de la vie
            
            pyxel.blt(self.vaisseau_x, self.vaisseau_y, 0, 0, 32, 16, 24) # le dessin du vaisseau
        
            for tir in self.tirs_liste:
               pyxel.blt(tir[0], tir[1], 0, 8, 0, 8, 8, scale = 0.5) # le dessin des tirs
            
            for meteor in self.meteors_liste:
                pyxel.blt(meteor[0], meteor[1], 0, 48, 32, 16, 16)
            
            for ennemi in self.ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0, 8, 96, 16, 16) # le dessin des ennemis
            
            for explosion in self.explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3) # le dessin des explosion
            
            for bonus in self.bonus_liste:
                pyxel.blt(bonus[0], bonus[1], 0, 32, 32, 8, 8)
            
            for tirsbonus in self.tirsbonus_liste:
                pyxel.blt(tirsbonus[0], tirsbonus[1], 0, 40, 32, 8, 16, rotate = 45)
            
            for tirsbonus2 in self.tirsbonus2_liste:
                pyxel.blt(tirsbonus2[0], tirsbonus2[1], 0, 40, 32, 8, 16, rotate = -45)
            
            
            for tirsbonus3 in self.tirsbonus3_liste:
                pyxel.blt(tirsbonus3[0], tirsbonus3[1], 0, 40, 32, 8, 16)
        
            for coeursbonus in self.coeursbonus_liste:
                pyxel.blt(coeursbonus[0], coeursbonus[1], 0, 8, 8, 8, 8 )
        
        else:  
            
            pyxel.text(45,64, 'GAME OVER', 7) # afficher le texte game over à la fin de la partie)
            
           

Jeu()