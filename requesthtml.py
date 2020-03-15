#Sample : http://requests-html.kennethreitz.org/
# pip install  requests_html
from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://python.org/')


#Grab a list of all links on the page, as–is (anchors excluded):
print(r.html.links)

#Grab a list of all links on the page, in absolute form (anchors excluded):