""" import argparse
parser = argparse.ArgumentParser(description="Adds videos' duration")
parser.add_argument('times', metavar='TIMES', type=str, nargs='+', help='adds times and shows their sum')
args = parser.parse_args()

all_passed = add_everything(args.times)
total_passed = calculate_total_time(*all_passed)
print(f"args.times\n{total_passed}") """


def sum_time(durations):
    hours, minutes, seconds = add_everything(durations)
    return calculate_total_time(hours, minutes, seconds)


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

    return total_hours, total_minutes, total_seconds


def calculate_total_time(h=0, m=0, s=0):
    m += s // 60
    s %= 60
    h += m // 60
    m %= 60

    # if m < 10:
    #     m = str(m)
    #     m = f"0{m}"
    # if s < 10:
    #     s = str(s)
    #     s = f"0{s}"
    #
    # return f"{h}:{m}:{s}"
    return "%d:%02d:%02d" % (h, m, s)


if __name__ == "__main__":
    completed_python = ("3:10:30",)
    completed_linux = ("1:14:29",)
    completed_rust = ("1:25:37",)
    completed_big_o_notation = ("0:00:00",)
    completed_bootstrap = ("0:00:00",)
    completed_docker = ("0:00:00",)
    completed_lua = ("0:00:00",)
    completed_durations = (
        *completed_python,
        *completed_linux,
        *completed_rust,
        *completed_big_o_notation,
        *completed_docker,
        *completed_bootstrap,
        *completed_lua,
    )

    total_python = ("3:10:30", "2:42:55", "1:22:23", "3:46:22")
    total_linux = ("1:14:29", "2:47:56", "5:00:17", "4:41:24")
    total_rust = ("1:25:37",)
    total_big_o_notation = ("1:56:16",)
    total_bootstrap = ("2:46:22",)
    total_docker = ("2:10:19",)
    total_lua = ("11:11:51",)
    total_durations = (
        *total_python,
        *total_linux,
        *total_rust,
        *total_big_o_notation,
        *total_docker,
        *total_bootstrap,
    )

    sum_completed_python = sum_time(completed_python)
    sum_completed_linux = sum_time(completed_linux)
    sum_completed_rust = sum_time(completed_rust)
    sum_completed_big_o_notation = sum_time(completed_big_o_notation)
    sum_completed_bootstrap = sum_time(completed_bootstrap)
    sum_completed_docker = sum_time(completed_docker)
    sum_completed_lua = sum_time(completed_lua)
    sum_durations = sum_time(completed_durations)

    sum_total_python = sum_time(total_python)
    sum_total_linux = sum_time(total_linux)
    sum_total_rust = sum_time(total_rust)
    sum_total_big_o_notation = sum_time(total_big_o_notation)
    sum_total_bootstrap = sum_time(total_bootstrap)
    sum_total_docker = sum_time(total_docker)
    sum_total_lua = sum_time(total_lua)
    sum_total = sum_time(total_durations)
    print("📽️ VIDEOS 📽️")
    print(f"🐍 Python: {sum_completed_python} / {sum_total_python}")
    print(f"🐧 Linux: {sum_completed_linux} / {sum_total_linux}")
    print(f"🦀 Rust: {sum_completed_rust} / {sum_total_rust}")
    print(
        f"⭕ Big O Notation: {sum_completed_big_o_notation} / {sum_total_big_o_notation}"
    )
    print(f"🥾 Bootstrap: {sum_completed_bootstrap} / {sum_total_bootstrap}")
    print(f"🐳 Docker: {sum_completed_docker} / {sum_total_docker}")
    print(f"🔵 Lua: {sum_completed_lua} / {sum_total_lua}")
    print(f"🟰 Total: {sum_durations} / {sum_total}")

    print("\n📝 ARTICLES 📝")
    completed_python_articles = ("0:09:05", "0:05:18")
    completed_docker_articles = ("0:00:00",)

    total_python_articles = ("0:09:05", "0:05:18")
    total_docker_articles = ("0:05:45",)

    completed_articles = (*completed_python_articles, *completed_docker_articles)
    total_articles = (*total_python_articles, *total_docker_articles)

    sum_completed_python_articles = sum_time(completed_python_articles)
    sum_completed_docker_articles = sum_time(completed_docker_articles)

    sum_total_python_articles = sum_time(total_python_articles)
    sum_total_docker_articles = sum_time(total_docker_articles)

    sum_completed_articles = sum_time(completed_articles)
    sum_total_articles = sum_time(total_articles)

    print(f"🐍 Python: {sum_completed_python_articles} / {sum_total_python_articles}")
    print(f"🐳 Docker: {sum_completed_docker_articles} / {sum_total_docker_articles}")
    print(f"🟰 Total: {sum_completed_articles} / {sum_total_articles}")
