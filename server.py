"""
Flask Web App for Emotion Detection using IBM Watson API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """
    API route to detect emotion from text input.

    Returns:
        str: Emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    result = response['dominant_emotion']

    if result is None:
        return "Invalid text! Try again."
    else:
        return "For the given statement, the system response is {}: {}.".format(result, response)

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)     
