from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import  HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import UnstructuredFileLoader
import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain.document_loaders import TextLoader
loader = UnstructuredFileLoader('./CoStarBenefits2023.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

qa = VectorDBQA.from_chain_type(llm = Petals(model_name="bigscience/bloom-petals"), chain_type="stuff", vectorstore=docsearch)
query = "who is eligible for benefits?"
print(qa.run(query))