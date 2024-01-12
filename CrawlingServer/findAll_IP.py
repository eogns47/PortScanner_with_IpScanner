import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import config
import logging
import os
import logger
from sql import insertCrawlingData

get_ip_url = config.get_ip_url

logger.setLogger()

def getAllKoreaIP():
    # Chrome 웹 드라이버 옵션 설정
    options = Options()
    options.add_argument('--headless')  # headless 모드 활성화
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")

   # 현재 스크립트 파일의 위치를 가져옴
    currentDir = os.path.dirname(__file__)
    #driver = webdriver.Chrome('~/daehoon/potatonet/findWeakOfWeb/CrawlingServer/chromedriver', options=options)

    # 상위 폴더에 있는 chromedriver 파일을 가리키는 상대 경로 설정
    chromeDriverPath = os.path.join(currentDir, 'chromedriver')
    options.binary_location= "/usr/bin/google-chrome"


    return getIpRangeByWeb(chromeDriverPath, options)


def getIpRangeByWeb(chromeDriverPath:str, options:Options):
    with webdriver.Chrome(executable_path=chromeDriverPath, options=options) as driver:
        driver.implicitly_wait(10)
        driver.get(get_ip_url)
        logging.info('Trying to get all Korea IP...')
        wait = WebDriverWait(driver, 10)

        dataTable=driver.find_element(By.CLASS_NAME,'datatable')
        table_body = dataTable.find_element(By.TAG_NAME, "tbody")
        all_rows = table_body.find_elements(By.TAG_NAME, "tr")

        allIP=[]

        for row in all_rows[:2]:
            logging.info(f'Getting Korea IP...{row.text}')
            columns = row.find_elements(By.TAG_NAME, "td")
            allIP.append(findAllIpInRange(columns[1].text, columns[2].text))

        return allIP
            

def findAllIpInRange(start:str, end:str):
    AllkoreaIP = []
    logging.info(f'Found Korea IP in range {start} to {end}')
    startIp = start.split('.')
    endIp = end.split('.')

    for i in range(int(startIp[0]), int(endIp[0])+1):
        for j in range(int(startIp[1]), int(endIp[1])+1):
            for k in range(int(startIp[2]), int(endIp[2])+1):
                for l in range(int(startIp[3]), int(endIp[3])+1):
                    ip = f'{i}.{j}.{k}.{l}'
                    AllkoreaIP.append(ip)
                    
    return AllkoreaIP

def crwalAndSaveAllKoreaIP():
    AllkoreaIp=getAllKoreaIP()
    insertCrawlingData(AllkoreaIp)

if __name__ == "__main__":  
    crwalAndSaveAllKoreaIP()





