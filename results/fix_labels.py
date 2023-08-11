import csv

with open('res.csv', newline='') as csvfile, open('res.fixed.csv', 'w', newline='') as f:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        if 'NSG32' in row['algo']:
            row['algo'] = 'NSG32' 
        writer.writerow(row)



