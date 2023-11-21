
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
