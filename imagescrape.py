from bs4 import BeautifulSoup
import requests
from lxml import etree
import io
import re

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
site1 = ""
site2 = ""
site3 = ""
site4 = ""
sites = [site1,site2,site3,site4]
dlist1, dlist2, dlist3, dlist4 = [], [], [], []
dlists = [dlist1, dlist2, dlist3, dlist4]
names = []
count = 0
for site in sites:
    response = requests.get(f"{site}",headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("h1", {"class" : "text-[24px] font-bold text-dark dark:text-white"})
    name = name.text.strip().split('\n')[0]
    names.append(name)
    print(names)
    smalllinks = soup.find_all("a")
    links = [a["href"] for a in smalllinks if a["href"].endswith((".jpg", "JPG"))]
    for image in links:
        if 'å°é¢-8pVSbrZC' in image:
            continue
        updated_image = re.sub(r'cdn(\d+)', r'i\g<1>', image)
        dlists[count].append(updated_image)
    count += 1
    
for dlist in dlists:
    print(dlist)
count = 0    
for name in names:
    f = io.open(f"{name}.txt", "w", encoding='utf-8')
    for link in dlists[count]:
        f.write(link + '\n')
    f.close()
    count += 1