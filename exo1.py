import random

def jeu_de_deviner():
    # L'ordinateur choisit un nombre aléatoire entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)
    essais = 0
    trouve = False
    
    print("Bienvenue au jeu de devinette !")
    print("L'ordinateur a choisi un nombre entre 1 et 100.")
    
    while not trouve:
        # L'utilisateur propose un nombre
        try:
            proposition = int(input("Devinez le nombre : "))
            essais += 1
            
            if proposition < nombre_a_deviner:
                print("Trop petit ! Essayez encore.")
            elif proposition > nombre_a_deviner:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Félicitations ! Vous avez trouvé le nombre {nombre_a_deviner} en {essais} essais.")
                trouve = True
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Lancer le jeu
jeu_de_deviner()