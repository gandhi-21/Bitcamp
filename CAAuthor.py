# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import storage

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/gaurav/Desktop/BItcamp/key.json"

storage_client = storage.Client.from_service_account_json('key.json')


buckets = list(storage_client.list_buckets())


# Instantiate a client
client = language.LanguageServiceClient()

# The text to analyze
linestring = open('Author History.txt', 'r').read()
document = types.Document(
    content=linestring,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

