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