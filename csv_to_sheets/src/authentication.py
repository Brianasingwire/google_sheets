'''Authenticate Google APIs'''

import gspread

from google.oauth2.service_account import Credentials


def authenticate_google_sheets(json_file):
    '''Function to authenticate google sheets'''
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']

    credential = Credentials.from_service_account_file(json_file, scopes=scope)

    client = gspread.authorize(credential)

    return client
