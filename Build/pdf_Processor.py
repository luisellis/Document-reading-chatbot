
from langchain.document_loaders.pdf import PDFMinerLoader
import sys 

# Use this code to unselect the files with parsing issues
def pdf_file_processor(pdf):
    # Try to open the PDF file and create a PDFLoader instance for it
    try:
        loader = PDFMinerLoader(pdf)
        return(loader)
    except Exception as e:
        print(f"Error processing file {pdf}: {str(e)}")
        return None