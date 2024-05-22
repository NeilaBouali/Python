# Exerice1
# Tables de multiplication à générer
tables = [1, 2, 3, 5, 8]

# Génération des tables de multiplication
resultats_tables = [[table * i for i in range(1, 11)] for table in tables]

# Affichage des résultats
for i, table in enumerate(tables):
    print(f"Table de multiplication de {table}: {resultats_tables[i]}")

#Autre Méthode avec Map()
tables = [1, 2, 3, 5, 8]
def myfunc(a):
  return [a * i for i in range(11)]

x = map(myfunc,tables)
#convert the map into a list, for readability:
print(list(x))


# Exercice2
'''tables = [5]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Génération des tables de multiplication
resultats_tables = [5 * i for i in range(1, 11)]

# Affichage des résultats
for i in list1:
   print(f"5x{i}={resultats_tables[i-1]}")
''''''
'''
# Exercice3

'''
# Création d'une liste pour la table de multiplication par 5 avec une boucle while
table_de_5_while = []
i = 1
while True:
    resultat = 5 * i
    table_de_5_while.append(f"5 x {i} = {resultat}")
    i += 1
    if i > 10:
        break

# Affichage des résultats
for ligne in table_de_5_while:
    print(ligne)
'''
#Exercice4
# Création de l'objet avec les valeurs initiales
obj = {"a": 42, "b": 42, "c": 42, "d": 42}

# Initialisation de l'accumulateur
accumulateur = 1

# Parcours de chaque clé de l'objet
for key in obj:
    if key == 'd':
        accumulateur -= obj[key]
    else:
        accumulateur *= obj[key]

# Affichage du résultat final
print(accumulateur)  # Devrait afficher 74046


#Exercice5
    
# Initialisation de la liste pour stocker les lignes du motif
motif = []

# Génération du motif en utilisant des boucles imbriquées
for i in range(1, 6):  # La boucle extérieure gère les lignes (de 1 à 5)
    ligne = " "
    for j in range(i):  # La boucle intérieure génère les étoiles par ligne
        ligne += "*" 
    motif.append(ligne)  # Ajout de la ligne à la liste

# Affichage du motif
print(" ".join(motif))

#Autre méthode avec Map()
tables ="*"
def myfunc(a):
  return [a * i for i in range(1,6)for j in range(1)]

x = map(myfunc,tables)
#convert the map into a list, for readability:
print(list(x))

print(' ' .join(list(map(lambda x:x*"*", range (1,6))))) 

#lambda appelle une autre fonction lambda arguments : expression
#Ajoutez 10 à l'argument a et renvoyez le résultat :

#x = lambda a : a + 10
#print(x(5))

#Exercice6
# Initialisation du tableau
nbr = [5, 5, 6, 2, 1]

# Implémentation du tri à bulles
for i in range(len(nbr)):
    for j in range(0, len(nbr) - i - 1):
        if nbr[j] > nbr[j + 1]:
            # Échange des éléments si nécessaire
            nbr[j], nbr[j + 1] = nbr[j + 1], nbr[j]

# Affichage du tableau trié
print(nbr)

#Exercice7
from datetime import datetime

# Obtenir l'année actuelle
annee_actuelle = datetime.now().year

# Créer une liste des années de 1980 à l'année actuelle
liste_annees = [annee for annee in range(1980, annee_actuelle + 1)]

# Afficher la liste des années
print(liste_annees)

#Exerice8
for i in range(1,10):
    print('1'*i)
    
#Exerice9
for i in range(1,10):
    motif'[