import browser_cookie3
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36", 
    "Accept-Encoding":"gzip, deflate", 
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "DNT":"1",
    "Connection":"close", 
    "Upgrade-Insecure-Requests":"1"
}

cookies = browser_cookie3.chrome(domain_name='dr-alok-trivedi.mykajabi.com')
response = requests.get('https://dr-alok-trivedi.mykajabi.com/products/life-vault/categories/1141571', verify=False, headers=headers, cookies=cookies, timeout=3)
page_source = response.text

title_find = '<p class="syllabus__title">'
titles = []

tfirst = (page_source.find('<p class="syllabus__title">')+27)
tlast = (page_source.find('</p>',tfirst))
title = (page_source[tfirst:tlast])
titles.append(title)

for i in range(48):
    tfirst = (page_source.find('<p class="syllabus__title">',tlast)+27)
    tlast = (page_source.find('</p>',tfirst))
    title = (page_source[tfirst:tlast])
    titles.append(title)

print(titles)
# with open('test.txt', 'w') as f:
#     f.truncate(0)
#     f.write(f'{page_source}')