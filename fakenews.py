import csv

## Alton perrish has 3/3 fake articles

with open('news_sample.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    count = 0
    fake = 0
    political = 0
    alton = 0
    beforeitnew = 0
    for row in csv_reader:

        if (row["domain"] == "beforeitsnews.com"):
            beforeitnew += 1
            print(row["type"])

        if (row["type"] == "fake"):
            fake += 1

        elif (row["type"] == "political"):
            political += 1
        
        if(row["authors"] == 'Alton Parrish'):
            alton += 1

        count += 1

    print(beforeitnew)
    print(count)
    print(155/250)
    our_string = "CDEFGHIJKL"

print(csv_reader._fieldnames)