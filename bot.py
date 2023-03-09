import os
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredFileLoader

os.environ["OPENAI_API_KEY"] = "insert your open ai key here"

loader = UnstructuredFileLoader('./CoStarBenefits2023.txt')

index = VectorstoreIndexCreator().from_loaders([loader])

def get_response(user_input):
    return index.query(user_input)

# test for checking bot in console without running full application
# while True:
#     print('Bot: ' + get_response(input('You: ')))