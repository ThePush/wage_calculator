import csv
header = ["name", "wage"]
wage_per_hour = 15
with open('input.csv') as input_file, open('output.csv', 'w') as output_file:
    reader = csv.DictReader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    writer.writerow(header)
    for line in reader:
        writer.writerow([line['name'], int(line['worked_hours']) * wage_per_hour])
