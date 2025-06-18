# this will be our local database this is the file that contains all the logic to vectoem  embedding chunking the information from the provided document.
from encodings import search_function
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df=pd.read_csv("data.csv")## load your data from the csv file
embeddings=OllamaEmbeddings(model="mxbai-embed-large")
db_location="./chroma_langchain_db"# this is the file/folder that will contain all the retrival data from csv
add_documents=not os.path.exists(db_location)

if add_documents:#create a readme for this document
    db=Chroma.from_documents(
        documents=[
            Document(page_content=row["text"],metadata={"source":row["source"]})# chain the following by understanding the key points of your csv 
            for _,row in df.iterrows()
        ],
        embedding=embeddings,
        persist_directory=db_location
    )
    db.persist()
else:
    db=Chroma(
        persist_directory=db_location,
        embedding_function=embeddings
    )

#connecting to llm
retriever=db.as_retriever(
search_kwargs={"k":5})
#this is used to control the number of documents that will be retrived
#k specifies how many of the most similar documents (or vectors) you want to retrieve.
#search_kwargs is a dictionary of keyword arguments passed to the search or retriever method; in this case, it sets k to 5.

#the code bellow has little to no difference the only difference being it will be able to analyse both textual and numeric data
"""import os
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# === Configuration ===
CSV_FILE = "data.csv"
DB_LOCATION = "./chroma_langchain_db"
EMBEDDING_MODEL = "mxbai-embed-large"
COLS_TO_EMBED = ["text", "description", "notes"]  # Customizable text fields
NUMERIC_COLS_AS_META = ["price", "rating", "score"]  # Columns to include as metadata

df = pd.read_csv(CSV_FILE)
df = df.fillna("")  # Handle NaNs gracefully

embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
add_documents = not os.path.exists(DB_LOCATION)

if add_documents:
    documents = []
    for i, row in df.iterrows():
        # Concatenate multiple text fields
        page_content = " ".join(str(row[col]) for col in COLS_TO_EMBED if col in row and str(row[col]).strip() != "")

        # Collect metadata from numeric (or categorical) fields
        metadata = {col: row[col] for col in NUMERIC_COLS_AS_META if col in row}

        document = Document(
            page_content=page_content,
            metadata=metadata,
        )
        documents.append(document)

    # Build vector store
    db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=DB_LOCATION
    )
    db.persist()
else:
    db = Chroma(
        persist_directory=DB_LOCATION,
        embedding_function=embeddings
    )


retriever = db.as_retriever(search_kwargs={"k": 5})

query = "Show me reviews with high scores"
results = retriever.get_relevant_documents(query)
displaying result 
for i, doc in enumerate(results, 1):
    print(f"\nResult #{i}")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
"""