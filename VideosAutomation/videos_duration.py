import csv
from datetime import timedelta


def str_to_timedelta(str_duration):
    h, m, s = str_duration.split(":")
    return timedelta(hours=int(h), minutes=int(m), seconds=int(s))


def read_csv(file_name="videos.csv"):
    with open(file_name, mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        duration_dict = {}

        for row in csv_dict_reader:
            tech = row["technology"]

            duration_dict[tech] = duration_dict.get(tech, {})
            duration_dict[tech]["emote"] = duration_dict.get(row["emote"], row["emote"])

            timedelta_duration = str_to_timedelta(row["duration"])
            duration_dict[tech]["all"] = (
                    duration_dict.get(tech, {}).get("all", timedelta()) + timedelta_duration
            )
            # 0 because 1 is added anyway
            duration_dict[tech]["all_videos"] = (
                    duration_dict.get(tech, {}).get("all_videos", 0) + 1
            )
            if row["done"] == "True":
                duration_dict[tech]["done"] = (
                        duration_dict.get(tech, {}).get("done", timedelta())
                        + timedelta_duration
                )
                duration_dict[tech]["done_videos"] = (
                        duration_dict.get(tech, {}).get("done_videos", 0) + 1
                )

        print_duration_dict(duration_dict)


def print_duration_dict(duration_dict):
    technology_list = [technology for technology in duration_dict]
    max_length = len(max(technology_list, key=len))
    fixed_formatting = False

    if not fixed_formatting:
        max_length = 0

    total_videos_done = 0
    total_videos = 0
    total_duration_done = timedelta(0)
    total_duration = timedelta(0)

    for technology in duration_dict:
        emote = duration_dict[technology]["emote"]

        all_duration = duration_dict.get(technology, {}).get("all", timedelta())
        all_videos = duration_dict.get(technology, {}).get("all_videos", 0)
        total_duration += all_duration
        total_videos += all_videos

        done_duration = duration_dict.get(technology, {}).get("done", timedelta())
        done_videos = duration_dict.get(technology, {}).get("done_videos", 0)
        total_duration_done += done_duration
        total_videos_done += done_videos

        print(
            f"{emote} {technology.title().ljust(max_length)} | {done_videos}/{all_videos} | {done_duration} / {all_duration}"
        )

    print(
        f"🟰 {'Total'.title().ljust(max_length)} | {total_videos_done}/{total_videos} | {total_duration_done} / {total_duration}"
    )


if __name__ == "__main__":
    read_csv()
