import argparse
import io
import json
import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import storage

import numpy
import six


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/gaurav/Desktop/BItcamp/key.json"

storage_client = storage.Client.from_service_account_json('key.json')

buckets = list(storage_client.list_buckets())

client = language.LanguageServiceClient()

def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document1 = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document1)
    categories1 = response.categories

    result = {}

    for category1 in categories1:
        # Turning the categories into a dictionary of the form:
        # {category.name: category.confidence}, so to treat it as
        # a sparse vector
        result[category1.name] = category1.confidence

    if verbose:
        print(text)
        for category1 in categories1:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category1.name))
            print(u'{:<16}: {}'.format('confidence', category1.confidence))

    return result

"""
def index(path, index_file):
     Classify each text file in a directory and write
    the results to the index_file
   

    result = {}
    for filename in os.listdir(file_path):
        file_path = os.path.join(path, filename)

        if not os.path.isFile(file_path):
            continue

        try:
            with io.open(file_path, 'r') as f:
                text = f.read()
                categories = classify(text, verbose=False)

                result[filename] = categories
        except Exception:
            print('Failed to process {}'.format(file_path))

    with io.open(index_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

    print('Text indexed in file: {}'.format(index_file))
    return result


def similarity(categories1, categories2):
    ##Cosine similarity of categories treated as sparse vectors.
    categories1 = split_labels(categories1)
    categories2 = split_labels(categories2)

    norm1 = numpy.linalg.norm(list(categories1.values()))
    norm2 = numpy.linalg.norm(list(categories2.values()))

    if norm1 == 0 or norm2 == 2:
        return 0.0

    # compute the cosine similarity
    dot = 0.0
    for label, confidence in six.iteritems(categories1):
        dot += confidence * categories2.get(label, 0.0)

    return dot / (norm1 * norm2)
"""


linestring = open('Text.txt', encoding = "ISO-8859-1").read()
document = types.Document(
    content=linestring,
    type=enums.Document.Type.PLAIN_TEXT)

category = classify(linestring, False)

for categories in category:
    print(categories)
