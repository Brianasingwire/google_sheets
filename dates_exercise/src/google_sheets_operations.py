'''Google sheets operations functions'''

import csv

import gspread

from google.oauth2.service_account import Credentials


def authenticate_sheet(json_file):
    '''Function to read from google sheet'''
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']

    creds = Credentials.from_service_account_file(json_file, scopes=scope)

    client = gspread.authorize(creds)

    return client


def read_from_sheet(json_file, sheet_id):
    '''Function to read from google sheet'''
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']

    creds = Credentials.from_service_account_file(json_file, scopes=scope)

    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(sheet_id)

    worksheet = spreadsheet.sheet1

    data = worksheet.get_all_records()

    return data


def write_to_new_sheet(input_csv, spreadsheet_name, sheet_name, client):
    '''Function to write today's data to sheet'''
    with open(input_csv, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data_to_write_to_sheet = list(reader)
        print(data_to_write_to_sheet)

        spreadsheet = client.open(spreadsheet_name)
        worksheet = spreadsheet.worksheet(sheet_name)

        worksheet.clear()

        worksheet.update(data_to_write_to_sheet, 'A1')
