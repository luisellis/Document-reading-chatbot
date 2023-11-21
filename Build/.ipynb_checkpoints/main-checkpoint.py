# -*- coding: utf-8 -*-
"""
v1: Created on Tue May  2  2023
v1.1: Started developing in November 9 2023

"""

# Remember to install these packages in pip - We have to figure out how to set up an environment to run this
#pip install PyPDF2
#pip install langchain

# Base requeriments
import os
import requests

#User defined functions
from pdf_Cleanser import pdf_file_cleanser

# for AI and PDF processing

# libraries and dependencies:
    # pip install tiktoken
    # Visual Studio C++ Tools
    # pip install hnswlib
    # pip install openai
    # pip install chromadb
from langchain.document_loaders.pdf import PDFMinerLoader
from langchain.indexes import VectorstoreIndexCreator


# # To implement later
# my_variable = os.environ.get("OPENAI_API_KEY")

# if my_variable is not None:
#    print(f"OPENAI_API_KEY: {my_variable}")
# else:
#    print("OPENAI_API_KEY is not set.")
    
###################
#     Read PDF
###################

# Set the path to the directory containing the PDF files
pdf_dir  = "D:/Freelancering/Andrew/Document-reading-chatbot/PDFs" # This has to be changed to the raw_url

# Get a list of all files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# create empty string object
all_text = ""
#Iterate over files - find a way to change this
for file in pdf_files:
    dir = pdf_dir + '/' + file
    #dir = os.path.join(pdf_dir, file)
    # Apply cleansing function to read files
    text = pdf_file_cleanser(dir)
    # all_text += text


index = VectorstoreIndexCreator().from_loaders(loaders)

# query
query = "what is the objective for 2050 challenge?"
index.query_with_sources(query)
query = "what are foundational ideas of science of cities authors"
index.query_with_sources(query)
query = "do the authors mention any role cities?"
index.query_with_sources(query)
query = "What are some things that cities could apply in order to fulfill the 2050 challenge?"
index.query_with_sources(query)

# --- This one adds the page number and document name
# all_text = ""
# # Loop through each PDF file and extract its text
# for pdf_file in pdf_files:
#     # Set the path to the current PDF file
#     pdf_path = os.path.join(pdf_dir, pdf_file)
    
#     # Try to open the PDF file and read its contents
#     try:
#         with open(pdf_path, 'rb') as f:
#             pdf_reader = PdfReader(f)
#             doc_name = pdf_file.split(".")[0] # extract document name without extension
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text = page.extract_text()
#                 page_text = f"{doc_name} - Page {page_num + 1}: {text}" # add document name and page number before page text
#                 all_text += page_text
#     except Exception as e:
#         print(f"Error processing file {pdf_file}: {str(e)}")
#         continue
    