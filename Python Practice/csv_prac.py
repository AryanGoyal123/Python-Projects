import csv

# writing csv files
data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]
new_data = [['Aryan', 19], ['Puneet', 49], ['Nishi', 48], ['Anya', 15]]

with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)

with open('output.csv', mode='a') as file:
    csv_writer = csv.writer(file)
    for row in new_data:
        csv_writer.writerow(row)

# reading a csv file
with open('output.csv', mode='r') as infile, open('filtered.csv', mode='w') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    headers = next(csv_reader)

    # we want to filter for age below 30 and print out to a new csv file
    new_data = [row for row in csv_reader if int(row[1]) <= 30]
    csv_writer.writerow(headers)
    for line in new_data:
        csv_writer.writerow(line)

with open('filtered.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        # but we don't want to have lists of strings
        print(' '.join(line))

# calculate average age of the filtered csv people
with open('filtered.csv', mode='r') as file:
    total_age = 0
    count_age = 0

    csv_reader = csv.reader(file)
    headers = next(csv_reader)

    for line in csv_reader:
        total_age += int(line[1])
        count_age += 1

    average_age = total_age / count_age
    print(f"Average age below 30: {average_age}")
