from ahorcado import ahorcado 
from adivina import adivina_el_numero_computadora


print(
    "1. Jugar ahorcado \n"
    "2. Jugar adivinanza  "
)

operacion=int(input(">>>"))
if operacion == 1:
    ahorcado()

elif operacion == 2:
    limiteSuperior = input(f"Elegi el limite superior del juego: ")
    print(limiteSuperior)
    adivina_el_numero_computadora(int(limiteSuperior))
#    adivina_el_numero_computadora()

    
