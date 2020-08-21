import os
import requests
from lxml import etree
import wget

# prepare
download_directory = 'CSE_5526/'
os.makedirs(download_directory, exist_ok=True)
url = 'http://web.cse.ohio-state.edu/~wang.77/teaching/cse5526/'

# make request
r = requests.get(url)
html = etree.HTML(r.text)

# extract links
# for xpath 2.0
# slide_links = html.xpath('//li/a[ends-with(@href, ".pdf")]')
# for xpath 1.0 <--- lxml
slide_links = html.xpath("//li/a[substring(@href, string-length(@href)-3)='.pdf']")
slide_links = list(set(slide_links)) # remove the duplicated links
print(len(slide_links))

# download
for slide in slide_links:
  slide = slide.attrib['href']
  print(slide)
  download_link = url+slide
  file_name = os.path.basename(slide)
  download_path = download_directory + file_name # complete download link
  wget.download(download_link, download_path)