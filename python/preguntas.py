import random
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Diccionario con preguntas y respuestas
preguntas = {
    "¿Cuál es la capital de Australia?": "canberra",
    "¿Cuál es el río más largo del mundo?": "Nilo",
    "¿En qué continente se encuentra el Monte Everest?": "Asia",
    # Agregar más Preguntas aquí
} 

# Mezclar el orden de las preguntas
preguntas_aleatorias = list(preguntas.items())
random.shuffle(preguntas_aleatorias)

puntaje = 0 

# Parte del cuestionario
for pregunta, respuesta in preguntas_aleatorias:
    print(Fore.CYAN + Style.BRIGHT + pregunta)  # Pregunta en color cian y en negrita
    respuesta_usuario = input(Fore.GREEN + "Tu respuesta: " + Style.RESET_ALL)
    
    if respuesta_usuario.lower() == respuesta.lower():
        print(Fore.GREEN + "¡Correcto!" + Style.RESET_ALL)
        puntaje += 1
    else:
        print(Fore.RED + f"Incorrecto. La respuesta correcta era: {respuesta}" + Style.RESET_ALL)

print(Fore.YELLOW + Style.BRIGHT + f"¡Felicidades! Tu puntaje final es: {puntaje}" + Style.RESET_ALL)
