import csv # CSV module
from datetime import datetime

from matplotlib import pyplot as plt 

# Get dates, high and low temperatures from file.
filename= 'sitka_weather_2014.csv'
with open(filename) as f: # open and store object in f
    reader= csv.reader(f) # create reader object by passing object to reader
    header_row=next(reader) # returns next line in reader (contains file header)
   
   
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Enumerate gets index of each item and its value

    dates, highs, lows = [], [], []  # Empty list of highs
    for row in reader: # loop through the rows in reader object
        try: # Try to extra data
            current_date = datetime.strptime(row[0], "%Y-%m-%d") # Gets the string 
            # with the time, formatted to YYYY-MM-DD
            high = int(row[1])
            low = int(row[3])
        
        except ValueError: # If data missing, will print error with the missing data
            print(current_date, 'missing data')
            # After error processed, continue processing next row
        
        else: # If no error, else block runs
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
        print(highs)
    
# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5) # Pass the list of highs to plot, mark them in red
plt.plot(dates, lows, c='blue', alpha=0.5) # Pass list of lows to plot, mark them blue
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Alpha controls transparency
# Format plot
plt.title("Daily high  and low Temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16) # Dont have dates yet, so blank
fig.autofmt_xdate() # Draws labels diagonally to prevent overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
