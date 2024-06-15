import nltk

def sentiment_analysis(text):
    sentiment_analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
    sentiment_score = sentiment_analyzer.polarity_scores(text)
    return sentiment_score

text = "I love this product!"
sentiment_score = sentiment_analysis(text)

print(sentiment_score)