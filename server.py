from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Inicializar la aplicación Flask
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Ruta para procesar el texto enviado desde el frontend y
    devolver la respuesta formateada con las puntuaciones de las emociones.
    """
    # Extraer el texto a analizar desde los parámetros de la URL
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Ejecutar la función de detección de emociones
    response = emotion_detector(text_to_analyze)
    
    # Extraer los puntajes e identificación del diccionario de respuesta
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Retornar la cadena de texto con el formato exacto requerido por el cliente
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Ruta raíz para renderizar la página HTML de la interfaz de usuario.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Desplegar la aplicación en el puerto 5000 de localhost
    app.run(host="0.0.0.0", port=5000)