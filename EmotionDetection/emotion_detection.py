import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 400 or not text_to_analyze.strip(): 
        raise ValueError("Invalid input! Please try again.")

    formatted_response = json.loads(response.text)
    
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    result = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
    
    return result
