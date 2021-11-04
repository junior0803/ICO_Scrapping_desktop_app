import gc
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from numberact import getNumber

def tradingeconomics():
    src = 'https://tradingeconomics.com/matrix'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(
        "./UI/chromedriver", options=option, desired_capabilities=capa)
    wait = WebDriverWait(driver, 20)

    driver.get(src)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "table[id*='ContentPlaceHolder']")))
    driver.execute_script("window.stop();")

    datas = {}
    trs = driver.find_elements_by_css_selector(
        "table[id*='ContentPlaceHolder'] > tbody > tr")

    for tr in trs:
        data = {}
        try:
            tds = tr.find_elements_by_tag_name("td")
            cntry = tds[0].text
            con1 = tds[1].text
            con2 = tds[2].text
            con3 = tds[3].text
            con4 = tds[4].text
            con5 = tds[5].text
            con6 = tds[6].text
            con7 = tds[7].text
            con8 = tds[8].text
            con9 = tds[9].text
            con10 = tds[10].text

            data["Country"] = cntry
            data["GDP"] = con1
            data["GDP YoY %"] = getNumber(con2)
            data["GDP QoQ %"] = getNumber(con3)
            data["Interest rate % "] = getNumber(con4)
            data["Inflation rate %"] = getNumber(con5)
            data["Jobless rate % "] = getNumber(con6)
            data["Gov. Budget % "] = getNumber(con7)
            data["Debt/GDP %"] = getNumber(con8)
            data["Current Account"] = con9
            data["Population"] = con10

        except:
            pass

        datas[cntry] = data

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/tradingeconomics.csv")

    driver.quit()

    gc.collect()
