import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pymongo import MongoClient
from datetime import datetime
import nltk

# nltk.download('vader_lexicon')
# Function to fetch reviews (simulated API call)
def fetch_reviews():
    # Simulating API call to fetch reviews
    reviews = [
        "Great product! Fast delivery and excellent quality.",
        "The item was damaged upon arrival. Very disappointed.",
        "Average experience. Nothing special about the product.",
        "Awesome service! Highly recommended seller.",
        "Too expensive for what you get. Wouldn't buy again."
    ]
    return reviews

# Function to perform sentiment analysis
def perform_sentiment_analysis(review):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(review)

    # Classify the sentiment based on compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment, sentiment_scores

# Function to store reviews in MongoDB
def store_in_mongodb(reviews):
    client = MongoClient('localhost', 27017)  # Assuming MongoDB is running on localhost
    db = client['sentiment_analysis']
    collection = db['reviews']

    for review in reviews:
        sentiment, sentiment_scores = perform_sentiment_analysis(review)
        review_entry = {
            'review': review,
            'sentiment': sentiment,
            'sentiment_scores': sentiment_scores,
            'timestamp': datetime.now()
        }
        collection.insert_one(review_entry)

    client.close()

# Function to query database for sentiment statistics
def query_sentiment_statistics():
    client = MongoClient('localhost', 27017)
    db = client['sentiment_analysis']
    collection = db['reviews']

    total_count = collection.count_documents({})
    positive_count = collection.count_documents({'sentiment': 'positive'})
    negative_count = collection.count_documents({'sentiment': 'negative'})
    neutral_count = collection.count_documents({'sentiment': 'neutral'})

    if total_count > 0:
        positive_percentage = (positive_count / total_count) * 100
        negative_percentage = (negative_count / total_count) * 100
        neutral_percentage = (neutral_count / total_count) * 100
    else:
        positive_percentage = 0.0
        negative_percentage = 0.0
        neutral_percentage = 0.0

    print(f"Total Reviews: {total_count}")
    print(f"Positive Reviews: {positive_count} ({positive_percentage:.2f}%)")
    print(f"Negative Reviews: {negative_count} ({negative_percentage:.2f}%)")
    print(f"Neutral Reviews: {neutral_count} ({neutral_percentage:.2f}%)")

    client.close()

# Main function to orchestrate the process
def main():
    # Simulate fetching reviews (from API or other source)
    reviews = fetch_reviews()

    # Store reviews in MongoDB
    store_in_mongodb(reviews)

    # Query and print sentiment statistics
    query_sentiment_statistics()

if __name__ == "__main__":
    main()
