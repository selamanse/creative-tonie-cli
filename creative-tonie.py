from __future__ import unicode_literals

import os, sys
from tonie_controller import TonieController
import typer
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('downloading done, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'outtmpl': 'output.%(ext)s'
}

main = typer.Typer()

@main.command()
def copy_yt(tonie_name: str, youtube_link: str, content_title: str='custom_content'):
    tonie_id = tc.getTonieIdByName(tonie_name)
    typer.echo(f"found tonie {tonie_name} with ID: {tonie_id}")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])
        tc.tonieUpload(tonie_id, './output.mp3', content_title)
    typer.echo(f"done.")

@main.command()
def print_tonies():
    typer.echo(tc.printToniesOverview())

@main.command()
def wipe_tonie(tonie_name: str):
    tonie_id = tc.getTonieIdByName(tonie_name)
    tc.wipeTonie(tonie_id)
    typer.echo(f'tonie {tonie_name} (ID: {tonie_id}) wiped.')

@main.command()
def print_tonie_chapters(tonie_name: str):
    tonie_id = tc.getTonieIdByName(tonie_name)
    typer.echo(tc.getChaptersForTonie(tonie_id))

if __name__ == "__main__":
    tc = TonieController(os.environ.get('TONIECLOUD_USERNAME'), os.environ.get('TONIECLOUD_PASSWORD'))
    main()
