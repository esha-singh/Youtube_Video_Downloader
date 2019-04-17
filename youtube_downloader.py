import os 
from pytube import YouTube
import urllib.request
from bs4 import BeautifulSoup

def your_url():
    url_lists=[]
    #textString = "lost in istanbul" When inbuilt functionality
    textString = input("Search your video/song..")
    query = urllib.parse.quote(textString)
    url ="https://www.youtube.com/results?search_query="+query
    response =urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            url_lists.append('https://www.youtube.com'+vid['href'])

    return url_lists[0]

def progresscheck(stream = None, chunk = None,file_handle =None, left = None):
    progress_amount =(100*(file_size-left))/file_size
    print("{:00.0f}% downloaded".format(progress_amount))
    #print(progress_amount)

def file_path():
    home = os.path.expanduser('~');
    print (home)
    download_path =os.path.join(home,'Downloads')
    return download_path

def start():
    print("Video being saved to :{}".format(file_path()))
    y_url = your_url()
    #print(y_url)
    print("Accessing URL..")
    try:
        video = YouTube(y_url,on_progress_callback=progresscheck)
    except:
        print("Error : Check your Internet Connection")
        redo = start()
    video_type = video.streams.filter(progressive = True, file_extension ="mp4").first()
    title = video.title
    print("Fetching URL..")
    global file_size
    file_size = video_type.filesize
    video_type.download(file_path())
    print ("Ready to downlaod another video")
    again = start()
file_size=0
begin =start()

