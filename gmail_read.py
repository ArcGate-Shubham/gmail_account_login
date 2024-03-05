import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from selenium import webdriver


max_results = int(input('Enter number of display inbox message :'))
driver = webdriver.Chrome()
driver.maximize_window()
# OAuth 2.0 credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
flow = InstalledAppFlow.from_client_secrets_file('/home/arcgate/Downloads/credentials.json', SCOPES)
creds = None
token_path = 'token_data.json'

if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        creds = flow.run_local_server(port=0)
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

# Gmail API
service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(userId='me', labelIds=['INBOX'],maxResults=max_results).execute()
messages = results.get('messages', [])

# Read and print the subject of each email
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    description = msg['snippet']
    print('Description :',description)
    headers = msg['payload']['headers']
    for header in headers:
        if header['name'] == 'Subject':
            print(f"Subject: {header['value']}")
            
driver.quit()

