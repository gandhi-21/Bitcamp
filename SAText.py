""" Sentimental Analysis on the text"""

import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/gaurav/Desktop/BItcamp/key.json"

storage_client = storage.Client.from_service_account_json('key.json')


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    print("For the text written by the Author given for analysis:")
    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    if(score < 0.0):
        print("Too Negative!!")
        print(" May be Biased")
    elif(score >= 0.5):
        print("Too Positive!!")
        print("May be biased")
    else:
        print("Neither too positive(>0.5) nor too negative(<0.0)")
        print("Looks Unbiased")
    return 0


def analyze(linestring):
    client = language.LanguageServiceClient()

    document1 = types.Document(
        content=linestring,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document1)

    print_result(annotations)

linestring = open('text.txt', 'r', encoding="ISO-8859-1").read()
document = types.Document(
    content=linestring,
    type=enums.Document.Type.PLAIN_TEXT)

analyze(linestring)



