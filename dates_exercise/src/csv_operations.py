'''CSV file operations functions'''

import csv


def compare_csv_files(file1, file2):
    '''Function to compare today's and yesterday's csv files'''
    with open(file1, 'r', encoding='utf-8') as f1, open(
        file2, 'r', encoding='utf-8'
    ) as f2:
        read_file1 = csv.DictReader(f1)
        read_file2 = csv.DictReader(f2)

        data1 = list(read_file1)
        data2 = list(read_file2)

        emails1 = {row['Email'] for row in data1}
        emails2 = {row['Email'] for row in data2}

        common_emails = emails1.intersection(emails2)

        today_only_emails = [
            row for row in data1 if row['Email'] not in common_emails]
        return today_only_emails


def write_to_csv(main_csv_file, data):
    '''Function to write sheet data to CSV file'''
    with open(main_csv_file, 'w', encoding='utf-8') as file:
        fieldnames = ['Dates', 'Names', 'Address', 'Telephone', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def write_to_todays_only_csv(today_only_file, today_only_emails):
    '''Function to write emails that appear only today to csv file'''
    with open(today_only_file, 'w', encoding='utf-8') as file:
        fieldnames = ['Dates', 'Names', 'Address', 'Telephone', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(today_only_emails)


def write_to_todays_csv(todays_csv_file, todays_filtered_data):
    '''Function to write today's data to csv file'''
    with open(todays_csv_file, 'w', encoding='utf-8') as file:
        fieldnames = ['Dates', 'Names', 'Address', 'Telephone', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(todays_filtered_data)


def write_to_yesterdays_csv(yesterdays_csv_file, yesterdays_filtered_data):
    '''Function to write yesterday's data to csv file'''
    with open(yesterdays_csv_file, 'w', encoding='utf-8') as file:
        fieldnames = ['Dates', 'Names', 'Address', 'Telephone', 'Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(yesterdays_filtered_data)
