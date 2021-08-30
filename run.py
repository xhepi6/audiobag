import typer
import urllib.request
import re
import os

BASE = os.getcwd()


app = typer.Typer()


@app.command()
def search(search_keyword: str):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for _id in video_ids[:4]:
        typer.echo(f"https://www.youtube.com/watch?v={_id}")


@app.command()
def download(link):
    os.system(f'youtube-dl --extract-audio --audio-format mp3 --output '
              f'"/audio_in/%(uploader)s%(title)s1234.%(ext)s" {link}')


@app.command()
def download_from_file():
    with open("links.txt", "r") as links_file:
        for line in links_file:
            download(line.replace("\n", ""))


@app.command()
def download_from_soundcloud():
    ...


@app.command()
def split(filename):
    os.system(f"docker run -v {BASE}\\audio_out:/output -v {BASE}\\audio_in:/input nda_spleeter"
              f" separate -o /output /input/{filename} -p spleeter:5stems")


@app.command()
def split_all():
    to_do = [
        f_name for f_name in os.listdir(f"{BASE}/audio_in/")
        if f_name.split('.')[0] not in os.listdir(f"{BASE}/audio_out/")
    ]
    for file_name in to_do:
        os.system(f"docker run -v {BASE}\\audio_out:/output -v {BASE}\\audio_in:/input nda_spleeter"
                  f" separate -o /output -p spleeter:5stems \"/input/{file_name}\"")


if __name__ == "__main__":
    app()
