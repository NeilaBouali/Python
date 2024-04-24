print("My Python Code Forever")
print(
    """My
      Python 
      Code Forever"""
)
var1 = 2
var2 = 3
var3 = "abc"
var4 = 3 + 1
var5 = True
var6 = [5, 5]
var7 = 3.4
var8 = {"name": "Neila"}

my42count = "quarante-deux"
print(len(my42count))


# Variable à vérifier
variable_a_verifier = 23
# Création d'un dictionnaire globals() contenant toutes les variables globales existantes
variables_globales = globals()
# Création de la variable souhaitée en utilisant get() pour obtenir la valeur de la variable si elle existe, sinon la valeur par défaut est 42
nouvelle_variable = variables_globales.get("variable_a_verifier", 42)
print(nouvelle_variable)

myArray42 = list("quarante-deux")
print(myArray42)

# Question 7
myArray42Len = myArray42
print(len(myArray42))

# Question 8
var1 = "La grande réponse sur la vie, l'univers et le reste!"
print(var1)
# recompose le mot dans une variable
myArray42 = "".join(myArray42)
print(myArray42)
myArray42 = myArray42 + var1
print(myArray42)

# Question 9
import random

rand = random.uniform(1, 42)
print(rand)
rand = rand == 42
print(rand)

# Question 10
var1 = 2
var2 = ("&", "2")
var3 = "abc"
var4 = 3 + 1
var5 = True
var6 = [5, 5]
var7 = 3.4
var8 = {"name": "Neila"}
var10 = None
my42Type = True
# my42Type=var1+var2
print(type(my42Type))

# Question 11
compute42 = 7 * 6
print(compute42)

compute42 = str(compute42)
print(compute42)

# Question 12
var1 = "424242"
var1 = var1.replace("42", "quarante-deux")
print(var1)

# Question 13
a = 24
b = 42
print(a, b)
c = a
a = b
b = c
print(a, b)




hdbfvjdgnfghfgh