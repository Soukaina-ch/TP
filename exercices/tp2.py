import logging

# Configurer le logging
logging.basicConfig(
    filename='harmonic_sum_log.txt',  # Nom du fichier de log
    level=logging.INFO,                # Niveau de gravité minimum à enregistrer
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format des messages
)

def harmonic_sum(n):
    try:
        # Vérification que n est strictement positif
        if n <= 0:
            raise ValueError("Le nombre doit être strictement positif.")
        
        # Cas de base : si n est 1, la somme est simplement 1
        if n == 1:
            return 1
        else:
            # Récursion : 1/n + somme des n-1 termes
            return 1/n + harmonic_sum(n-1)
    except ValueError as e:
        logging.error(f'Erreur : {e}')
        return None  # Retourne None en cas d'erreur

# Exemple d'utilisation
if __name__ == "__main__":

    logging.info('Début du programme')

    for i in [-1, 0, 1, 4]:  # Test avec plusieurs valeurs
        result = harmonic_sum(i)
        if result is not None:
            print(f"La somme harmonique jusqu'au {i}-ième terme est : {result}")
        else:
            print(f"Erreur dans le calcul pour n={i}.")

    logging.info('Fin du programme')

