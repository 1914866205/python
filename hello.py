from selenium.webdriver.chrome.options import Options
from selenium import webdriver
System.setProperty("webdriver.chrome.driver",
                   "D:\\360MoveData\\Users\\lenovo\\Desktop\\java\\后端\\小组作业\\20200320——Selenium\\Web自动化\\chromedriver\\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get("https://www.baidu.com")
browser.set_window_position(20, 40)
browser.set_window_size(1100, 700)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
print(browser.page_source)
