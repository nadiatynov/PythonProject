#len(final_mdp) >= 12
#En python les import doivent être rangés deans l'ordre alphabétique(on regarde la 1ère lettre de l'import)

import random
import string

choice = input("Quelle longueur voulez-vous pour votre mot de passe? ")

mdp = []

#string.ascii_uppercase renvoie une chaine de caractères avec toutes les lettres de l'alphabet en majuscule
#string.ascii_lowercase fait pareil à la diff que les lettres sont en miniscule
#string.digits renvoie une chaine de caractère contenant les chiffres de 0 à 9
#string.punctuation renvoie une chaine de caractères avec tous les caractères spéciaux 
#random.choice() permet de choisir aléatoirement un élément dans une liste 

Maj = random.choice(string.ascii_uppercase)
Min = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special_char = random.choice(string.punctuation)

mdp.extend([Maj,Min,digit,special_char])

random.shuffle(mdp) #random.shuffle() permet de mélanger une liste sur place de façon aléatoire

final_mdp = ''.join(mdp)

choice = input("Quelle longueur voulez-vous pour votre mot de passe: ")

print("--- Générateur de Mot de Passe Certifié ---")

print(f"Votre mot de passe sécurisé: {final_mdp}")