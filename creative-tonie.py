#! /usr/bin/env python3
from __future__ import unicode_literals

import logging
import os
from tonie_controller import TonieController
import typer
from typing import Optional
from yt_dlp import YoutubeDL

log = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO)
log.addHandler(logging.NullHandler())

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
    'logger': log,
    'progress_hooks': [my_hook],
    'outtmpl': 'output.%(ext)s',
    'nocheckcertificate': True,
    'verbose': True,
    'force_generic_extractor': True
}

main = typer.Typer()

@main.command()
def copy_yt(tonie_name: str, youtube_link: str, content_title: Optional[str] = typer.Argument(default="custom_content")):
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])
        tc.tonieUpload(tonie_name, './output.mp3', content_title)
    typer.echo(f"done.")

@main.command()
def copy_path(tonie_name: str, file_path: str, content_title: Optional[str] = typer.Argument(default="custom_content")):
    if os.path.isdir(file_path):  
        log.info(f"uploading all files in {file_path}")
        for (dirpath, dirnames, filenames) in os.walk(file_path):
            for i in range(len(filenames)):
                f = f"{file_path}/{filenames[i]}"
                tc.tonieUpload(tonie_name, f, f"{content_title}-{i}")                
            break
    elif os.path.isfile(file_path):  
        tc.tonieUpload(tonie_name, file_path, content_title)
    typer.echo(f"done.")

@main.command()
def print_tonies():
    typer.echo(tc.printToniesOverview())

@main.command()
def wipe_tonie(tonie_name: str):
    tc.wipeTonie(tonie_name)
    typer.echo(f'tonie {tonie_name} wiped.')

@main.command()
def print_tonie_chapters(tonie_name: str):
    typer.echo(tc.getChaptersForTonie(tonie_name))

if __name__ == "__main__":
    tc = TonieController(os.environ.get('TONIECLOUD_USERNAME'), os.environ.get('TONIECLOUD_PASSWORD'))
    main()
