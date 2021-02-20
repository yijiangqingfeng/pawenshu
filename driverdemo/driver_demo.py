import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')

wb = Chrome(executable_path="chromedriver", options=chrome_options)

with open('stealth.min.js') as f:
    js = f.read()

wb.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

wb.execute('get', {'url': 'https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?open=login'})
wb.maximize_window()
wb.switch_to.frame("contentIframe")
username = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//*[@id="root"]/div/form/div[1]/div[1]/div/div/div/input'
})['value']
password = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//*[@id="root"]/div/form/div[1]/div[2]/div/div/div/input'
})['value']
login_in = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//*[@id="root"]/div/form/div[3]/span'
})['value']
username._execute('sendKeysToElement', {'text': '13752011679',
                                        'value': ''})
time.sleep(1)
password._execute('sendKeysToElement', {'text': 'Zzx20010509',
                                        'value': ''})
time.sleep(1)
login_in._execute('clickElement')
time.sleep(1)
wb.switch_to.parent_frame()
time.sleep(1)
search_input = wb.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div/div[2]/input')
search_input._execute('sendKeysToElement', {'text': '知识产权'})
btn = wb.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div/div[3]')
time.sleep(2)
btn._execute('clickElement')
time.sleep(5)
all_select=wb.find_element_by_xpath('//*[@id="AllSelect"]')
all_download=wb.find_element_by_xpath('//*[@id="_view_1545184311000"]/div[2]/div[4]/a[3]')
all_select.click()
time.sleep(2)
all_download.click()
