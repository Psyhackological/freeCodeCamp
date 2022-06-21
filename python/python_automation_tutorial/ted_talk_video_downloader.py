import requests  # requests module
from bs4 import BeautifulSoup  # web scrapping module
import re  # regular expressions
import argparse  # argument parsing

url = "https://www.ted.com/talks/david_cage_how_video_games_turn_players_into_storytellers"
request_response = requests.get(url)
soup = BeautifulSoup(request_response.content, "html.parser")
title = soup.find("h1", attrs={"data-testid": "talk-title"})
huge_chunk_to_search = soup.find("script", attrs={"id": "__NEXT_DATA__", "type": "application/json"})
match = re.search(
    'https://py\.tedcdn\.com/consus/projects/[0-9]{2}/[0-9]{2}/[0-9]{2}/[0-9]{3}/products/[a-z0-9-]{4,}\.mp4',
    huge_chunk_to_search.text)
print(title.text)
print(match.group())
