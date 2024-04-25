'''Read into csv file'''

import csv


def read_into_csv(csv_file):
    '''Function to read into csv file'''
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        return data
