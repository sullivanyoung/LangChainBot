#make sure you have python installed

#pip install langchain, openai (pending changes), unstructured and chromadb

import os
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredFileLoader

os.environ["OPENAI_API_KEY"] = "insert your open ai key here"

loader = UnstructuredFileLoader('./CoStarBenefits2023.txt')

index = VectorstoreIndexCreator().from_loaders([loader])

query = "what is the 401k contribution limit"

print(index.query(query))