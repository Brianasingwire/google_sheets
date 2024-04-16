'''Export to csv'''

import csv

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
worksheet_list = sheet.worksheets()
print(worksheet_list)
worksheet = sheet.worksheet('Form Responses 1')

print('')
print(sheet.title)


with open('sheet.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(worksheet.get_all_values())
