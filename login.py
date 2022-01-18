from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--user-data-dir=D:\\user_data")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(executable_path='C:\\Users\\Administrator\\Downloads\Compressed\\chromedriver_win32\\chromedriver.exe',options=options)
driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
