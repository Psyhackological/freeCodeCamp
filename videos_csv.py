import csv

with open("videos.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(
            row["emote"],
            row["technology"],
            row["yt-link"],
            row["duration"],
            row["done"],
        )
