'''Email operation functions'''


def filter_by_todays_date(data, todays_date):
    '''Function to filter out today's data'''
    # todays_list = [row for row in data if row['Dates'] == todays_date]
    todays_list = []
    for row in data:
        if row['Dates'] == todays_date:
            todays_list.append(row)
    return todays_list


def remove_todays_duplicate_emails(todays_list):
    '''Function to filter out today's duplicate emails'''
    unique_email = set()
    todays_filtered_data = []

    for item in todays_list:
        email = item['Email']
        if email not in unique_email:
            todays_filtered_data.append(item)
            unique_email.add(email)
    return todays_filtered_data


def filter_by_yesterdays_list(data, date):
    '''Function to filter out yesterday's list'''
    yesterdays_list = [row for row in data if row['Dates'] == date]
    return yesterdays_list


def remove_yesterdays_duplicate_emails(yesterdays_list):
    '''Function to filter out yesterday's duplicate email'''
    unique_email = set()
    yesterdays_filtered_data = []

    for item in yesterdays_list:
        email = item['Email']
        if email not in unique_email:
            yesterdays_filtered_data.append(item)
            unique_email.add(email)
    return yesterdays_filtered_data
