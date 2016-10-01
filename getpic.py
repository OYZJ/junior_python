#coding=utf-8
import urllib
import re

def getHtml(url):
    # type: (object) -> object
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1


html = getHtml("http://tieba.baidu.com/p/2970106602")

print getImg(html)

