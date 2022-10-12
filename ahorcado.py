
import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras)  


    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("=======================================")
    print("  Ahorcado de la Seleccion Argentina  ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra) 
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()  

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(f"Te quedan {vidas} vidas y usaste estas letras: {' '.join(letras_adivinadas)}")

    
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}") 

        
        letra_usuario = input('Elegi una letra: ').upper()

        
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:
            print("\nYa elegiste esa letra. Elegi otra letra .")
        else:
            print("\nEsta letra no se puede.")

    
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado. Perdiste malo. La palabra era: {palabra}")
    else:
        print(f'Joya mi loco. Adivinaste la palabra {palabra}!')


if __name__ == "__main__":
    ahorcado()

