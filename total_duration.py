def add_everything(durations):
    total_hours = 0
    total_minutes = 0
    total_seconds = 0

    for duration in durations:
        hours, minutes, seconds = duration.split(":")
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        total_hours += hours
        total_minutes += minutes
        total_seconds += seconds

    return (total_hours, total_minutes, total_seconds)


def calculate_total_time(h, m, s):
    m += s // 60
    s %= 60
    h += m // 60
    m %= 60


    if m < 10:
        m = str(m)
        m = f"0{m}"
    if s < 10:
        s = str(s)
        s = f"0{s}"

    return f"{h}:{m}:{s}"

   
completed_durations = ("1:14:29", "1:25:37")

total_durations = (
    "3:10:30", "1:22:23", "3:46:22", "1:14:29", "2:47:56",
    "5:00:17", "4:41:24", "1:25:37", "1:56:16", "2:46:22",
    "2:42:55")

all_completed = add_everything(completed_durations)
all_total = add_everything(total_durations)

completed = calculate_total_time(*all_completed)
total = calculate_total_time(*all_total)


print(f"{completed} / {total}")
