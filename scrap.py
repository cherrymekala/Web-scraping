import requests
from bs4 import BeautifulSoup
import csv

url="https://www.bikewale.com/bmw-bikes/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

l1=[]
link=soup.findAll('div',class_='zkBALk o-bXKmQE')

with open('l.csv','w') as csv_file:
	w=csv.writer(csv_file)
	w.writerow(link)
	
