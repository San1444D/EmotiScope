from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    text = request.args.get('textToAnalyze')
    res = emotion_detector(text)
    return res

app.run(host='0.0.0.0', port="5000")