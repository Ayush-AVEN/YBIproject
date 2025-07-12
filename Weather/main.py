#Create Basic Functions
import csv
from datetime import datetime

def add_weather_entry(file_path):
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format.")
        return

    temp = input("Enter temperature (°C): ")
    try:
        temp = float(temp)
    except ValueError:
        print("Invalid temperature.")
        return

    condition = input("Enter weather condition (e.g., Sunny): ")

    # Check if date already exists
    existing_dates = set()
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                existing_dates.add(row[0])
    except FileNotFoundError:
        pass

    if date in existing_dates:
        print("Entry for this date already exists.")
        return

    # Append new entry
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['Date', 'Temperature', 'Condition'])
        writer.writerow([date, temp, condition])
    print("Entry added successfully!")


#Summarize and Export Trends
import pandas as pd

def summarize_weather(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n--- Weather Summary ---")
        print("Average Temp:", df['Temperature'].mean())
        print("Max Temp:", df['Temperature'].max())
        print("Min Temp:", df['Temperature'].min())
        print("\nWeather Condition Frequency:")
        print(df['Condition'].value_counts())
    except FileNotFoundError:
        print("No data available.")


#Create a Simple Menu
def main():
    file_path = 'data.csv'
    while True:
        print("\n1. Add Weather Entry")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_weather_entry(file_path)
        elif choice == '2':
            summarize_weather(file_path)
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()

