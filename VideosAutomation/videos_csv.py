import csv

def read_csv(file_name="videos.csv"):
    with open(file_name, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(
                row["emote"],
                row["technology"],
                row["yt-link"],
                row["duration"],
                row["done"],
            )

if __name__ == "__main__":
    read_csv()