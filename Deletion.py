import csv

def main():
    with open(r'./Weather-Forecaster/GNV_RGNL_AP.csv', 'r', newline='') as csvfile, open(r'./Weather-Forecaster/Dataset.csv', 'w', newline='') as outputfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outputfile)
        header = next(reader)  # Skip header row
        writer.writerow(["YYYYMMDD", "PRECIPITATION", "MEAN TEMP"])
        
        for row in reader:
            coop_id, year, month, day, precipitation, temp = row
            if ((month == '2' and day == '29') and (precipitation == '-99.99' and temp == '-99.9')):
                continue
            
            YYYYMMDD = int(year) * 10000 + int(month) * 100 + int(day)
            writer.writerow([str(YYYYMMDD), precipitation, temp])

if __name__ == "__main__":
    main()
