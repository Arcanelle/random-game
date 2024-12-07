import random
#Niveau de difficulté
A = int(input('Quel niveau de diffuclté choisissez vous (1, 2 ou 3)? '))

if A == 1 : 
# le programme tire un nombre aléatoire entre 1 et 10
    secret = (random.randint(1,10))

# La personne propose des solutions et le programme indique si c'est plus ou c'est moins
    user_number = int(input('Essayez de trouver le nombre tiré au sort par la machine entre 1 et 10 ! '))
    attempts = 1
    
    while secret != user_number :
        if secret < user_number :
            print("C'est plus petit...")
        else:
            print("C'est plus grand...")   
             
        user_number = int(input('Essayez de trouver le nombre tiré au sort par la machine entre 1 et 10 ! '))
        attempts = attempts + 1
    
    print(f'Bravo, vous avez trouvé le nombre {secret} en {attempts} essais ! ')
    
        
elif A == 2 :
# le programme tire un nombre aléatoire entre 1 et 100
    secret = (random.randint(1,100))

# La personne propose des solutions et le programme indique si c'est plus ou c'est moins
    user_number = int(input('Essayez de trouver le nombre tiré au sort par la machine entre 1 et 100 ! '))
    attempts = 1
    
    while secret != user_number :
        if secret < user_number :
            print("C'est plus petit...")
        else:
            print("C'est plus grand...")   
             
        user_number = int(input('Essayez de trouver le nombre tiré au sort par la machine entre 1 et 100 ! '))
        attempts = attempts + 1
    
    print(f'Bravo, vous avez trouvé le nombre {secret} en {attempts} essais ! ')


elif A == 3 :  
# le programme tire un nombre aléatoire entre 1 et 1000
    secret = (random.randint(1,1000))

# La personne propose des solutions et le programme indique si c'est plus ou c'est moins
    user_number = int(input('Essayez de trouver le nombre tiré au sort par la machine entre 1 et 1000 ! '))
    attempts = 1
    
    while secret != user_number :
        if secret < user_number :
            print("C'est plus petit...")
        else:
            print("C'est plus grand...")   
             
        user_number = int(input('Essayez de trouver le nombre tiré au sort par la machine entre 1 et 1000 ! '))
        attempts = attempts + 1
    
    print(f'Bravo, vous avez trouvé le nombre {secret} en {attempts} essais ! ')

else:
    print("Vous n'avez pas saisi le niveau correctement.")
