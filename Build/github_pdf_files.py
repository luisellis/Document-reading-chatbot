#---------------------------------------------------------------------------------------
#
#      Do not use until we have set up rate limits and this will be ran in the cloud or something. Better run locally for testing phase
#
#---------------------------------------------------------------------------------------


# Make a request to the GitHub API
url = f'https://api.github.com/repos/{github_owner}/{github_repo}/contents/{github_path}'
headers = {'Authorization': f'token {github_token}'}
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    content_info = response.json()

    # Extract PDF URLs
    pdf_urls = [file['download_url'] for file in content_info if file['name'].lower().endswith('.pdf')]

    # Now you can process each PDF using PdfReader or any other library
    for pdf_url in pdf_urls:
        # Your code to process the PDF
        print(f"Processing PDF: {pdf_url}")
else:
    print(f"Failed to fetch repository content. Status code: {response.status_code}")
