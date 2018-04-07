""" Classify Content on Author's text"""

import os
import six

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/gaurav/Desktop/BItcamp/key.json"

storage_client = storage.Client.from_service_account_json('key.json')


def classify_text(text):
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:
        print(u'=' *20)
        print(u'{:<16}: {}' .format('name', category.name))
        print(u'{:<16}: {}' .format('confidence', category.confidence))


linestring = open('text.txt', 'r', encoding="ISO-8859-1").read()

classify_text(linestring)
