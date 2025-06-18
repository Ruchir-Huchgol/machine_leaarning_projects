from langchain_ollama.llms import OllamaLLM
from langchain_ollama.prompts import ChatPromptTemplate
from vector import retriever

model=Ollama(model="llama3.2")

template="""
You are a helpful assistant.
Question: {question}
Answer:{question}
"""

prompt=ChatPromptTemplate.from_template(template)
chain=prompt | model

while True:
    question=input("How may I help you today : ")
    print("\n\n")
    if question=="exit":
            break
    results=retriever.invoke(query=question)
    result=chain.invoke({"question":question})
    print(result)

