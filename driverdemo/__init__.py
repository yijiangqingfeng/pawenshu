import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')

driver = Chrome(executable_path="chromedriver", options=chrome_options)

with open('stealth.min.js') as f:
    js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})
driver.get('https://www.bqkan.com/1_1094/')
time.sleep(5)
driver.save_screenshot('walkaround.png')

# 你可以保存源代码为 html 再双击打开，查看完整结果
source = driver.page_source
with open('result.html', 'w',encoding='utf-8') as f:
    f.write(source)