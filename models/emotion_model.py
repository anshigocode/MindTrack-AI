from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)


def analyze_emotion(text):

    result = emotion_classifier(text)[0][0]

    emotion = result["label"]

    confidence = round(result["score"] * 100, 2)

    summary = generate_summary(emotion)

    return emotion, confidence, summary


def generate_summary(emotion):

    summaries = {

        "joy":
            "You seem to be experiencing positive emotions today.",

        "sadness":
            "Your journal reflects sadness or emotional difficulty.",

        "anger":
            "You appear frustrated or angry about something.",

        "fear":
            "Your writing suggests worry or anxiety.",

        "surprise":
            "Something unexpected stood out in your day.",

        "disgust":
            "Your journal expresses discomfort or dissatisfaction.",

        "neutral":
            "Your journal appears emotionally balanced."

    }

    return summaries.get(
        emotion.lower(),
        "Emotion detected."
    )

if __name__ == "__main__":

    print(analyze_emotion("Today was the best day of my life!"))