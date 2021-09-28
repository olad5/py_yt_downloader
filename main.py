#!/usr/bin/python3
import youtube_dl
import shutil
from hurry.filesize import size
import json
import sys
import pprint
import logging
import re

logging.basicConfig(
    level=logging.DEBUG, format="Line %(lineno)d - %(message)s",
)




class Youtube_download:
    def __init__(self):
        # self.show_formats()
        self.format_link()

    def format_link(self):
        self.url  = sys.argv[1]
        video_link_regex = re.compile(r'(https?://)?(www\.)?youtube\.(com|nl)/watch\?v=([\w-]+)(&.*?)')
        playlist_link_regex = re.compile(r'(https?://)?(www\.)?youtube\.(com|nl)/playlist\?list=([\w-]+)')
        # check if it's a single video link
        if  video_link_regex.search(self.url):
            logging. debug('hello')
            result_regex  = video_link_regex.search(self.url)
            video_link  = result_regex.group().split('&')[0]
            logging.debug(video_link)
        # check if it's a playlist link
        elif playlist_link_regex.search(self.url):
            logging. debug('Yes it a playlist')
            result_regex  = playlist_link_regex.search(self.url)
            playlist_link  = result_regex.group().split('&')[0]
            logging.debug(playlist_link)
        # check if link is not a youtube link
        else:
            logging.debug('Not even a yt link')
            sys. exit()
        sys.exit()


    def show_formats(self):
        # the link below is Ginger by Wizkid, you can replace it with any other
        # Youtube link
        #  demo link 'https://www.youtube.com/watch?v=YSy2lBZ1QrA'
        self.url  = sys.argv[1]


        self.ydl = youtube_dl.YoutubeDL()
        # uses the youtube_dl as a context manager
        with self.ydl:
            self.result  =  self.ydl.extract_info(self.url,
                                                  extra_info={'listformats':True},download=False)
            for format in  self.result['formats']:
                format_id = format['format_id']
                filesize = size( format['filesize'] ) if format['filesize'] else 0
                if  format['ext'] =='mp4':
                    ext = format['ext']
                else:
                    continue
                format_note = format['format_note']
                full_info  = '    '.join([str( 'id=' + format_id ), str(format_note),
                                          str( ext), str(filesize)])
                print(full_info)
            print()
            self.request_id()




    def request_id(self):
        select_id =  input("Pick a video id to download \n>>> ")
        # select_id = str ( 160 )
        select_dict = [format for format in self.result['formats'] if format['format_id'] == select_id][0]
        filesize=size( ( select_dict['filesize']  ))
        url = select_dict['url']
        print(f"Downloading {self.result['title']}, size={filesize}")
        self.title = self.result['title']
        for item in ["(", ")",  " ", ",", ".", "'"]:
            # logging.debug(item)
            self.title  = self.title.replace(item, '_')
        self.title  = self.title.replace('__', '_')
        self.download_video(select_id)

    def download_video(self,select_id):
        ydl_opts ={
            # 140 is hardcoded there because you can only merge m4a with mp4
            'format': select_id + '+140' ,
            'outtmpl':self.title +  '.%(ext)s',
        }

        logging.debug(ydl_opts['format'])
        logging.debug(self.url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ self.url ])
            shutil.move(self.title+'.mp4' ,'data')




if __name__ == '__main__':
    # initializes the class
    yt = Youtube_download()

