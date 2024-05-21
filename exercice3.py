# Exerice1
'''# Tables de multiplication à générer
tables = [1, 2, 3, 5, 8]

# Génération des tables de multiplication
resultats_tables = [[table * i for i in range(1, 11)] for table in tables]

# Affichage des résultats
for i, table in enumerate(tables):
    print(f"Table de multiplication de {table}: {resultats_tables[i]}")
'''
# Exercice2
'''tables = [5]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Génération des tables de multiplication
resultats_tables = [5 * i for i in range(1, 11)]

# Affichage des résultats
for i in list1:
    print(f"5x{i}={resultats_tables[i-1]}")
'''
# Exercice3
tables = [5]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Génération des tables de multiplication
resultats_tables = [5 * i for i in range(1, 11)]

# Affichage des résultats
while i<11:
    print(f"5x{i}={resultats_tables[i-1]}")
    i=i+1

    
