import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

global url
def url():
    url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=190991'
    return url

global Chrome_selenium_setting
def Chrome_selenium_setting():
    # from scrapy.utils.project import get_project_settings
    # re_text


    chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    driver_path = f'{chrome_version}\chromedriver.exe'

    if os.path.exists(driver_path):
        print(f'chrome driver is installed : {driver_path}')
    else:
        print(f'chrome driver is installed : {driver_path}')
        print(f'install the chrome driver > version : {chrome_version}')
        print(f'install complete > {driver_path}')
        chromedriver_autoinstaller.install(True)
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(executable_path = driver_path,
                                chrome_options=chrome_options)
    return driver

# driver = Chrome_selenium_setting()



def selenium_movement():
    driver = Chrome_selenium_setting()
    click_css = '#_TopArea > div.first_mv_list.current_mv_list._mv_default_list > div > ul > li:nth-child(2) > a > img'
    driver.get(url())
    body = driver.fine_element_by_css(click_css)
    body.click()
    visitors_css = '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(10) > div > p.count'
    visitors = driver.find_element_by_css(visitors_css)
    href = visitors.get_attribute('href')
    print(href)
    driver.quit()
    
selenium_movement()

