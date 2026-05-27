"""
Server module for the Emotion Detection application.
Provides routes to render the user interface and process emotion analysis requests.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Ruta para procesar el texto enviado desde el frontend,
    incorporando el manejo de errores para entradas inválidas o vacías.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Verificar si la emoción dominante es None (caso de error 400)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extraer los datos si la respuesta es válida
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Ruta raíz para renderizar la interfaz de usuario.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
