'''Create and write to Google sheet'''

import gspread


def write_to_sheet(data, spreadsheet_name, sheet_name, client):
    '''Function to write to Google sheet'''
    try:
        spreadsheet = client.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        print(f'Spreadsheet {spreadsheet_name} not found')
        return

    try:
        worksheet = spreadsheet.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title=sheet_name, row='1000', col='20')

    worksheet.clear()

    worksheet.update(data, 'A1')
