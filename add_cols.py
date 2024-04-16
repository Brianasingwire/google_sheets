'''Add column'''

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

email_list = sheet.sheet1.col_values(3)
print(email_list)

print('')
all_data = worksheet.get_all_values()

print('')
email_counts = {}

for row in all_data[1:]:
    email = row[2]
    if email in email_counts:
        email_counts[email] += 1
    else:
        email_counts[email] = 1

for index, row in enumerate(all_data):
    if index == 0:
        row.append('Repeated email count')
    else:
        email = row[2]
        count = email_counts[email]
        row.append(str(count))

worksheet.update('A1', all_data)
