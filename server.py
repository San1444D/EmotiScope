"""
This module is the main flask file to run the server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    This function return index.html to clients as response
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    """
    This endpoint get text and run emotion detection and return a response
    """
    text = request.args.get('textToAnalyze')
    res = emotion_detector(text)
    if not res['dominant_emotion']:
        return "Invalid text! Please try again!."
    return res

app.run(host='0.0.0.0', port="5000")
