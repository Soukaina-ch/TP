def compter_mots_python(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            # Compte le nombre de fois que "python" apparaît (en minuscules)
            compteur = contenu.lower().count("python")
            return compteur
    except FileNotFoundError:
        return None

def main():
    essais_max = 3
    essais = 0

    while essais < essais_max:
        nom_fichier = input("Veuillez entrer le nom du fichier (avec .txt) : ")
        compteur = compter_mots_python(nom_fichier)

        if compteur is not None:
            print(f"Le mot 'python' apparaît {compteur} fois dans le fichier '{nom_fichier}'.")
            break  # Sortir de la boucle si le fichier a été lu avec succès
        else:
            essais += 1
            print(f"Erreur : le fichier '{nom_fichier}' n'a pas été trouvé. Essayez encore.")

    if essais == essais_max:
        print("Vous avez atteint le nombre maximum d'essais. Le programme va quitter.")

if __name__ == "__main__":
    main()
