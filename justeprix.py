#tirage au sort d'un prix entre 1 et 10 (compris)
import random
cible=random.randint(1,10)

for i in range(1,6):
    #choix du prix du joueur
    try:
        essai = int(input(f"essai n'{i}-prix ?"))
    except:
        print("valeur incorrect....")
        continue
    #message "bravo" si le prix est trouvé
    if cible == essai:
       print("bravo")
       break
    #message "pas assez" si le prix est trop bas
    elif cible > essai :
        print("pas assez")
    #message "trop eleve" si le prix est trop haut
    else:
        print("trop eleve")
#message "perdu" au bout de 5 essais:
if (cible != essai):
   print("perdu")
#fin au bout de 5 essais ou si le prix est touvé