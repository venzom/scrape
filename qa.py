# from lxml import html, etree
import requests


# Get Wistia embed link from kajabi
wistia = input("What is the wistia link? ")

# Extract video ID code from link
video_id = wistia[116:126]
# print(video_id)
# Generate link from video ID

webpageLink = (f'https://fast.wistia.com/embed/medias/{video_id}')
# webpageLink = (f"https://fast.wistia.net/embed/iframe/{video_id}?videoFoam=true")
print(webpageLink)

# Get page source of link
page = requests.get(webpageLink)
page_source = page.text



# Find video link 
first = (page_source.find('"metadata":{},"url":"')+21)
last = page_source.find('.bin","created_at"')

video = (f"{page_source[first:last]}")

print(video)
# # video = (f"{page_source[first+22:last]}")

# with open('test.txt', 'w') as f:
#     f.truncate(0)
    # f.write(f'{page_source}')

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