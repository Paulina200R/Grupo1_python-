import flet as ft
import random
import time

# Diccionario con preguntas y respuestas
preguntas = {
    "¿Cuál es la capital de Australia?": "Canberra",
    "¿Cuál es el río más largo del mundo?": "Nilo",
    "¿En qué continente se encuentra el Monte Everest?": "Asia",
    # Agrega más preguntas aquí
}

# Mezclar el orden de las preguntas
preguntas_aleatorias = list(preguntas.items())
random.shuffle(preguntas_aleatorias)

class QuizApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Quiz de Preguntas"

        self.puntaje = 0
        self.total_preguntas = len(preguntas_aleatorias)
        self.preguntas_aleatorias = preguntas_aleatorias
        self.pregunta_index = 0
        self.start_time = None

        # Crear los controles de la interfaz
        self.question_label = ft.Text(size=20)
        self.answer_entry = ft.TextField(label="Tu respuesta", keyboard_type=ft.KeyboardType.TEXT)
        self.submit_button = ft.ElevatedButton(text="Enviar", on_click=self.check_answer, width=800, height=35)
        self.resultado = ft.Text(size=20)
        self.imagen_resultado = ft.Image(src="", width=100, height=100)
        self.imagen_final = ft.Image(src="", width=200, height=200)  # Imagen final

        self.page.add(ft.Column(
            controls=[
                self.question_label,
                self.answer_entry,
                self.submit_button,
                self.resultado,
                self.imagen_resultado,
                self.imagen_final  # Agregar imagen final
            ]
        ))

        self.update_question()

    def update_question(self):
        if self.pregunta_index < self.total_preguntas:
            pregunta, _ = self.preguntas_aleatorias[self.pregunta_index]
            self.question_label.value = f"Pregunta {self.pregunta_index + 1}/{self.total_preguntas}: {pregunta}"
            self.answer_entry.value = ""
            self.start_time = time.time()
        else:
            self.show_results()
        self.page.update()

    def check_answer(self, e):
        respuesta_usuario = self.answer_entry.value.strip()
        _, respuesta_correcta = self.preguntas_aleatorias[self.pregunta_index]

        end_time = time.time()
        tiempo_respuesta = end_time - self.start_time

        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.puntaje += 1
            self.resultado.value = "¡Correcto!"
            self.imagen_resultado.src = src="./image/feliz.jpeg"  # URL de la imagen de una cara feliz
        else:
            self.resultado.value = f"Incorrecto. La respuesta correcta era: {respuesta_correcta}"
            self.imagen_resultado.src = "./image/enojado.jpeg"  # URL de la imagen de una cara enojada

        self.pregunta_index += 1
        self.update_question()

    def show_results(self):
        resultado = f"¡Felicidades! Tu puntaje final es: {self.puntaje} de {self.total_preguntas}\n"
        if self.puntaje == self.total_preguntas:
            resultado += "¡Perfecto! ¡Eres un genio!"
            self.imagen_final.src = "https://example.com/great_job.png"  # Imagen para puntaje perfecto
        elif self.puntaje >= self.total_preguntas * 0.7:
            resultado += "¡Muy bien! Tienes buen conocimiento."
            self.imagen_final.src = "https://example.com/well_done.png"  # Imagen para buen desempeño
        elif self.puntaje >= self.total_preguntas * 0.4:
            resultado += "No está mal, pero puedes mejorar."
            self.imagen_final.src = "https://example.com/keep_trying.png"  # Imagen para desempeño medio
        else:
            resultado += "Necesitas estudiar más."
            self.imagen_final.src = "/image/triste.jpeg"  # Imagen para bajo desempeño

        self.resultado.value = resultado
        self.page.update()

ft.app(target=QuizApp)