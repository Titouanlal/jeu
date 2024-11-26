import pyxel, random #import c'est pour prendre des codes déjà fais pur les utiliser

class Jeu:

    def __init__(self):# quand le jeu commence
        
        pyxel.init(128, 128, title="Nuit du c0de")# c'est la taille et le titre de la page
        self.score = 0 # le score au début du jeu
        self.vaisseau_x = 60 # l'endroit où le vaisseau vas apparaitre pour x
        self.vaisseau_y = 60 # l'endroit où le vaisseau vas apparaitre pour y
        self.vies = 5 # le nombre d vie au début du jeu
        self.tirs_liste = [] # la liste des tirs
        self.ennemis_liste = [] # la liste des ennemis
        self.explosions_liste = [] # la liste des explosions
        
        pyxel.load("titouan.pyxres") # le nom du fichier où il doit chercher les dessin
         
        pyxel.run(self.update, self.draw)
        
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
       
       if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
           self.tirs_liste.append([self.vaisseau_x+2, self.vaisseau_y-4]) # touche pour tirer (clique gauche)
    
    def tirs_deplacement(self):
        for tir in self.tirs_liste:
            tir[1] -= 1
            if tir[1]<-8:
                self.tirs_liste.remove(tir) # comment se déplacent les tirs (vers le haut)
                
    def ennemis_creation(self):
        if (pyxel.frame_count % 30 == 0):
            self.ennemis_liste.append([random.randint(0, 120), 0]) # comment se craient les ennemis (1 par seconde)
    
    def ennemis_deplacement(self): 
           for ennemi in self.ennemis_liste:
            ennemi[1] += 1
            if  ennemi[1]>128:
                self.ennemis_liste.remove(ennemi) # comment se déplacent les ennemis (vers le bas)
     
    def vaisseau_suppression(self):   
      for ennemi in self.ennemis_liste:
            if ennemi[0] <= self.vaisseau_x+8 and ennemi[1] <= self.vaisseau_y+8 and ennemi[0]+8 >= self.vaisseau_x and ennemi[1]+8 >= self.vaisseau_y:
                self.ennemis_liste.remove(ennemi)
                self.vies -= 1 # quand le vaisseau doit se détruire (quand il n'a plus de vie)
                
    def ennemis_suppression(self):
        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if ennemi[0] <= tir[0]+2 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                    self.ennemis_liste.remove(ennemi)
                    self.tirs_liste.remove(tir)
                    self.explosions_creation(ennemi[0], ennemi[1])
                    self.score += 1 # quand les ennemis doivent se détruire (quand ils sont touché par un tirs) et prendre plus 1 au score
                    
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
         
    def draw(self): # les dessin
        pyxel.cls(0)
        if self.score > 0:
            nombre_de_caractere = len(str(self.score))
            pyxel.text(115 - nombre_de_caractere * 4,8, ':'+ str(self.score), 7) # le texte du score
            pyxel.blt(105 - nombre_de_caractere * 4,5, 0, 16, 40, 8, 8)
        if self.vies > 0:
            pyxel.text(15,8, ':'+ str(self.vies), 7)
            pyxel.blt(5,5, 0, 8, 8, 8, 8) # le texte de la vie
            
            pyxel.blt(self.vaisseau_x, self.vaisseau_y, 0, 0, 0, 8, 8) # le dessin du vaisseau
        
            for tir in self.tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 8, 0, 8, 8) # le dessin des tirs
            
            for ennemi in self.ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1], 0, 0, 8, 8, 8) # le dessin des ennemis
            
            for explosion in self.explosions_liste:
                pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3) # le dessin des explosion
        else:  
            
            pyxel.text(50,64, 'GAME OVER', 7) # afficher le texte game over à la fin de la partie
Jeu()