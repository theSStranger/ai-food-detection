import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 

query = "serdar"
htmldata = getdata("https://www.google.com/search?q=" + query + "&tbm=isch") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    if(item.parent.class == "bRMDJf islir"):
       print(item['src'])
