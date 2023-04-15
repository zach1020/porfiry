# Adapted from https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma 
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

text = 'crime-and-punishment.txt'

from langchain.document_loaders import TextLoader 
loader = TextLoader('crime-and-punishment.txt')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0),
vectorstore.as_retriever(), return_source_documents=True)

chat_history = []

while True:
    query = input('> ')
    result = qa({"question": query, "chat_history": chat_history})
    chat_history.append((query, result['answer']))
    print("\nChatGPT: " + result['answer'] + '\n')
    print("Source documents: " + str(result['source_documents'][0]) + '\n')

