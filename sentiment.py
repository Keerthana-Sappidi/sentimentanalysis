from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float

    @staticmethod
    def get_mood(input_text: str, threshold: float = 0.3):
        sentiment = TextBlob(input_text).sentiment.polarity
        friendly_threshold = threshold
        hostile_threshold = -threshold

        if sentiment >= friendly_threshold:
            return Mood('😊', sentiment)
        elif sentiment <= hostile_threshold:
            return Mood('😠', sentiment)
        else:
            return Mood('😐', sentiment)


if __name__ == '__main__':
    while True:
        text = input('Text:')
        mood = Mood.get_mood(text, threshold=0.3)

        print(f'{mood.emoji} ({mood.sentiment})')
