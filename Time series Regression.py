from textblob import TextBlob

# Example text
regulatory_announcement = "The new regulations are expected to increase transparency in the market."

# Sentiment analysis
sentiment = TextBlob(regulatory_announcement).sentiment
print(sentiment)
