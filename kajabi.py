# from lxml import html, etree
import requests


# Get Wistia embed link from kajabi
wistia = input("What is the wistia link? ")

# Extract video ID code from link
video_id = wistia[109:119]

# Generate link from video ID
webpageLink = (f"https://fast.wistia.net/embed/iframe/{video_id}?videoFoam=true")

# Get page source of link
page = requests.get(webpageLink)
page_source = page.text

# Find video link 
first = page_source.find('"progress":1.0,"url":"')
last = page_source.find(".bin")

video = (f"{page_source[first+22:last]}")

def downloadfile(name,url):
    name=(name+".mp4")
    r=requests.get(url)
    print("****Connected****")
    f=open(name,'wb');
    print("Downloading.....")
    for chunk in r.iter_content(chunk_size=255): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print("Done")
    f.close()

name = (f'videos/{input("Video Name: ")}')

downloadfile(name, video)