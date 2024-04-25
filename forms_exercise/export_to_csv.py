'''Export to csv'''

import csv

import os

import gspread

from google.oauth2.service_account import Credentials

from dotenv import load_dotenv


load_dotenv()


def export_to_csv(sheet_id, credential_file, output_file):
    '''function to export sheet to csv'''
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    creds = Credentials.from_service_account_file(
        credential_file, scopes=scope)

    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.worksheet('Form Responses 1')

    with open(output_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(worksheet.get_all_values())


if __name__ == '__main__':
    sheets = os.getenv('SHEET_ID')
    credential = 'credentials.json'
    output = 'sheet.csv'

    export_to_csv(sheets, credential, output)
