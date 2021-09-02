import os
import urllib.request
import re
from bs4 import BeautifulSoup


class YoutubeDownloader:
    """
    Model to adjust wanted youtube download.

    command example: youtube-dl --extract-audio --audio-format mp3 --output "/audio_in/%(uploader)s%(title)s1234.%(ext)s" {youtube_link}
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    video_link = "https://www.youtube.com/watch?v="
    search_link = "https://www.youtube.com/results?search_query="

    # TODO: Define the return type 
    def search(self, search_keyword: str):
        html = urllib.request.urlopen(self.search_link + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        result_links = [self.video_link + _ for _ in video_ids[:4]]
        for link in result_links:
            print(f"{result_links.index(link) + 1}  {self.title_from_video(link)} {link}")

        index = int(input("Number to download, 0 to exit: "))
        if index in range(1, len(result_links) + 1):
            return True if self.download(result_links[index - 1]) else False
        else:
            return False

    def download(self, link) -> bool:
        try:
            os.system(f'youtube-dl --extract-audio --audio-format mp3 --output '
                      f'"./audio_in/{input("File name: ")}.%(ext)s" {link}')
            return True
        except Exception:
            return False

    def download_from_file(self) -> None:
        with open("links.txt", "r") as links_file:
            for line in links_file:
                self.download(line.replace("\n", ""))

    @staticmethod
    def title_from_video(video_link):
        soup = BeautifulSoup(urllib.request.urlopen(video_link), "html.parser")
        return soup.title.get_text()
