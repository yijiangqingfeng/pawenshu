from bs4 import BeautifulSoup
import sys
import requests


class downloader(object):
    def __init__(self):
        self.server = 'https://www.bqkan.com'
        self.target = 'https://www.bqkan.com/1_1094/'
        self.names = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for item in a[15:]:
            self.names.append(item.string)
            self.urls.append(self.server + item.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='showtxt')
        div = div[0].text.replace('\xa0' * 8, '\n\n')
        return div

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer((dl.names[i]), '一念永恒.txt', dl.get_contents((dl.urls[i])))
        sys.stdout.write(" 已下载：%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('《一念永恒》下载完成')
