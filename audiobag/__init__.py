import typer

from audiobag.helpers import YoutubeDownloader, Separator


yt = YoutubeDownloader()
sp = Separator()
app = typer.Typer()


@app.command()
def search(search_keyword: str):
    """
    Firstly search with a word and select one to download.
    """
    if not yt.search(search_keyword):
        typer.echo("Mission failed")
    else:
        typer.echo("Finished.")
    

@app.command()
def download_from_file():
    """
    Write links in links.txt file first.
    """
    with open("links.txt", "r") as links_file:
        for line in links_file:
            yt.download(line.replace("\n", ""))


@app.command()
def download_from_soundcloud():
    ...


@app.command()
def split(filename: str, stems: int) -> None:
    """
    Separate files in parts. 
    Stems can be 2, 3 or 5
    """
    sp.split(filename, stems)


@app.command()
def split_all(overwrite: bool = False, stems: int = 2):
    """
    Separate all files in audio_in, user --overwrite to separate those that are already separated
    Set stems to 2, 3 or 5
    """
    sp.split_all(overwrite, stems)


