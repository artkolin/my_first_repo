import csv

if __name__ == "__main__":
    csvfile = open('eggs.csv', 'w', newline='')
    spamwriter = csv.writer(
        csvfile, delimiter=',',
    )
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    csvfile.close()