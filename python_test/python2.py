import sys
sys.path.append('/home2/anderary/soup')

import os
from datetime import datetime
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Select url
my_url = 'http://www.apablog.org/category/9th-grade/'

# Get today's date

my_url_date = datetime.today().strftime('%Y-%m-%d')

# opening up connection, grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# choose parser
page_soup = soup(page_html, "html.parser")

# set selections for parser
containers = page_soup.findAll("div",{"class":"entry-content"},
	{"class":"has-large-font-size"})

# delete file if exists
if os.path.exists("demo.html"):
	os.remove("demo.html")

# create html document
f=open('demo.html','a')
f.write('<!DOCTYPE html>\n')
f.write('<html>\n')
f.write('<body>\n')
f.write('<style>\n')
f.write('body{\n')
f.write('width:80%;\n')
f.write('margin:20px;\n')
f.write('}\n')
f.write('</style>\n')
f.write('<h1>Summary for ' + my_url + ' on ' + 
	my_url_date + '.</h1>')

# loop through containers to write content retrieved from my_url
for x in range(len(containers)):
	# line below corrects an odd unicode error

	f.write('<p>')
	s1=containers[x].get_text(' ', strip=True)
	s2 = str(s1.encode('ascii', 'ignore'))
	s3 = s2.split("b'")[1]
	f.write('<p>')
	f.write(s3)

f.write('\n</html>\n')
f.write('</body>\n')
f.close()

