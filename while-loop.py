import random 


print("Bienvenido a Adivina el Número \n")
print("las reglas son simples. pensare en un numero e intentaras adivinarlo")
numero = random.randint(1,10) 
escorrecto=False

while escorrecto != True:
    resultado=input("Adivina un numero entre 1 y 10 \n")
    if int(resultado) == numero:
     print("adivinaste correctamente el numero {}".format(resultado))
    escorrecto=True 
else:
    print("El numero no es: {}".format(resultado))
    


    
         
        
    



