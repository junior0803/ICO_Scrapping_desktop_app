import gc
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from numberact import getNumber

def icomarks():
    src = 'https://icomarks.com/icos'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(
        "./UI/chromedriver", options=option)
    wait = WebDriverWait(driver, 20)

    driver.get(src)
    # wait.until(EC.presence_of_element_located(
    #     (By.CSS_SELECTOR, 'a.show-more')))
    # driver.execute_script("window.stop();")
    time.sleep(5)

    while(True):
        try:
            H = driver.execute_script('return document.body.scrollHeight;')
            driver.execute_script("window.scrollTo({}, {});".format(0, H))
            showBtn = driver.find_element_by_css_selector(
                "a.show-more")
            showBtn.click()
            time.sleep(2)
        except:
            break

    urls = []
    atags = driver.find_elements_by_css_selector("a.icoListItem__title")
    for atag in atags:
        tmp = atag.get_attribute("href")
        if("undefined" not in tmp):
            urls.append(tmp)

    print(len(urls))
    driver.quit()
    datas = {}

    for url in urls:
        try:
            driver = webdriver.Chrome(
                "./UI/chromedriver", options=option, desired_capabilities=capa)
            wait = WebDriverWait(driver, 20)
            driver.get(url)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'h1[itemprop = "name"]')))
            driver.execute_script("window.stop();")

            data = {}
            try:
                ico_name = driver.find_element_by_css_selector(
                    "h1[itemprop = 'name']").text
                ico_description = driver.find_element_by_css_selector(
                    "div.company-description").text

                data["ICO Name"] = ico_name
                data["ICO Description"] = ico_description
            except:
                pass

            try:
                divs = driver.find_elements_by_css_selector(
                    "div.icoinfo-block__item")
                for div in divs:
                    span_text = div.find_element_by_tag_name("span").text
                    span_text = str(span_text).replace(":", "")
                    if(("Links" in span_text) or (span_text == "")):
                        soc_link = div.find_element_by_tag_name(
                            "a").get_attribute("href")
                        if("facebook" in soc_link):
                            data["Facebook link"] = soc_link
                        elif("reddit" in soc_link):
                            data["Reddit link"] = soc_link
                        elif("twitter" in soc_link):
                            data["Twitter link"] = soc_link
                        elif("t.me" in soc_link):
                            data["Telegram link"] = soc_link
                        elif("medium" in soc_link):
                            data["Medium link"] = soc_link
                        elif("discord" in soc_link):
                            data["Discord link"] = soc_link
                        else:
                            data["Youtube link"] = soc_link
                    elif(("Website" in span_text) or ("White paper" in span_text) or ("MVP" in span_text)):
                        link = div.find_element_by_tag_name(
                            "a").get_attribute("href")
                        if("Website" in span_text):
                            link = str(link).replace(
                                "?utm_source=icomarks", "")
                        data[span_text] = link
                    else:
                        li_text = str(div.text).replace(span_text, "")[2:]
                        # Junior patch begin
                        if(("ICO Time" in span_text) or ("Pre-sale Time" in span_text)):
                            id = str(li_text).index("-")
                            data["Start Date"] = li_text[:id - 1]
                            data["End Date"] = li_text[id + 2:]
                        elif("ICO Price" in span_text):
                            data[span_text] = li_text
                            data["ICO Price Value"] = getNumber(li_text)
                        elif("Soft cap" in span_text):
                            data[span_text] = li_text
                            data["Soft cap Value"] = getNumber(li_text)
                        elif("Hard cap" in span_text):
                            data[span_text] = li_text
                            data["Hard cap Value"] = getNumber(li_text)
                        elif("Available for sale" in span_text):
                            data[span_text] = li_text
                            data["Available value for sale"] = getNumber(li_text)
                        elif("Total supply" in span_text):
                            data[span_text] = li_text
                            data["Total supply Value"] = getNumber(li_text)
                        elif("Pre-sale Price" in span_text):
                            id = str(li_text).index("=")
                            data[span_text] = li_text                            
                            data["Pre-sale Price Value"] = getNumber(li_text[:id + 2])
                        # Junior patch end
                        else:
                            data[span_text] = li_text
            except:
                pass

            datas[ico_name] = data
        except:
            pass

        driver.quit()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/icomarks.csv")

    gc.collect()
