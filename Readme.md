# Youtube Crawler Running Instructions

### Use Python 2.7

## Dependencies
    lxml

## Running Commands

### Virtual Enviromnet Set Up
    virtualenv -p /usr/bin/python2.7  yout
    source  yout/bin/activate
    pip install -r requirements.txt

### Downloading Comments

### Collecting Youtube ID
    copy the video id from youtube video url
    example if  https://www.youtube.com/watch?v=zsnc0vkwWRk is the url 

    then id is zsnc0vkwWRk

### Command to run crawler

    python downloader.py --youtubeid <youtubeid> --output out.json

### Extraction

    python extraction.py 