'''Repeated columns in a Googlesheet'''

import os

import gspread

from google.oauth2.service_account import Credentials

from dotenv import load_dotenv


load_dotenv()


def repeated_columns(sheet_id, credentials_file):
    '''function to return all columns'''
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    creds = Credentials.from_service_account_file(
        credentials_file, scopes=scope)

    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id)

    worksheet = sheet.worksheet('Form Responses 1')

    all_data = worksheet.get_all_values()

    email_counts = {}

    for row in all_data[1:]:
        email = row[2]
        if email in email_counts:
            email_counts[email] += 1
        else:
            email_counts[email] = 1

    print('Repeated email addresses...')

    for email, count in email_counts.items():
        if count > 1:
            print(f'{email}: occurs {count} times')


if __name__ == '__main__':
    sheets = os.getenv('SHEET_ID')
    credentials = 'credentials.json'

    repeated_columns(sheets, credentials)
