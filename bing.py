import urllib.request
import requests         
import os,datetime
from bs4 import BeautifulSoup

dirname=os.environ['HOME']+"/Pictures/Bing/"
if not os.path.exists(dirname):
    os.mkdir(dirname)

date = datetime.datetime.now()
month = date.strftime('%m')
day = date.strftime('%d')
filename = month+'_'+day+'.jpg'

if not os.path.exists(dirname+filename):
    prevMonth = 12 if month == 1 else (int(month) - 1)%12
    prevMonStr = str(prevMonth) if prevMonth >= 10 else '0'+str(prevMonth)
    prevFileName = prevMonStr+'_'+day+'.jpg'
    if os.path.exists(dirname+prevFileName):
        os.remove(dirname+prevFileName)

    raw_img_url = "https://cn.bing.com/HPImageArchive.aspx?n=1"
    soup = BeautifulSoup(requests.get(raw_img_url).text,"html.parser")
    img_url = 'https://cn.bing.com'+soup.find('url').text
    try:
        urllib.request.urlretrieve(img_url,dirname+filename)
    except IOError as e:
        pass
    except Exception as e:
        pass
