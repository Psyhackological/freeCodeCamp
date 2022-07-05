from requests import get
from bs4 import BeautifulSoup
import readtime


class Article:
    def __init__(self, url):
        self.article_url = url
        self.soup = BeautifulSoup(get(self.article_url).content, "html.parser")
        self.title = self.soup.title.text
        self.tupple_tags = self.find_all_text()
        self.string_tags = []
        self.convert_them_into_string()
        self.mega_string = self.merge_into_mega_string()
        self.img_readtime_s = self.image_readtime()
        self.text_readtime_s = self.text_readtime()
        self.total_readtime_s = self.text_readtime_s + self.img_readtime_s

    def __str__(self):
        seconds = self.total_readtime_s % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)

    def find_all_text(self):
        all_h1 = self.soup.find_all("h1")
        all_h2 = self.soup.find_all("h2")
        all_p = self.soup.find_all('p')
        all_pre = self.soup.find_all("pre")

        return all_h1, all_h2, all_p, all_pre

    def text_readtime(self):
        estimated_text_readtime = readtime.of_text(self.mega_string)
        return estimated_text_readtime.seconds

    def image_readtime(self):
        # img_weight * num_images
        # With img_weight starting at 12 and decreasing one second with each image encountered, with a minium img_weight of 3 seconds.
        # all_img_readtime = [readtime.of_html(image).seconds for image in all_img_filtered]
        # total_seconds = sum(all_img_readtime)

        all_img_filtered = self.soup.find_all("img")[2:-1]
        num_images = len(all_img_filtered)
        img_weight = 12 - num_images + 1  # Adding 1, because I think when I have 1 image it is multiplied by 12, not 11.
        if img_weight < 3:
            img_weight = 3
        print(img_weight, num_images)
        total_seconds = img_weight * num_images

        return total_seconds

    def convert_them_into_string(self):
        for object_tag in self.tupple_tags:
            tuple_of_tup = tuple([tag.text.strip() for tag in object_tag if len(tag) != 0])
            string_tag = "".join(tuple_of_tup)
            self.string_tags.append(string_tag)

    def merge_into_mega_string(self):
        return "".join(self.string_tags)


article1 = Article("https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/")
print(article1.title, article1)
