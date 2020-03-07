import xml.etree.ElementTree as et
import urllib.request
from pyproj import Proj, transform
proj_UTMK = Proj(init='epsg:5178')
b=[]
url1 = 'http://www.opinet.co.kr/api/aroundAll.do?code=F668191226&x=314681.8&y=544837&radius=5000&sort=1&prodcd=B027&out=xml'
response = urllib.request.urlopen(url1).read()
root = et.fromstring(response)
for a in range(0, 1):
    b.append(root[a][3].text)
print(b)
