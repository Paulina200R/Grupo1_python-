import random

#Diccionario con preguntas y respuestas
preguntas = {
    "¿Cuál es la capital de Australia?": "canberra",
    "¿Cuál es el rio mas largo del mundo?": "Nilo",
    "¿En qué continente se encuentra el Monte Everest?": "Asia",
    #Agregar mas Preguntas aqui
} 

# parte lisandro
for pregunta, respuesta in preguntas_aleatorias:
    print(pregunta)
    respuesta_usuario = input("Tu respuesta: ")
    
    if respuesta_usuario.lower() == respuesta.lower():
        print("¡Correcto!")
        puntaje += 1
    else: