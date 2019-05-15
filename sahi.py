from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/DailyDeal.aspx?name=DailyDeal&cm_sp=Homepage_Dailydeal-_--_-05152019'


#  opnening up connection , grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML PARSING
 page_soup = soup(page_html, "html.parser")

 containers = page_soup.findAll("div" , {"class": "item-container"})

 