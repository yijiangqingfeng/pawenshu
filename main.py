from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    server = 'https://www.bqkan.com'
    target = 'https://www.bqkan.com/1_1094/'
    req = requests.get(url = target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div',class_='listmain')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    print(a)
    #for item in a:
   #     print(item.string,server + item.get('href'))
    #print(a[0])