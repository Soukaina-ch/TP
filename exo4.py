def harmonic_sum(n):
    # Vérification que n est strictement positif
    if n <= 0:
        raise ValueError("Le nombre doit être strictement positif.")
    
    # Cas de base : si n est 1, la somme est simplement 1
    if n == 1:
        return 1
    else:
        # Récursion : 1/n + somme des n-1 termes
        return 1/n + harmonic_sum(n-1)

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        n = 4  # Vous pouvez changer ce nombre pour tester d'autres valeurs
        result = harmonic_sum(n)
        print(f"La somme harmonique jusqu'au {n}-ième terme est : {result}")
    except ValueError as e:
        print(e)
