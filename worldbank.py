import gc
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def worldbank():
    src = 'https://data.worldbank.org/country'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(
        "./UI/chromedriver", options=option, desired_capabilities=capa)
    wait = WebDriverWait(driver, 20)

    driver.get(src)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'section > ul > li > a')))
    driver.execute_script("window.stop();")

    urls = []
    atags = driver.find_elements_by_css_selector("section > ul > li > a")
    for atag in atags:
        tmp = atag.get_attribute("href")
        if("undefined" not in tmp):
            urls.append(tmp)

    driver.quit()
    datas = {}

    for url in urls:
        try:
            driver = webdriver.Chrome(
                "./UI/chromedriver", options=option, desired_capabilities=capa)
            wait = WebDriverWait(driver, 20)
            driver.get(url)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.location')))
            driver.execute_script("window.stop();")

            data = {}

            location = driver.find_element_by_css_selector(
                "span.location").text
            csv_url = driver.find_element_by_css_selector(
                "div.download > p > a:nth-child(1)").get_attribute("href")
            data["CSV_Url"] = csv_url

            src = driver.find_element_by_css_selector(
                "a.links").get_attribute("href")

            req = requests.get(src)
            bsText = BeautifulSoup(req.content, "html.parser")
            trs = bsText.find_all("tr", class_="rowdata")

            for tr in trs:
                head_text = tr.find("td", class_="header").text
                divs = tr.find_all("div", class_="spacer2")
                data[str(head_text + "1990")] = divs[0].text
                data[str(head_text + "2000")] = divs[1].text
                data[str(head_text + "2010")] = divs[2].text
                data[str(head_text + "2020")] = divs[3].text

            datas[location] = data
        except:
            pass

        driver.quit()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/worldbank.csv")

    gc.collect()
