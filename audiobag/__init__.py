import typer
import os

from audiobag.helpers.Downloaders import YoutubeDownloader

BASE = os.getcwd()

yt = YoutubeDownloader()
app = typer.Typer()


@app.command()
def search(search_keyword: str):
    if not yt.search(search_keyword):
        typer.echo("Work failed")
    else:
        typer.echo("Finished")
    

@app.command()
def download_from_file():
    """
    Write links in links.txt file
    """
    with open("links.txt", "r") as links_file:
        for line in links_file:
            yt.download(line.replace("\n", ""))


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
