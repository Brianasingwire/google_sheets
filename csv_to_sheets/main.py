'''Main function call'''

from src.authentication import authenticate_google_sheets
from src.reader import read_into_csv
from src.writer import write_to_sheet


def main():
    '''Main'''
    json_file = 'credentials.json'
    csv_file = 'innovators.csv'

    spreadsheet_name = 'Innovatorss'
    sheet_name = 'Sheet1'

    client = authenticate_google_sheets(json_file)
    data = read_into_csv(csv_file)

    write_to_sheet(data, spreadsheet_name, sheet_name, client)


if __name__ == '__main__':
    main()
