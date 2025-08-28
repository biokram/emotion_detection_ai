'''
Module contains a Flask application for emotion detection using Watson NLP API.
It provides a web interface and an API endpoint for analyzing emotions in text.
'''
#Import dependecies
from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector", methods = ['POST'])
def emote_detector():
    
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    e_response = emotion_detector(text_to_analyze)

    if emotion_response['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    formatted_message = (
            f"For the given statement, the system response is 'anger': "
            f"{e_response['anger']}, 'disgust': {e_response['disgust']}, "
            f"'fear': {e_response['fear']}, 'joy': {e_response['joy']} "
            f"and 'sadness': {e_response['sadness']}. The dominant emotion is "
            f"{e_response['dominant_emotion']}."
        )
        
    return jsonify({'message': formatted_message, 'details': response})


if __name__ == "__main__":
    ''' 
    This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)