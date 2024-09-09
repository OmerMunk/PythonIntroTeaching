import csv
from datetime import datetime

csv_file_path ='export (1).csv'

data_list = []

with open(csv_file_path, "r", encoding="utf-8-sig", newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data_list = list(csv_reader)




def analyze_interest_with_dates(data, start, end):
    # Convert start and end to datetime objects for comparison
    start_date = datetime.strptime(start, '%m/%Y')
    end_date = datetime.strptime(end, '%m/%Y')

    # Filter rows that are within the date range
    filtered_data = []
    for row in data:
        try:
            # Convert the 'Time' column to a datetime object
            row_date = datetime.strptime(row['Time'], '%Y-%m-%d')


        except (ValueError, KeyError):
            continue

        # Check if the row date is within the start and end date range
        if start_date <= row_date <= end_date:
            # print(f'row is {row}')
            filtered_data.append(row)

    # Extract interest rates as float values
    interests = [float(row['']) for row in filtered_data]
    # print(f'interests: {interests}')

    # Calculate required statistics
    avg = sum(interests) / len(interests) if interests else 0
    total_change = interests[-1] - interests[0] if len(interests) > 1 else 0
    max_interest = max(interests, default=0)
    min_interest = min(interests, default=0)
    start_interest = interests[0] if interests else 0
    end_interest = interests[-1] if interests else 0

    # Prepare result dictionary
    result = {
        'avg': avg,
        'total_change': total_change,
        'max': max_interest,
        'min': min_interest,
        'start_interest': start_interest,
        'end_interest': end_interest
    }

    return result

def analyze_interest(data, start, end):
    # Extract month and year from start and end
    start_month, start_year = map(int, start.split('/'))
    end_month, end_year = map(int, end.split('/'))

    # Filter rows that are within the date range
    filtered_data = []
    for row in data:
        try:
            # Extract year, month, and day from the 'Time' column
            year, month, day = map(int, row['Time'].split('-'))
        except (ValueError, KeyError):
            # Skip rows that do not match the date format or are missing the 'Time' key
            continue

        # Compare the year and month to check if within the start and end range
        if (start_year < year < end_year) or \
           (year == start_year and month >= start_month) or \
           (year == end_year and month <= end_month):
            filtered_data.append(row)

    # Extract interest rates as float values
    # interests = [float(row['']) for row in filtered_data]
    interests = []
    for row in filtered_data:
        interests.append(float(row['']))

    # Calculate required statistics
    avg = sum(interests) / len(interests)
    total_change = interests[-1] - interests[0]
    max_interest = max(interests)
    min_interest = min(interests)
    start_interest = interests[0]
    end_interest = interests[-1]

    # Prepare result dictionary
    result = {
        'avg': avg,
        'total_change': total_change,
        'max': max_interest,
        'min': min_interest,
        'start_interest': start_interest,
        'end_interest': end_interest
    }

    return result



start = '11/2019'
end = '07/2024'
result = analyze_interest(data_list, start, end)
print(result)

# {'avg': 1.7774780058651025, 'total_change': 4.25, 'max': 4.75, 'min': 0.1, 'start_interest': 0.25, 'end_interest': 4.5}
# {'avg': 1.8245533141210375, 'total_change': 4.25, 'max': 4.75, 'min': 0.1, 'start_interest': 0.25, 'end_interest': 4.5}