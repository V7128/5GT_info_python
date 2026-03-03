

class Chaise():
    def __init__(self):
        self.materiau=""
        self.prix=int()
        self.hauteur=float()
        self.largeur=float()
        self.profondeur=float()
        self.couleur=""
        self.poids=int()
        self.surface= float()
    #self pour determiner que c'es l'attribut de la classe, sans quoi on ne peut pas appeler les attributs depuis l'exterieur de la classe
    # = pour le matériau de la chaise vaut, on parle des diff variables depuis l'interieur de la classe
    
    def calc_surface(self):
        self.surface=self.largeur*self.profondeur
        
        
chaise=Chaise() #instanciation de la classe chaise
chaise.materiau="bois"
chaise.prix=160
chaise.hauteur=0.8
chaise.profondeur=0.5
chaise.largeur=0.4

chaise.calc_surface()
