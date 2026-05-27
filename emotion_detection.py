import requests

def emotion_detector(text_to_analyze):
    # URL de la API de Watson Emotion Predict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos por la API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Estructura JSON de entrada con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Enviar la solicitud POST a la API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Retornar el atributo de texto (.text) de la respuesta
    return response.text