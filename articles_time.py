from requests import get
from bs4 import BeautifulSoup
import readtime

url = "https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/"
request_response = get(url)
soup = BeautifulSoup(request_response.content, "html.parser")
all_h1 = soup.find_all("h1")
all_h2 = soup.find_all("h2")
all_p = soup.find_all('p')
all_pre = soup.find_all("pre")
print(all_h1.text, all_h2.text, all_p.text, all_pre.text)
# estimated_readtime = readtime.of_text(section_post_full_content)
# print(section_post_full_content)