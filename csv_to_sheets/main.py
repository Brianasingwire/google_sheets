'''Main function call'''

from src.authentication import authenticate_google_sheets
from src.reader import read_from_csv
from src.writer import write_to_sheet


def main():
    '''Main'''
    json_file = 'credentials.json'
    csv_file = 'innovators.csv'

    spreadsheet_name = 'Innovatorss'
    sheet_name = 'Sheet1'

    client = authenticate_google_sheets(json_file)
    data = read_from_csv(csv_file)

    write_to_sheet(data, spreadsheet_name, sheet_name, client)


if __name__ == '__main__':
    main()


# Given spreadsheet ID, read and save as csv file with a file name of
# that days' date

# Filter out duplicate email before writing csv file
# 26_04_2024_all.csv

# Read yesterday's file(e.g 25_04_2024_all.csv) and today's file then
# compare and generate new file with emails appearring only once

# 26_04_2024_today_only.csv

# Generate a Google sheet with above csv file(26_04_2024_today_only.csv)
# contents
