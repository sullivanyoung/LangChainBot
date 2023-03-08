#make sure you have python installed

#pip install langchain, openai (pending changes), unstructured and chromadb

import os
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredFileLoader

os.environ["OPENAI_API_KEY"] = "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"

loader = UnstructuredFileLoader('./CoStarBenefits2023.txt')

index = VectorstoreIndexCreator().from_loaders([loader])

def get_response(user_input):
    return index.query(user_input)

#testing response
while True:
    print('Bot: ' + get_response(input('You: ')))