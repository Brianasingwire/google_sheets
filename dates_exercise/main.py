'''Calling function'''

import os

from dotenv import load_dotenv

from src.csv_operations import (
    compare_csv_files,
    write_to_csv,
    write_to_todays_only_csv,
    write_to_todays_csv,
    write_to_yesterdays_csv)

from src.google_sheets_operations import (
    authenticate_sheet, read_from_sheet, write_to_new_sheet)

from src.email_operations import (filter_by_todays_date,
                                  filter_by_yesterdays_list,
                                  remove_todays_duplicate_emails,
                                  remove_yesterdays_duplicate_emails)


load_dotenv()


def main():
    '''Function to call'''
    json_file = 'credentials.json'

    sheet_id = os.getenv('SHEET_KEY')

    client = authenticate_sheet(json_file)

    data = read_from_sheet(json_file, sheet_id)

    todays_date = '30-04-2024'

    yesterdays_date = '29-04-2024'

    todays_list = filter_by_todays_date(data, todays_date)

    yesterdays_list = filter_by_yesterdays_list(data, yesterdays_date)

    main_csv_file = 'main.csv'

    todays_csv_file = '30_04_2024.csv'

    today_only_file = '30_04_2024_today_only.csv'

    yesterdays_csv_file = '29_04_2024.csv'

    write_to_csv(main_csv_file, data)

    todays_filtered_data = remove_todays_duplicate_emails(todays_list)

    write_to_todays_csv(todays_csv_file, todays_filtered_data)

    yesterdays_filtered_data = remove_yesterdays_duplicate_emails(
        yesterdays_list)

    write_to_yesterdays_csv(yesterdays_csv_file, yesterdays_filtered_data)

    today_only_emails = compare_csv_files(todays_csv_file, yesterdays_csv_file)

    write_to_todays_only_csv(today_only_file, today_only_emails)

    spreadsheet_name = 'Registration Sheets'
    sheet_name = 'Sheet2'

    write_to_new_sheet(today_only_file, spreadsheet_name, sheet_name, client)


if __name__ == '__main__':
    main()
