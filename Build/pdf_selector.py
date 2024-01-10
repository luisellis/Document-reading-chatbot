from PyPDF2 import PdfReader
import sys 

# Use this code to unselect the files with parsing issues
def pdf_file_selector(pdf):
    # Try to open the PDF file and read its contents
    try:
        with open(pdf, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                _ = page.extract_text() # we really don't care about the text - don't save
        #print(f"Processed file: {pdf}") 
        return pdf # Return the path if it was successfull
    except Exception as e:
        print(f"Error processing file {pdf}: {str(e)} -- file Excluded from analysis")
        return None