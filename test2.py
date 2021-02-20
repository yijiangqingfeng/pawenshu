from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = 'https://www.runoob.com/w3cnote/android-tutorial-intro.html'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('ul', class_='membership')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    # print(a)
    b = []
    c = []
    for item in a:
        b.append(item.get('href'))
        c.append(item.string)
    with open("resource.txt", 'w', encoding="utf-8") as f:
        for i in range(len(b)):
            f.write(c[i] + " ")
            f.write(b[i] + '\n')
    # for i1 in range(len(b)):
    #     with open("resource2.txt", 'a', encoding="utf-8") as f1:
    #         t=b[i1]
    #         req1 = requests.get(url=t)
    #         html1 = req.text
    #         div_bf1 = BeautifulSoup(html1)
    #         div1 = div_bf1.find_all('div', class_='container main')
    #         #print(div1)
    #         f1.write(str(div1))
