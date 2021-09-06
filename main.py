#!/usr/bin/python3
import youtube_dl
from hurry.filesize import size
import json
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG, format="Line %(lineno)d - %(message)s",
)


# Quick demo on the youtube_dl module
# Note this module is a downloader but this demo is using it as API to get data from 
# Youtube


class Youtube_data:
    def __init__(self):
        # initialize youtube_dl
        # self.ydl = youtube_dl.YoutubeDL()
        # print(sys.argv[1])
        # sys.exit()
        # self.query_video()
        self.show_formats()
        # self.print_data()
        # self.save_to_json()



    def show_formats(self):
        # the link below is Ginger by Wizkid, you can replace it with any other
        # Youtube link
        #  demo link 'https://www.youtube.com/watch?v=YSy2lBZ1QrA'
        self.url  = sys.argv[1]
        self.ydl = youtube_dl.YoutubeDL(ydl_opts)
        logging.debug(self.url)
        logging.debug(type(self.url))
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
                logging.debug(full_info)




    def save_to_json(self):
        # this function saves the output to a json file in the current directory
        # for easy viewing
        # NOTE: it overwrites the file result.json everytime it is run
        with open('data/result.json', 'w') as f:
            json_data  = json.dumps(self.result, indent=4)
            f.write(json_data)

    def print_data(self):
        # this function prints some important data we need about the Youtube
        # video
        # Title of the video
        video_title  =self.result['title']
        logging.debug(f"Video title is {video_title}\n")

        # video id for easy storage in database
        video_id  =self.result['id']
        logging.debug(f"Video id is {video_id}\n")

        # thumbnails that we can display for audio files
        thumbnails  =self.result['thumbnails']
        logging.debug(f"Video thumbnail links are  {thumbnails}\n")

        # duration of the video
        video_duration  =self.result['duration']
        logging.debug(f"Video duration is {video_duration}\n")

        # the artist name
        artist  =self.result['artist']
        logging.debug(f"Video artist is {artist}\n")



if __name__ == '__main__':
    # initializes the class
    yt = Youtube_data()

