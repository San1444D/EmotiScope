import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=headers)
    print(response.status_code, response.text)
    if response.status_code == 500:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }

    data = response.json()

    # Extract sentiment probabilities
    sentiment = data['documentSentiment']['sentimentMentions'][0]['sentimentprob']
    positive = sentiment.get('positive', 0)
    neutral = sentiment.get('neutral', 0)
    negative = sentiment.get('negative', 0)

    # --- Simple mapping to emotion intensities ---
    anger = negative * 0.6
    disgust = negative * 0.2
    fear = negative * 0.2
    joy = positive
    sadness = neutral * 0.5 + negative * 0.3

    # Determine dominant emotion
    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Formatted response
    formatted_resp = {
        'anger': round(anger, 4),
        'disgust': round(disgust, 4),
        'fear': round(fear, 4),
        'joy': round(joy, 4),
        'sadness': round(sadness, 4),
        'dominant_emotion': dominant_emotion
    }

    return formatted_resp
