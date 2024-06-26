# Exerice1
def myPutStr(string):
    if isinstance(string, (int, float)):
        return "et pourquoi pas 42 ?"
    else:
        return string


# Test de la fonction
print(myPutStr("Hello"))  # Devrait afficher: Hello World
print(myPutStr(657565))  # Devrait afficher: et pourquoi pas 42 ?


# Autre méthode sans  isinstance
def myPutStr(string):
    try:
        # conversion en entier ou flottant
        float(string)
        #conversion réussit, c'est un nombre
        return "et pourquoi pas 42 ?"
    except ValueError:
        #conversion échoue, ce n'est pas un nombre
        return string


# Test de la fonction
print(myPutStr("Hello World"))  # Devrait afficher: Hello World
print(myPutStr("123"))  # Devrait afficher: et pourquoi pas 42 ?


# Exerice2
# Créer une fonction “computeSurfaceM2” qui calcule une surface en m² carré. Type de résultat attendu :  “Votre surface et de 200 m2”

def computeSurfaceM2(longueur, largeur): 
    surface=longueur*largeur
    return f"Votre surface est de {surface} m2!"

print(computeSurfaceM2(10,20))

# Exerice 3
# Créer une fonction “detectMyAgeByNight” capable d’implémenter votre précédent script de la boîte de nuit <
# et de faire entrer dans une boîte de nuit une personne ayant plus de 18 ans et refusant celles qui ont entre 0 et 17.

#
'''
age = int(input("Ton age: "))
def detectMyAgeByNight(age):
    # Demander l'âge de l'utilisateur
     # Vérifier l'âge et afficher le message approprié
    if age < 18:
             return(f"Vous ne pouvez pas entrer, vous n'êtes pas majeur, vous avez {age} ans.") #pas de besoin de else pour une condition uniquement deux return
    return(f"Vous pouvez entrer, vous êtes majeur, vous avez {age} ans.")

# Appeler la fonction pour tester
print(detectMyAgeByNight(age))
'''
# Exerice 4
"""Faite en sorte de créer une fonction “tableGenerator” capable de générer un tableau matriciel avec des “|” et des ”-”  d’après une liste python à plusieurs dimensions. 
Se tableau devra obligatoirement comprendre des titres pour chaque colonnes même vide et des valeurs même si vide. 
Appuyez-vous sur la structure de votre liste pour reproduire votre tableau à l’identique dans votre console."""

table = [
    ["", "Test1", "Test2", "Test3"],
    ["Data1", "1", "2", "3.33"],
    ["Data2", "3", "2", "1"],
    ["Data3", "6.7", "4", "2"],
]


def max_taille(table):
    if not table or not table[0]:
        return 0
    return max(len(column) for column in zip(*table))


table = [[1, 2, 3], [4, 5, 6], [7, 8]]
print(max_taille(table)) 


def tableGenerator(table):
    for i, row in enumerate(table):
        rowStr = ""

        for j, col in enumerate(row):
            rowStr += f"|{col}"
        if not i:
            print({max_taille}*" -")
        print(f"{rowStr}|")

print(tableGenerator(table))

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

# exercice 7
