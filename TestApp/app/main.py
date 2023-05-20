import os

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from PyPDF2 import PdfReader

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain import PromptTemplate

from authorization import authorization
from validation import chunks_size_validation

app = FastAPI()
file_path = os.getenv('FILE_PATH')


class Message(BaseModel):
    msg: str


@app.post('/api/send', dependencies=[Depends(authorization)])
async def send_message(msg: Message, chunk_size: int):
    msg_dict = msg.dict()

    reader = PdfReader(file_path)

    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunks_size_validation(chunk_size),
        chunk_overlap=0,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    embeddings = OpenAIEmbeddings(model='gpt-3.5-turbo')
    docsearch = FAISS.from_texts(texts, embeddings)

    template = """Answer the question based on the context below.
    
    If you are greeted, answer "Hello I am NiftyBridge AI assistant. How could I help you?" For example:
    User: Hello!
    AI: Hello I am NiftyBridge AI assistant. How could I help you?
    
    If the question is about Nifty Bridge and text of question have "Nifty Bridge" and you can`t find answer in context, 
    you should say "I don't know please contact with support by email support@nifty-bridge.com"
    For example:
    User: Tell about Nifty Bridge first customer
    AI: I don't know please contact with support by email support@nifty-bridge.com
    Another example:
    User: What is the name of Nifty Bridge CEO?
    AI: I don't know please contact with support by email support@nifty-bridge.com
    Another example:
    User: Who is the the founder of Nifty Bridge?
    AI: I don't know please contact with support by email support@nifty-bridge.com
    
    If the question is about everything but not Nifty Bridge, you say "I don`t know".
    An example:
    User: Tell about python
    AI: I don`t know
    Another example:
    User: What do you think about Ukraine?
    AI: I don`t know
    Another example:
    User: Where do you live?
    AI: I don`t know
    
    Context: {context}

    Question: {question}

    Answer: """

    prompt_template = PromptTemplate(
        input_variables=['context', 'question'],
        template=template
    )

    chain = load_qa_chain(OpenAI(model_name='gpt-3.5-turbo'), chain_type="stuff", prompt=prompt_template)

    question = msg_dict.get('msg')
    docs = docsearch.similarity_search(question)
    res = chain.run(input_documents=docs, question=question)

    return res
