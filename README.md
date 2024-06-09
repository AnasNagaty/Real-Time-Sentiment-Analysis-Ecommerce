# Real-Time-Sentiment-Analysis
Python script integrates sentiment analysis using NLTK's VADER module and MongoDB for storing and querying sentiment data from simulated reviews.



Script Overview:
Fetching Reviews: Simulates fetching reviews from an API or another source.
Sentiment Analysis: Uses NLTK's VADER sentiment analyzer to classify reviews into positive, negative, or neutral sentiments based on their compound score.
Storing in MongoDB: Stores each review along with its sentiment analysis results (sentiment, sentiment scores, timestamp) in MongoDB.
Querying Sentiment Statistics: Retrieves and prints overall sentiment statistics (total reviews, counts, and percentages of positive, negative, and neutral sentiments).
Optimizations and Improvements:
1. Error Handling and Resource Management:
Ensure proper error handling and resource management, especially when connecting to MongoDB (try-except-finally blocks).
2. MongoDB Operations:
Use insert_many() instead of insert_one() for bulk insertion of reviews to MongoDB for better performance.
3. Efficient Querying:
Instead of multiple count_documents() calls, which can be inefficient, use MongoDB's aggregation framework for more efficient counting.
4. Code Refactoring:
Refactor the code to enhance readability and maintainability.
5. NLTK VADER Initialization:
Initialize the SentimentIntensityAnalyzer() instance once outside the loop for better performance.
