import gc
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def bravenewcoin():
    src = 'https://bravenewcoin.com/events'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(
        "./UI/chromedriver", options=option, desired_capabilities=capa)
    wait = WebDriverWait(driver, 20)

    driver.get(src)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'button.ladda-button')))
    driver.execute_script("window.stop();")

    while(True):
        try:
            btn = driver.find_element_by_css_selector("button.ladda-button")
            btn.click()
            time.sleep(2)
        except:
            break

    urls = []
    atags = driver.find_elements_by_css_selector("div.event-name > a")
    for atag in atags:
        tmp = atag.get_attribute("href")
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
                (By.CSS_SELECTOR, 'div.event > div > div:nth-child(2) > h1')))
            driver.execute_script("window.stop();")

            data = {}

            try:
                event_name = driver.find_element_by_css_selector(
                    "div.event > div > div:nth-child(2) > h1").text
                data["Event Name"] = event_name

                event_date = driver.find_elements_by_css_selector(
                    "div.event.d-none div.event-detail > p")[0].text

                event_date = str(event_date).replace("\n", " ")
                id = str(event_date).index("-")

                data["Start Date"] = event_date[:id - 1]
                data["End Date"] = event_date[id + 2:]

                location = driver.find_element_by_css_selector(
                    "div.event.d-none p.location > span").text
                data["Location"] = location
            except:
                pass

            try:
                website = driver.find_element_by_css_selector(
                    "div.event.d-none a.btn-outline-primary").get_attribute("href")
                data["Website"] = website

                bTicket = driver.find_element_by_css_selector(
                    "div.event.d-none div.event-action > a").get_attribute("href")
                data["Buy Ticket"] = bTicket

                tags = driver.find_elements_by_css_selector(
                    "div.event.d-none p.article-tags >a")
                article_tag = ""
                for tag in tags:
                    article_tag += (tag.text + ", ")
                data["Article Tags"] = article_tag[:-2]
            except:
                pass

            try:
                description = driver.find_elements_by_css_selector(
                    "div.event.d-none > div > div:nth-child(2) > p")[1].text
                description += ("\n" + driver.find_element_by_css_selector(
                    "div.event.d-none markdown > p").text)
                data["Description"] = description
            except:
                pass

            datas[event_name] = data
        except:
            pass

        driver.quit()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/bravenewcoin.csv")

    gc.collect()
