# Exerice1
def myPutStr(string):
    if isinstance(string, (int, float)):
        return "et pourquoi pas 42 ?"
    else:
        return string


# Test de la fonction
print(myPutStr("Hello World"))  # Devrait afficher: Hello World
print(myPutStr(123))  # Devrait afficher: et pourquoi pas 42 ?
print(myPutStr(3.14))  # Devrait afficher: et pourquoi pas 42 ?
print(myPutStr("42"))  # Devrait afficher: 42


# Autre méthode sans  isinstance
def myPutStr(string):
    try:
        # Tenter de convertir en entier ou flottant
        float(string)
        # Si la conversion réussit, c'est un nombre
        return "et pourquoi pas 42 ?"
    except ValueError:
        # Si la conversion échoue, ce n'est pas un nombre
        return string


# Test de la fonction
print(myPutStr("Hello World"))  # Devrait afficher: Hello World
print(myPutStr("123"))  # Devrait afficher: et pourquoi pas 42 ?
print(myPutStr("3.14"))  # Devrait afficher: et pourquoi pas 42 ?
print(myPutStr("42"))  # Devrait afficher: et pourquoi pas 42 ?

# Exerice2
# Créer une fonction “computeSurfaceM2” qui calcule une surface en m² carré. Type de résultat attendu :  “Votre surface et de 200 m2”

def computeSurfaceM2(longueur, largeur): 
    surface=longueur*largeur
    return f"Votre surface est de {surface} m2!"

print(computeSurfaceM2(10,20))

# Exerice 3
# Créer une fonction “detectMyAgeByNight” capable d’implémenter votre précédent script de la boîte de nuit <
# et de faire entrer dans une boîte de nuit une personne ayant plus de 18 ans et refusant celles qui ont entre 0 et 17.


def detectMyAgeByNight():
    # Demander l'âge de l'utilisateur
    age = int(input("Ton age: "))

    # Vérifier l'âge et afficher le message approprié
    if age < 18:
        print(
            f"Vous ne pouvez pas entrer, vous n'êtes pas majeur, vous avez {age} ans."
        )
    else:
        print(f"Vous pouvez entrer, vous êtes majeur, vous avez {age} ans.")

# Appeler la fonction pour tester
# detectMyAgeByNight()

# Exerice 4
"""Faite en sorte de créer une fonction “tableGenerator” capable de générer un tableau matriciel avec des “|” et des ”-”  d’après une liste python à plusieurs dimensions. 
Se tableau devra obligatoirement comprendre des titres pour chaque colonnes même vide et des valeurs même si vide. 
Appuyez-vous sur la structure de votre liste pour reproduire votre tableau à l’identique dans votre console."""

test1=[1, 3, 6.7]
test2=[2, 2, 4]
test3=[3.33, 1, 2]


test1=[1, 3, 6.7]
test2=[2, 2, 4]
test3=[3.33, 1, 2]

def tableGenerator(n):
    # Générer la table
    a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]

    # Afficher la table
    for row in a:
        print(" ".join([str(elem) for elem in row]))


# Définir la taille de la table
n = 3


# Appeler la fonction pour générer et afficher la table
tableGenerator(n)

# exercice 5
from datetime import datetime

# Obtenir la date locale actuelle
date_locale_actuelle = datetime.now()

# Afficher la date locale actuelle
print("La date locale actuelle est :", date_locale_actuelle.strftime("%Y-%m-%d %H:%M:%S"))

# Exercice 6
# Faite en sorte de créer une fonction “is_palindrome” qui vérifie si une chaîne de caractère est un palindrome elle devra renvoyer “True” ou “False”
# Initialisation du tableau

def is_palindrome(mot):
    mot = str(mot)
    for i in range(len(mot)//2):
        if mot[i] == mot[-(i + 1)]:
            return True
        else: 
            return False
print(is_palindrome(121))
print(is_palindrome("sjhfbe"))
print(is_palindrome("ababa"))

#exercice 7



