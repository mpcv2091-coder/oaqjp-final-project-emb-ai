import requests
import json

def emotion_detector(text_to_analyze):
    # URL de la API de Watson Emotion Predict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos por la API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Estructura JSON de entrada con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Enviar la solicitud POST a la API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convertir la respuesta de texto (JSON) a un diccionario de Python
    formatted_response = json.loads(response.text)
    
    # Extraer el diccionario de emociones que viene dentro de la respuesta de Watson
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extraer los puntajes individuales de cada emoción requerida
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Diccionario con las emociones y sus puntajes para facilitar la búsqueda del mayor
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Lógica para encontrar la emoción dominante (la que tiene el puntaje más alto)
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # Agregar la emoción dominante al diccionario final de salida
    emotions_dict['dominant_emotion'] = dominant_emotion
    
    # Retornar el formato exacto solicitado por IBM
    return emotions_dict