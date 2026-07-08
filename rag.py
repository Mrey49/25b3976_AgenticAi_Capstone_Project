import os
import pathlib

from dotenv import load_dotenv

from pypdf import PdfReader

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

API_KEY = os.getenv("api_key")
PDF_PATH = pathlib.Path("ugrulebook.pdf")
INDEX_PATH = pathlib.Path("rag_index")



embeddings = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",

    google_api_key=API_KEY,

    temperature=0

)


def build_vector_store():

    if not PDF_PATH.exists():

        raise FileNotFoundError(

            f"{PDF_PATH} not found."

        )

    loader = PyPDFLoader(

        str(PDF_PATH)

    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1500,

        chunk_overlap=300

    )

    chunks = splitter.split_documents(

        documents

    )

    vector_store = FAISS.from_documents(

        chunks,

        embeddings

    )

    vector_store.save_local(

        str(INDEX_PATH)

    )

    print(

        "Vector Store Created Successfully."

    )

def load_vector_store():

    if not INDEX_PATH.exists():

        build_vector_store()

    return FAISS.load_local(

        str(INDEX_PATH),

        embeddings,

        allow_dangerous_deserialization=True

    )

def retrieve(question, k=8):

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(

        search_type="mmr",

        search_kwargs={

            "k": k,

            "fetch_k": 20

        }

    )

    return retriever.invoke(question)

def get_context(question, k=8):

    docs = retrieve(question, k)

    context = []

    for doc in docs:

        page = doc.metadata.get(

            "page",

            "Unknown"

        )

        context.append(

            f"[PAGE {page + 1}]\n{doc.page_content}"

        )

    return "\n\n".join(

        context

    )

def get_registration_context():

    reader = PdfReader(

        str(PDF_PATH)

    )

    pages = []

    #
    # PDF page indices
    #
    # Page 20 -> index 19
    # Page 21 -> index 20
    #

    for page in [19, 20]:

        pages.append(

            reader.pages[page].extract_text()

        )

    return "\n\n".join(

        pages

    )


def get_llm():

    return llm

if __name__ == "__main__":

    print(

        get_registration_context()

    )
