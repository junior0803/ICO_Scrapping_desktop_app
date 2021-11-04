import gc
import re
from re import findall
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from numberact import getNumber

def coincodex():
    src = 'https://coincodex.com/sto-list/'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    req = requests.get("https://coincodex.com/api/coincodexicos/get_icos_filter/?type=sto&ico_status=all&stages_status=all&search=&stage=all&platform=all&launchpad=all&offset=0&limit=1000&rating=0&hard_cap=0&bonus=0&for_sale=0&order_by=stage_start&order_direction=desc").json()

    urls = []
    tot = len(req)
    for i in range(tot):
        urls.append("https://coincodex.com/sto/" + req[i]["slug"] + "/")

    print(len(urls))
    datas = {}

    for url in urls:
        try:
            driver = webdriver.Chrome(
                "./UI/chromedriver", options=option, desired_capabilities=capa)
            wait = WebDriverWait(driver, 20)
            driver.get(url)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'header.main-title > h1')))
            driver.execute_script("window.stop();")

            data = {}
            try:
                ico_name = driver.find_element_by_css_selector(
                    "header.main-title > h1").text
                id = str(ico_name).index("(")
                ico_symbol = ico_name[id:]
                ico_name = ico_name[:id]

                ico_description = driver.find_element_by_css_selector(
                    "div.about-box-text > p").text

                data["ICO Name"] = ico_name
                data["ICO Symbol"] = ico_symbol
                data["ICO Description"] = ico_description
            except:
                pass

            try:
                links = driver.find_elements_by_css_selector(
                    "div.about-box-links > ul > li > a")
                for link in links:
                    soc_link = link.get_attribute("href")
                    soc_text = link.text
                    data[str.capitalize(soc_text)] = soc_link


            except:
                pass

            try:
                sto_dates = driver.find_elements_by_css_selector(
                    "div.ico-timeline-value")[1].text

                # Junior patch begin
                data["STO Dates"] = sto_dates
                id = str(sto_dates).index("-")
                data["Start Date"] = sto_dates[:id - 1]
                data["End Date"] = sto_dates[id + 2:]
                # Junior patch end

                data["Current Stage"] = "STO"
            except:
                pass

            try:
                trs = driver.find_elements_by_css_selector("tr.ico-data-entry")
                for i in range(5, 8):
                    cls_text = trs[i].find_element_by_css_selector(
                        "th > span").text
                    val_text = trs[i].find_element_by_css_selector(
                        "td > span").text
                    data[cls_text] = val_text
                    # Junior patch begin
                    if cls_text in "STO Price":
                        data["STO Price Value"] = getNumber(val_text)
                    elif cls_text in "Softcap":
                        data["Softcap Value"] = getNumber(val_text)
                    elif cls_text in "Hardcap":
                        data["Hardcap Value"] = getNumber(val_text)
                    elif cls_text in "Bonuses":
                        data["Hardcap Value"] = getNumber(val_text)
                    # Junior patch end
            except:
                pass

            try:
                unkown = driver.find_elements_by_css_selector(
                    "div.token-distribution > ul > li > span")[0].text
                investors = driver.find_elements_by_css_selector(
                    "div.token-distribution > ul > li > span")[1].text
                data["Token Distribution"] = "UNKOWN " + \
                    unkown + "/" + "INVESTORS " + investors
            except:
                pass

            datas[ico_name] = data
            
        except:
            pass

        driver.quit()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/coincodex.csv")

    gc.collect()
