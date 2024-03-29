# -*- coding: utf-8 -*-
"""
v1: Completely build in 1/9/2024


"""

#-----------------------------------
#   Notes for overall run of code
#-----------------------------------
"""""
Remember to install these packages in pip - We have to figure out how to set up an environment to run this
    pip install PyPDF2
    pip install langchain
for AI and PDF processing
 libraries and dependencies:
    # pip install tiktoken
    # Visual Studio C++ Tools
    # pip install hnswlib
    # pip install openai
    # pip install chromadb

"""
"""
# 1- check what the algorithm is doing with tables and images 
# separate functions - images, tables, pdf fixer 
# images, tables - 
"""
#-------------------------------------
# libraries and dependencies invoker 
#-------------------------------------

# environment
import Build.Environment # Temporal API Key
# Base requeriments
import os
import sys 
import requests
#User defined functions
from Build.pdf_selector import pdf_file_selector
from Build.pdf_Processor import pdf_file_processor

#LangChain
from langchain.indexes import VectorstoreIndexCreator
# Verify which of these dependencies are needed
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import time


# Verify if key exists
my_variable = os.environ.get("OPENAI_API_KEY")
if my_variable is not None:
   print("OPENAI_API_KEY exists - continue to run")
else:
   sys.exit("OPENAI_API_KEY is not set. Verify the key before running.")
    
#--------------------------------------------------------------------
#     PDF Directory - to be changed later to cloud implementation
#--------------------------------------------------------------------
   
# Set the path to the directory containing the PDF files 
   # This is done locally at the moment - but should work in any local pc with Github conf
current_dir = os.getcwd()
pdf_dir  = os.path.join(os.getcwd(),"PDFs")
if os.path.isdir(pdf_dir):
    print('folder exists')
else:
    sys.exit("Make sure the \"PDFs\" folder is in a relative path.") # Exit if not github conf

#--------------------
#     Read Selector
#--------------------

# Get all PDFs
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# create empty list
pdf_selected = []

#Iterate over files 
for file in pdf_files:
    dir = pdf_dir + '/' + file
    if os.path.isfile(dir): # only apply if the file exists (it should exist)
        # Apply cleansing function to select files
        selected_file = pdf_file_selector(dir)
        if selected_file is not None:
            pdf_selected.append(selected_file) 

print(f"Out of {len(pdf_files)} only {len(pdf_selected)} will be considered for the analysis.")

#----------------------
#     Process PDFs
#----------------------

# create empty loader
loaders = []

#Iterate over files 
for file in pdf_selected:
    if os.path.isfile(file): # in case something breaks above
        loader = pdf_file_processor(file)
        if loader is not None: # it should ALWAYS return objects
            loaders.append(loader) 

# Dependency: pip install unstructured
            # pip install "unstructured[pdf]"
# from langchain.document_loaders import DirectoryLoader
# loader = DirectoryLoader(pdf_dir, glob="./*.pdf")
# doc = loader.load ( )


#---------------------------
#     Create Vector Store
#---------------------------

# Try new method
            # Complication 1 with new method:
            # The splitting is bad apparently
index = VectorstoreIndexCreator(
    # split the documents into chunks
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0),
    # select which embeddings we want to use
    embedding=OpenAIEmbeddings(),
    # use Chroma as the vectorestore to index and search embeddings
    vectorstore_cls=Chroma).from_loaders(loaders)
            
# This part is from article, might not be needed because we are already creating loader
# loader = TextLoader(loaders, encoding='utf8')
# data = loader.load()
            
# # Apply method
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0, length_function = len,)
# documents = text_splitter.split_documents(loaders)
# embeddings = OpenAIEmbeddings()
# vectorstore = Chroma.from_documents(documents, embeddings)
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
# memory = ConversationBufferMemory(k = 3,memory_key="chat_history", return_messages=True)
# qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever(), memory=memory)
# result=qa({"question":'Can you analyze and compare the core functionalities of each decision support tool, focusing on their primary purposes and capabilities in the context of climate action?'})
# print(result)
# print(result['answer'])

###
#    First set of Queries to make:
###

# queries = [
#     "Can you analyze and compare the core functionalities of each decision support tool, focusing on their primary purposes and capabilities in the context of climate action?",
#     "What are the underlying methodological approaches used in each tool? How do they integrate data science and climate modeling techniques?",
#     "What types of data do these tools require for operation? Please identify and compare the sources of data they use (e.g., climatic, socio-economic, infrastructural).",
#     "How do user interfaces and accessibility features differ among these tools? Assess their ease of use for different stakeholder groups.",
#     "Evaluate the scenario modeling capabilities of each tool. How detailed and diverse are the climate and policy scenarios they can simulate?",
#     "What features do these tools offer for stakeholder engagement and communication? How do they visualize data and model outcomes for different audiences?",
#     "Assess the level of customization and flexibility offered by each tool. How well can they be adapted to specific urban contexts or policy goals?",
#     "How do each of these tools support policy decision-making? Analyze their capacity to provide actionable recommendations or insights.",
#     "What are the strengths and limitations of each tool in supporting climate action decisions? Compare their effectiveness in various urban and policy contexts.",
#     "Investigate how each tool can be integrated with other urban planning or climate action systems. What are the possibilities and challenges of such integrations?"
# ]

#####
#        Second set of queries to make:
#####

queries = [
    "make me a table of each master plan and free environmental impacts it covers",
    "Can you analyze and compare the core functionalities of each decision support tool, focusing on their primary purposes and capabilities in the context of climate action?",
    "What are the underlying methodological approaches used in each tool? How do they integrate data science and climate modeling techniques?",
    "What types of data do these tools require for operation? Please identify and compare the sources of data they use (e.g., climatic, socio-economic, infrastructural).",
    "How do user interfaces and accessibility features differ among these tools? Assess their ease of use for different stakeholder groups.",
    "Evaluate the scenario modeling capabilities of each tool. How detailed and diverse are the climate and policy scenarios they can simulate?",
    "What features do these tools offer for stakeholder engagement and communication? How do they visualize data and model outcomes for different audiences?",
    "Assess the level of customization and flexibility offered by each tool. How well can they be adapted to specific urban contexts or policy goals?",
    "How do each of these tools support policy decision-making? Analyze their capacity to provide actionable recommendations or insights.",
    "What are the strengths and limitations of each tool in supporting climate action decisions? Compare their effectiveness in various urban and policy contexts.",
     "Investigate how each tool can be integrated with other urban planning or climate action systems. What are the possibilities and challenges of such integrations?"
]

# query
llm = ChatOpenAI(temperature=0, openai_api_key=my_variable)

for query in queries:
    answer = index.query_with_sources(llm=llm, question=query, chain_type="stuff")
    print(query)
    print(answer)

#------------------------------------
#  IF THE WHOLE CODE DOESN'T NEED TO RUN JUST RUN THESE LINES AND RUN THE QUERIES ABOVE/MOVE BELOW
#------------------------------------
import pickle

# Save the file
pickle.dump(llm, file = open("llmmodel.pickle", "wb"))
pickle.dump(loader, file = open("loader.pickle", "wb"))
pickle.dump(loaders, file = open("loaders.pickle", "wb"))
#pickle.dump(index, file = open("index.pickle", "wb")) # the index cannot be saved with this method

# Reload the file
# index_reloaded = pickle.load(open("index.pickle", "rb"))
llm = pickle.load(open("llmmodel.pickle", "rb"))
#loader = pickle.load(open("loader.pickle", "rb"))
loaders = pickle.load(open("loaders.pickle", "rb"))