import requests
from bs4 import BeautifulSoap

page = requests.get("https://terraria.wiki.gg/wiki/Item_IDs#ID_list")
soap = BeautifulSoap(page.content,"html.parser")
soap.find("body",{"class":"mediawiki"})