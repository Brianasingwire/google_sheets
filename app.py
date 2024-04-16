'''Forms and Sheets'''

import os

import gspread

from google.oauth2.service_account import Credentials

from dotenv import load_dotenv


load_dotenv()

sheet_id = os.getenv('SHEET_ID')


scope = ['https://www.googleapis.com/auth/spreadsheets']

creds = Credentials.from_service_account_file('credentials.json', scopes=scope)

client = gspread.authorize(creds)


sheet = client.open_by_key(sheet_id)

print('')
print(sheet.title)

email_list = sheet.sheet1.col_values(3)
print(email_list)


# count repeated email addresses
# add column for repeated addresses
# export to csv
