import csv # Comma Seperated Values module
from datetime import datetime
from matplotlib import pyplot as plt 

# Get dates, high and low temperatures from file.
filename= 'winter_2017_2018.csv'
with open(filename) as f: # open and store object in f
    reader= csv.reader(f) # create reader object by passing object to reader
    header_row=next(reader) # returns next line in reader (contains file header)
    # print(header_row) prints out the contents of the file header (year, precip,etc)
    
    #for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # Enumerate on the list to get the index of each item and its value
    
    dates, precipitationList = [], []
    for rowsOfFile in reader:           # Loop through row
        #current_date = rowsOfFile[0]
        #dates.append(current_date)
        if (rowsOfFile[0].find('-') != -1): # dash character found, so Month-Year format
            month_year = rowsOfFile[0]
        if (rowsOfFile[0].isdigit() and int(rowsOfFile[0]) <= 31 ): # Making sure we take days of month only, not YYYY
            date_string = month_year + '-' + rowsOfFile[0]
            current_date = datetime.strptime(date_string, '%B-%Y-%d')
            dates.append(current_date)
        
        if rowsOfFile[1].isdigit():     # First row has preciptation. Filter out any non-digits
            precipValues = float(rowsOfFile[1])
            precipitationList.append(precipValues)
    print(precipitationList)
    

# Plot data
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates, precipitationList, c='red')

# Format plot
plt.title("Winter 2017-2018 Preciptation Amounts", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precip. (in)", fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
