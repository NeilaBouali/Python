# Exerice 1:
"""age = int(input("Ton age:"))
if age<18:
    print("Vous ne pouvez pas entrer vous n'êtes pas majeur vous avez " ,age)
elif 18<age<42: 
    print("Vous pouvez entrer vous êtes majeur vous avez ", age)
else: 
    print("Tu es le PATRON")"""

# Exercice 2 :
import random
temp=random.randrange(0, 30)
print(temp)
# temp=int(input("Donnez une température : "))
if 0<temp<=10:
    print("Cool")
elif 11<=temp<=20:
    print("Tepid")
else:
    print("Warm")

#Exerice 3:
import datetime

jour_actuel = datetime.datetime.now().strftime("%A")
match jour_actuel:
    case "Monday":
        print(f"Nous sommes Lundi")
    case "Tuesday":
        print(f"Nous sommes Mardi")
    case "Wednesday":
        print(f"Nous sommes Mercredi")
    case "Thursday":
        print(f"Nous sommes Jeudi")
    case "Friday":
        print(f"Nous sommes Vendredi")
    case "Saturday":
        print(f"Nous sommes Samedi")
    case "Sunday":
        print(f"Nous sommes Dimanche")
        
# Exerice 4:
print("Hello!")
print("Trois chemins s'offrent à toi. Choisis la bonne voie.")
choix1 = input("Vas-tu à gauche, à droite ou tout droit ? (gauche/droite/avant) ")

if choix1 == "gauche":
    print("Attention !")
    choix2 = input(
        "Veux-tu courir, marcher, ou brûler quelque chose ? (courir/marcher/brûler) "
    )

    if choix2 == "courir":
        print("Tu as décidé de courir.")
        choix3 = input(
            "Tu es tombé sur une boîte, es-tu curieux ? (oui/non/rien faire) "
        )

        if choix3 == "oui":
            print(
                "Tu ouvres la boîte et trouves la grande réponse sur la vie, l’univers et le reste !!"
            )
        elif choix3 == "rien faire":
            print("T'es mort, c'est sûr.")
        else:
            print("Tu choisis de ne pas ouvrir la boîte et continues ton chemin.")

    elif choix2 == "marcher":
        print("Tu as décidé de marcher.")
        choix3 = input(
            "Tu es tombé sur une boîte, es-tu curieux ? (oui/non/regarder autour) "
        )

        if choix3 == "oui":
            print(
                "Tu ouvres la boîte et trouves un trésor. Félicitations, tu es riche !"
            )
        elif choix3 == "regarder autour":
            print("En regardant autour, tu trouves un passage secret !")
        else:
            print("Tu choisis de ne pas ouvrir la boîte et tu meurs.")

    else:
        print("Tu as décidé de brûler quelque chose.")
        choix3 = input("Trouves-tu un objet à brûler ? (oui/non/chercher plus) ")

        if choix3 == "oui":
            print("Tu brûles l'objet et découvres un passage secret.")
        elif choix3 == "chercher plus":
            print("En cherchant plus, tu trouves une carte cachée.")
        else:
            print("Tu ne trouves rien à brûler et continues ton chemin.")

elif choix1 == "droite":
    print("Attention !")
    choix2 = input(
        "Veux-tu courir, marcher, ou brûler quelque chose ? (courir/marcher/brûler) "
    )

    if choix2 == "courir":
        print("Tu as décidé de courir.")
        choix3 = input(
            "Tu es tombé sur une boîte, es-tu curieux ? (oui/non/rien faire) "
        )

        if choix3 == "oui":
            print(
                "Tu ouvres la boîte et trouves la grande réponse sur la vie, l’univers et le reste !!"
            )
        elif choix3 == "rien faire":
            print("T'es mort, c'est sûr.")
        else:
            print("Tu choisis de ne pas ouvrir la boîte et continues ton chemin.")

    elif choix2 == "marcher":
        print("Tu as décidé de marcher.")
        choix3 = input(
            "Tu es tombé sur une boîte, es-tu curieux ? (oui/non/regarder autour) "
        )

        if choix3 == "oui":
            print(
                "Tu ouvres la boîte et trouves un trésor. Félicitations, tu es riche !"
            )
        elif choix3 == "regarder autour":
            print("En regardant autour, tu trouves un passage secret !")
        else:
            print("Tu choisis de ne pas ouvrir la boîte et continues ton chemin.")

    else:
        print("Tu as décidé de brûler quelque chose.")
        choix3 = input("Trouves-tu un objet à brûler ? (oui/non/chercher plus) ")

        if choix3 == "oui":
            print("Tu brûles l'objet et découvres un passage secret.")
        elif choix3 == "chercher plus":
            print("En cherchant plus, tu trouves une carte cachée.")
        else:
            print("Tu ne trouves rien à brûler et continues ton chemin.")

elif choix1 == "avant":
    print("Attention !")
    choix2 = input(
        "Veux-tu courir, marcher, ou brûler quelque chose ? (courir/marcher/brûler) "
    )

    if choix2 == "courir":
        print("Tu as décidé de courir.")
        choix3 = input(
            "Tu es tombé sur une boîte, es-tu curieux ? (oui/non/rien faire) "
        )

        if choix3 == "oui":
            print(
                "Tu ouvres la boîte et trouves la grande réponse sur la vie, l’univers et le reste !!"
            )
        elif choix3 == "rien faire":
            print("T'es mort, c'est sûr.")
        else:
            print("Tu choisis de ne pas ouvrir la boîte et continues ton chemin.")

    elif choix2 == "marcher":
        print("Tu as décidé de marcher.")
        choix3 = input(
            "Tu es tombé sur une boîte, es-tu curieux ? (oui/non/regarder autour) "
        )

        if choix3 == "oui":
            print(
                "Tu ouvres la boîte et trouves un trésor. Félicitations, tu es riche !"
            )
        elif choix3 == "regarder autour":
            print("En regardant autour, tu trouves un passage secret !")
        else:
            print("Tu choisis de ne pas ouvrir la boîte et continues ton chemin.")

    else:
        print("Tu as décidé de brûler quelque chose.")
        choix3 = input("Trouves-tu un objet à brûler ? (oui/non/chercher plus) ")

        if choix3 == "oui":
            print("Tu brûles l'objet et découvres un passage secret.")
        elif choix3 == "chercher plus":
            print("En cherchant plus, tu trouves une carte cachée.")
        else:
            print("La grande réponse sur la vie, l’univers et le reste !")


# Exercice 5:
# Non de la variable qui n'existe pas
ma_variable=2
try:
    resultat = str(ma_variable)  
except NameError:
    resultat = "cette variable n'existe pas"
else:
    resultat = "42"

print(resultat)

# Solution
var = 42
if var == 42:
    print(42)
else:
    print("cette variable n'existe pas")
# Exercice 5:
