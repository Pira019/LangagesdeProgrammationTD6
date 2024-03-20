import sys

# Définir une fonction génératrice pour générer les n premiers nombres pairs
def generate_even_numbers(n):
    count = 0
    while count < n:
        yield count * 2
        count += 1

# Créer un générateur pour les 1000 premiers nombres pairs
even_generator = generate_even_numbers(1000)
print(next(even_generator))
print(next(even_generator))
print(next(even_generator))
# Mesurer la taille du générateur
size_of_generator = sys.getsizeof(even_generator)
print("Taille du générateur:", size_of_generator, "octets")

# Créer une liste contenant les mêmes 1000 premiers nombres pairs
even_list = list(generate_even_numbers(1000))

# Mesurer la taille de la liste
size_of_list = sys.getsizeof(even_list)
print("Taille de la liste:", size_of_list, "octets")
