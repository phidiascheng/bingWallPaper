import urllib.request
import requests         
import os
from bs4 import BeautifulSoup

raw_img_url = "https://cn.bing.com/HPImageArchive.aspx?n=1"
soup = BeautifulSoup(requests.get(raw_img_url).text,"html.parser")
img_url = 'https://cn.bing.com'+soup.find('url').text
dirname=os.environ['HOME']+"/Pictures/Bing/"
if not os.path.exists(dirname):
    os.mkdir(dirname)
try:
    urllib.request.urlretrieve(img_url,dirname+'temp')
except IOError as e:
    pass
except Exception as e:
    pass
for i in range(30):
    filename = str(30-i)+'.jpg'
    if os.path.exists(dirname+filename):
        if filename == '30.jpg':
            os.remove(dirname+filename)
        else:
            os.rename(dirname+filename,dirname+str(31-i)+'.jpg')
os.rename(dirname+'temp',dirname+'1.jpg')
