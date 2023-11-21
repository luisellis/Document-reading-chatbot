from PyPDF2 import PdfReader

# Use this code to delete the files with errors
def pdf_file_cleanser(pdf):
    # Try to open the PDF file and read its contents
    try:
        with open(pdf, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text() 
                # Append the text to the all_text string
                return(text)

                # I have to change this in a way that it will create a dictionary and if a file is unable to be read it should create a flag so It's not processed later down the road.
    except Exception as e:
        print(f"Error processing file {pdf}: {str(e)}")
        return("")
