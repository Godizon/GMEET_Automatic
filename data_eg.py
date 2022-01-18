
# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def turnOffMicCam():
    # turn off Microphone
    pyautogui.moveTo(100, 500)
    pyautogui.click(100, 500)
    print(pyautogui.position())
    
    time.sleep(2)
    pyautogui.hotkey('ctrl','d')
    time.sleep(1)
    pyautogui.hotkey('ctrl','e')
    driver.implicitly_wait(3000)
    # explicit function to turn off mic and cam
#def turnOffMicCam():

    # turn off Microphone
    #time.sleep(2)
    #driver.find_element_by_xpath(
    #    '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    #driver.implicitly_wait(3000)

    # turn off camera
    #time.sleep(1)
    #driver.find_element_by_xpath(
    #    '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    #driver.implicitly_wait(3000)



def joinNow():
    # Join meet
    print(1)
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    print(1)


def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths

# create chrome instance
opt = Options()
opt.add_argument("--user-data-dir=D:\\user_data")
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
alertWords = [ "godizon.", "are you there.", "unmute yourself.", "say something.", "can you hear me.","11.","eleven.","attendance.","attendance"]
driver = webdriver.Chrome(executable_path='C:\\Users\\Administrator\\Downloads\Compressed\\chromedriver_win32\\chromedriver.exe',options=opt)
# login to Google account


# go to google meet
driver.get('https://meet.google.com/stb-tsgx-cue')
time.sleep(14)
turnOffMicCam()
# AskToJoin()
joinNow()
time.sleep(15)
print('hello')
#click  three dots
driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[5]/div/div[3]/div[1]/span/button').click()
driver.implicitly_wait(5000)
#click captions
driver.find_element_by_xpath('/html/body/div[3]/ul/li[5]/span[3]/span[1]').click()
driver.implicitly_wait(5000)
time.sleep(5)
#click english
driver.find_element_by_css_selector('#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.p23ndf.vDc8Ic.J9Nfi.iWO5td > span > div > div > span > label:nth-child(2) > div.d7L4fc.bJNwt.ftajtd > div > div.vd3tt > div').click()
driver.implicitly_wait(5000)
time.sleep(5)
#click apply
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[2]/div/span/span').click()
driver.implicitly_wait(5000)

while True:
    try:
        elems = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[7]/div/div[2]/div/span[3]/span')
        captioTextLower = str(elems.text).lower()
        for word in alertWords:
            if word in captioTextLower:
                driver.get('https://youtube.com')
                time.sleep(2)
        time.sleep(0.5)
    except (NoSuchElementException, StaleElementReferenceException):
        time.sleep(1)