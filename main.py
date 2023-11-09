# -*- coding: utf-8 -*-
"""
v1: Created on Tue May  2  2023
v1.1: Started developing in November 9 2023

"""

# Remember to install these packages in pip - We have to figure out how to set up an environment to run this
#pip install PyPDF2
#pip install langchain
import os
import requests
from PyPDF2 import PdfReader
from langchain.document_loaders.pdf import PDFMinerLoader
from langchain.indexes import VectorstoreIndexCreator




###################
#     Read PDF
###################



# Set the path to the directory containing the PDF files
#pdf_dir  = "D:/Freelancering/Andrew/ChatGPT consultation/academic read/academic read" # This has to be changed to the raw_url

# Replace 'raw_url' with the actual raw URL of the file in your GitHub repository
raw_url = 'https://raw.githubusercontent.com/username/repository/main/path/to/your/file.txt'


# change to a modular method
response = requests.get(raw_url)
if response.status_code == 200:
    data = response.text
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

#pdf_path = '../PDFs/file.pdf'
#with open(pdf_path, 'rb') as pdf_file:
    # Your code to work with the PDF file


    
# Get a list of all files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]


# Use this code to delete the files with errors
all_text = ""
for pdf_file in pdf_files:
    # Set the path to the current PDF file
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
    # Try to open the PDF file and read its contents
    try:
        with open(pdf_path, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                # Append the text to the all_text string
                all_text += text
    except Exception as e:
        print(f"Error processing file {pdf_file}: {str(e)}")
        continue

# Update after deleting -- I run this code after removing certain files
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# Create a list to store the loaders for each file
loaders = []
# Loop through each PDF file and extract its text
for pdf_file in pdf_files:
    # Set the path to the current PDF file
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
    # Try to open the PDF file and create a PDFLoader instance for it
    try:
        loader = PDFMinerLoader(pdf_path)
        loaders.append(loader)
    except Exception as e:
        print(f"Error processing file {pdf_file}: {str(e)}")
        continue


# Create the index -- Has a lot of requirements:
    # pip install tiktoken
    # Visual Studio C++ Tools
    # pip install hnswlib
    #pip install openai
    # pip install chromadb
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
    