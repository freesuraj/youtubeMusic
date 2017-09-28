from __future__ import unicode_literals
import youtube_dl
import thread


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

videos = [
    'https://www.youtube.com/watch?v=mcx6_3iuwI4',
    'https://www.youtube.com/watch?v=WPlY7K_MOJo',
    'https://www.youtube.com/watch?v=2Rm3YZ8D1rY',
    'https://www.youtube.com/watch?v=9AJAxPXVW1I',
    'https://www.youtube.com/watch?v=omk7j2-PH3c',
    'https://www.youtube.com/watch?v=gW_YwQ3UvXg',
    'https://www.youtube.com/watch?v=a3tiFj4gDWI',
    'https://www.youtube.com/watch?v=tNef_iSpt2I',
    'https://www.youtube.com/watch?v=34duoAEI44M',
    'https://www.youtube.com/watch?v=ERLPG5ThQp8',
    'https://www.youtube.com/watch?v=Wd5N9VNfM0U',
    'https://www.youtube.com/watch?v=ZsMdv0NMe6I',
    'https://www.youtube.com/watch?v=CZvhT9sIgF0',
    'https://www.youtube.com/watch?v=NOTaF9zv_pQ'
]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(videos)
    
