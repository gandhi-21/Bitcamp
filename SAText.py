
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

    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return 0


def analyze(linestring):
    client = language.LanguageServiceClient()

    document1 = types.Document(
        content=linestring,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document1)

    print_result(annotations)


if __name__ == '__main__':
    linestring = open('text.txt', 'r', encoding="ISO-8859-1").read()
    document = types.Document(
        content=linestring,
        type=enums.Document.Type.PLAIN_TEXT)

analyze(linestring)



