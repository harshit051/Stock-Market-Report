import requests
import bs4
from bs4 import BeautifulSoup

company_name = input("Enter the company name: ").strip()

url = "https://www.moneycontrol.com/stocks/marketstats/nse-mostactive-stocks/nifty-50-9/"

r = requests.get(url)

soup = bs4.BeautifulSoup(r.text,'lxml')

data = soup.select('tr td')
anchor = soup.find_all('a')

for i in range(len(data)):
    if data[i].find('a'):
        if str.upper(data[i].find('a').text) == str.upper(company_name):
            l = data[i].find('a').get('href')
            # print(data[i].find('a').get('href'))

url1 = str(l)
r1 = requests.get(url1)
soup = bs4.BeautifulSoup(r1.text,'lxml')
data1 = soup.find_all('div',{'class':"indimprice"})
for i in range(len(data1)):
    if data1[i].find('div',{'id':'bsecp'}) :
        result = data1[i].find_all('div',{'id':'bsecp'})
        for j in range(len(result)):
            print('BSE : ',result[j].text)
    if data1[i].find('div',{'id':'nsecp'}):
        result = data1[i].find_all('div', {'id': 'nsecp'})
        for j in range(len(result)):
            print('NSE : ',result[j].text)



input()