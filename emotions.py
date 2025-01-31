from flask import Flask, render_template_string, request, jsonify
import random
import spacy
from textblob import TextBlob

# Initialize Flask app
app = Flask(_name_)

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Emotion-based response templates
emotion_templates = {
    "Sadness": [
        "I’m really sorry you're feeling this way. What caused you to feel this way?",
        "I understand that failing exams can be tough. What’s been the hardest part for you?",
        "It’s okay to feel upset about this. We can talk through it and figure out what steps you can take next."
    ],
    "Anxiety": [
        "I hear you. Feeling anxious can be overwhelming. What part of exams or life is making you feel this way?",
        "It's completely normal to feel anxious, but focusing on what you can control might help. Would breaking things down help?",
        "Take a deep breath. What’s causing you to feel anxious about exams or life in general?"
    ],
    "Anger": [
        "I understand that you're feeling angry. What’s been bothering you the most?",
        "It’s okay to feel angry, but finding a way to channel that energy can help. What’s been the source of your anger?",
        "I hear you. Anger is a valid feeling, but let’s talk through it. What’s making you feel this way?"
    ],
    "Loneliness": [
        "I’m sorry you’re feeling lonely. Let’s talk about it. Maybe we can find something that makes you feel connected.",
        "Feeling lonely is tough. Would you like to share more about what's going on in your life right now?",
        "It’s okay to feel lonely, but know that you're not alone. Let’s chat about how we can help you feel more connected."
    ],
    "Stress": [
        "Stress can be overwhelming. Let’s talk about what’s causing this stress. Maybe we can find some ways to handle it.",
        "I understand that stress is tough. Sometimes it helps to break things into smaller pieces. What's the main thing that's causing stress right now?",
        "Take a deep breath. Breaking things into smaller steps might help. Can we start with one thing that’s stressing you out?"
    ],
    "Self-Doubt": [
        "Self-doubt is a common feeling. What’s making you feel uncertain about yourself?",
        "I believe in you! Self-doubt can cloud our judgment, but you’re capable. What’s making you feel unsure?",
        "You’ve accomplished so much. What part of yourself are you doubting right now? Let’s talk it through."
    ],
    "Joy": [
        "That’s wonderful to hear! What’s making you feel so happy today?",
        "I’m so glad you’re feeling happy! What made today feel so special?",
        "It’s amazing to hear you're feeling happy. What's one thing that’s been brightening your day?"
    ]
}

def extract_keyword(user_input):
    """Extracts the most relevant word from the user input using NLP."""
    doc = nlp(user_input)
    keywords = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "ADJ", "VERB"]]
    if not keywords:
        return "this feeling"
    for keyword in keywords:
        if nlp(keyword)[0].pos_ == "NOUN":
            return keyword
    return random.choice(keywords)

def analyze_sentiment(user_input):
    """Analyze the sentiment of the input text to tailor the tone of the response."""
    sentiment = TextBlob(user_input).sentiment.polarity
    if sentiment > 0.1:
        return "positive"
    elif sentiment < -0.1:
        return "negative"
    else:
        return "neutral"

def generate_dynamic_response(emotion, keyword, sentiment):
    """Generate a dynamic response based on emotion, keyword, and sentiment."""
    response = random.choice(emotion_templates[emotion]).format(keyword=keyword)
    return response

@app.route('/talk_to_your_emotions')
def index():
    return render_template_string(open('index.html').read())

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    selected_emotion = request.json.get('selected_emotion')
    
    if selected_emotion in emotion_templates:
        keyword = extract_keyword(user_input)
        sentiment = analyze_sentiment(user_input)
        response = generate_dynamic_response(selected_emotion, keyword, sentiment)
        return jsonify({"response": response})
    return jsonify({"response": "Please choose a valid emotion."})

if _name_ == '_main_':
    app.run(debug=True)