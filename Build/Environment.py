#To set environment variables for a GitHub repository, you can use GitHub Secrets:
#Go to your GitHub repository.
#Click on "Settings" in the repository's menu.
#In the left sidebar, select "Secrets."
#Click the "New repository secret" button.
#Enter a name for the secret (e.g., MY_VARIABLE) and its value.
#Click "Add secret" to save it.

import os

os.environ['OPENAI_API_KEY'] = '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'
# Replace these values with your own
github_owner = 'luisellis'
github_repo = 'Document-reading-chatbot'
github_path = 'PDFs/'  # Change this to the path where your PDFs are located

# Set your GitHub personal access token
github_token = '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' # This token is not working
