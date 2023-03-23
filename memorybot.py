import os
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredFileLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ChatVectorDBChain
import os 

os.environ["OPENAI_API_KEY"] = "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"
chat_history = []
loader = UnstructuredFileLoader('./CoStarBenefits2023.txt')
vectorstore_benefits = VectorstoreIndexCreator().from_loaders([loader]).vectorstore

system_template="""Use the following pieces of context to answer the users question. 
Try your best to answer. If the context does not help, use the document. If you are super unconfident, say i do not know
----------------
{context}"""

messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}")
]

prompt = ChatPromptTemplate.from_messages(messages)

qa = ChatVectorDBChain.from_llm(ChatOpenAI(temperature=0), vectorstore_benefits,qa_prompt=prompt)

def get_response(user_input):

    result = qa({"question": user_input, "chat_history": chat_history})
    chat_history.append([user_input, result["answer"]])

    return result["answer"]

# test for checking bot in console without running full application
# while True:
#     print('Bot: ' + get_response(input('You: ')))