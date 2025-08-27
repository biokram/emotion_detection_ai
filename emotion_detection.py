"""
Module designed to detect emotion from user input
"""
#Import required dependecies
import requests
import json 

def emotion_detector(text_to_analyse):
    """
    Function to detect emotion from user input.
    """
    #Emotion Predict function part of Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #Header information for model
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #JSON format
    myobj = {"raw_document": { "text": text_to_analyse }}
    
    #stores the information for further processing
    response = requests.post(url, json = myobj, headers=header)
    
    #Stores and formats the returned information for readability
    formatted_response = json.loads(response.text)
    
    #Upon success code, gets emotions
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        return {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    
    #Error handling statement for unsuccessful response
    elif response.status_code == 400:
         return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    #Prints error
    else:
        print(f"Error: {response.status_code}")
        return None