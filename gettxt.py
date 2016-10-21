#author:OYZJ
#date:10/21/2016

import re
import urllib2

response = urllib2.urlopen('http://baike.baidu.com/view/252108')
html = response.read()
matchobj = re.findall(r'<div class="para" label-module="para">(.*)</div>',html)
for i in range(4, 24):
    print matchobj[i]
# print matchobj.group()
# print html



