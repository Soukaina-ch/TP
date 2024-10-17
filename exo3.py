def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

# Exemple
if __name__ == "__main__":
    # Tester la fonction 
    for i in range(1, 20):
        print(i)
        print(fizz_buzz(i))
