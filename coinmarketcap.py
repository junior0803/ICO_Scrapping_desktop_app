import gc
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def coinmarketcap():
    src = ['https://coinmarketcap.com/airdrop/ongoing/',
           'https://coinmarketcap.com/airdrop/upcoming/',
           'https://coinmarketcap.com/airdrop/ended/',
           'https://coinmarketcap.com/airdrop/ended/?page=2']
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    urls = []
    for i in range(4):
        driver = webdriver.Chrome(
            "./UI/chromedriver", options=option, desired_capabilities=capa)
        wait = WebDriverWait(driver, 20)
        driver.get(src[i])
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'table.cmc-table > tbody > tr > td > a')))
        driver.execute_script("window.stop();")

        time.sleep(3)
        atags = driver.find_elements_by_css_selector(
            "table.cmc-table > tbody > tr > td > a")
        for atag in atags:
            urls.append(atag.get_attribute("href"))

        driver.quit()

    print(len(urls))
    datas = {}

    for url in urls:
        try:
            driver = webdriver.Chrome(
                "./UI/chromedriver", options=option)
            wait = WebDriverWait(driver, 20)
            driver.get(url)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'h2.h1')))
            driver.execute_script("window.stop();")

            data = {}

            try:
                name = driver.find_element_by_css_selector("h2.h1").text
                symbol = driver.find_element_by_css_selector(
                    "small.nameSymbol").text
                name = str(name).replace(symbol, "")

                data["Name"] = name
                data["Symbol"] = symbol

                title = driver.find_element_by_css_selector(
                    "div.stage-header-title > span").text
                data["Title"] = title

                description = driver.find_element_by_css_selector(
                    "div.right-join-box > div> div > p").text
                data["Description"] = description
            except:
                pass

            try:
                atags = driver.find_elements_by_css_selector("a.link-button")
                for atag in atags:
                    soc_link = atag.get_attribute("href")
                    soc_text = atag.text

                    data[soc_text] = soc_link

                contracts = driver.find_element_by_css_selector(
                    "div.contractsRow > div.content > div > a").text
                data["Contracts"] = contracts

                tags_text = ""
                tags = driver.find_elements_by_css_selector(
                    "ul.content > li > a.cmc-link > div.tagBadge")
                for tag in tags:
                    tags_text += (tag.text + ", ")

                data["Tags"] = tags_text[:-2]
            except:
                pass

            try:
                seDate = driver.find_element_by_css_selector(
                    "div.stage-header-date > span").text
                id = seDate.index(",", 25)
                seDate = seDate[:id - 1]
                id = seDate.index("-")

                data["Start Date"] = seDate[:id - 1]
                data["End Date"] = seDate[id + 2:]

                divs = driver.find_elements_by_css_selector(
                    "div.detailTable > div")
                for div in divs:
                    spans = div.find_elements_by_tag_name("span")
                    data[spans[0].text] = spans[1].text
            except:
                pass

            try:
                detail = driver.find_element_by_css_selector(
                    "div.markdown-desc > div").text
                data["How to Participate?"] = detail
            except:
                pass

            datas[name] = data
        except:
            pass

        driver.quit()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/coinmarketcap.csv")

    gc.collect()
