import random as r

class Penduclass:
    liste_mots = ("comme", "entre", "cette", "etait", "apres", "paris", "aussi", "alors", "ainsi", 
                  "ville", "notes", "trois", "monde", "annee", "titre", "avant", "deces", "serie", 
                  "premier", "commune", "famille", "general", "devient", "nouveau", "pendant", 
                  "village", "periode", "origine", "dernier")

    def __init__(self):
        self.mot = self.choix_du_mot()
        self.lettres_trouvees = set()
        self.tentatives_max = 8
        self.tentatives = 0
        self.lettre_echec = "FIN DU JEU"
    
    def choix_du_mot(self):
        return r.choice(self.liste_mots)
    
    def afficher_mot(self):
        mot_affiche = []
        for i, charactère in enumerate(self.mot):
            if charactère in self.lettres_trouvees or i == 0:
                mot_affiche.append(charactère)
            else:
                mot_affiche.append("_")
        print("Mot à deviner :", "".join(mot_affiche))
        return mot_affiche
    
    def afficher_progression_echec(self):
        # Affiche la partie du message "FIN DU JEU" selon le nombre de tentatives
        print("Lettre d'échec :", self.lettre_echec[:self.tentatives])

    def jouer(self):
        print("Bienvenue au jeu du pendu !")
        
        while self.tentatives < self.tentatives_max and "_" in self.afficher_mot():
            lettre = input("Veuillez rentrer une lettre : \n").lower()
            
            if lettre.isalpha() and len(lettre) == 1:
                if lettre in self.lettres_trouvees:
                    print("Vous avez déjà tenté cette lettre.\n")
                elif lettre in self.mot:
                    self.lettres_trouvees.add(lettre)
                    print("Bien joué ! La lettre est dans le mot.\n")
                else:
                    self.lettres_trouvees.add(lettre)
                    print("Dommage, la lettre n'est pas dans le mot.\n")
                    self.tentatives += 1
                    self.afficher_progression_echec()  # Affiche la progression de "FIN DU JEU"
            else:
                print("Veuillez entrer une seule lettre valide.\n")
            
            self.afficher_mot()
            print("\nNombre d'erreurs restantes :", self.tentatives_max - self.tentatives)
        
        if "_" not in self.afficher_mot():
            print("Félicitations, vous avez deviné le mot :", self.mot)
        else:
            print("Vous avez perdu ! Le mot était :", self.mot)
            print("FIN DU JEU")