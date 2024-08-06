import random







# parte lisandro
for pregunta, respuesta in preguntas_aleatorias:
    print(pregunta)
    respuesta_usuario = input("Tu respuesta: ")
    
    if respuesta_usuario.lower() == respuesta.lower():
        print("¡Correcto!")
        puntaje += 1
    else:
