from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup


linkregex = re.compile(b'<a\s*href=[\'|"](.*?)[\'"].*?>')
req = Request('http://www.viki.com', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#[m.start() for m in re.finditer('class',webpage)]

#links = linkregex.findall(webpage)
soup = BeautifulSoup(webpage,'html.parser')
mytitle = soup.find_all('a')
print(mytitle)
#for link in soup.find_all('a'):
#    print(link.get('href'))