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


#---------------------------
#     Create Vector Store
#---------------------------

index = VectorstoreIndexCreator().from_loaders(loaders)

queries = [
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
for query in queries[0]:
    index.query_with_sources(query)

#------------------------------------
#  IF THE WHOLE CODE DOESN'T NEED TO RUN JUST RUN THESE LINES AND RUN THE QUERIES ABOVE/MOVE BELOW
#------------------------------------
import pickle

# Save the file
pickle.dump(index, file = open("index.pickle", "wb"))

# Reload the file
index_reloaded = pickle.load(open("index.pickle", "rb"))