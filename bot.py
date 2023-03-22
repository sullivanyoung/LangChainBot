import os
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredFileLoader

os.environ["OPENAI_API_KEY"] = "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"

loader = UnstructuredFileLoader('./CoStarBenefits2023.txt')

index = VectorstoreIndexCreator().from_loaders([loader])

def get_response(user_input):
    return index.query(user_input)

# test for checking bot in console without running full application
while True:
    print('Bot: ' + get_response(input('You: ')))