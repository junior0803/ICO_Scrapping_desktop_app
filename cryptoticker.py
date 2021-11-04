import gc
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from numberact import getNumber

def cryptoticker():
    src = 'https://cryptoticker.io/en/top-4-upcoming-airdrops-july-2021/'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")

    driver = webdriver.Chrome("./UI/chromedriver", options=option)
    wait = WebDriverWait(driver, 20)

    driver.get(src)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'h2[id*="h-1"]')))
    driver.execute_script("window.stop();")

    datas = {}

    try:
        data = {}
        name1 = driver.find_element_by_css_selector("h2[id*='h-1']").text
        data["Name"] = name1[3:]

        data["About the Project"] = driver.find_element_by_css_selector(
            "p:nth-child(10)").text

        ul1 = driver.find_elements_by_css_selector("ul.nitro-offscreen")[0]
        lis = ul1.find_elements_by_css_selector("li > strong")
        print(lis[0].tag_name)
        data["Start date"] = str(lis[0].text).split(":")[1].strip()
        data["Total Airdrop Amount"] = str(lis[1].text).split(":")[1].strip()
        # Junior patch begin
        data["Total Airdrop Amount Value"] = getNumber(data["Total Airdrop Amount"] )
        # Junior patch end
        data["Number of Winners"] = str(lis[2].text).split(":")[1].strip()

        data["Guide"] = driver.find_elements_by_css_selector(
            "ol.nitro-offscreen")[0].text

        datas[name1[3:]] = data

        data = {}
        name2 = driver.find_element_by_css_selector("h2[id*='h-2']").text
        data["Name"] = name2[3:]

        data["About the Project"] = driver.find_element_by_css_selector(
            "p:nth-child(20)").text

        ul1 = driver.find_elements_by_css_selector("ul.nitro-offscreen")[1]
        lis = ul1.find_elements_by_tag_name("li")
        data["Start date"] = str(lis[0].text).split(":")[1].strip()
        data["Total Airdrop Amount"] = str(lis[1].text).split(":")[1].strip()

        # Junior patch begin
        data["Total Airdrop Amount Value"] = getNumber(data["Total Airdrop Amount"] )
        # Junior patch end

        data["Number of Winners"] = str(lis[2].text).split(":")[1].strip()

        data["Guide"] = driver.find_elements_by_css_selector(
            "ol.nitro-offscreen")[1].text

        datas[name2[3:]] = data

        data = {}
        name3 = driver.find_element_by_css_selector("h2[id*='h-3']").text
        data["Name"] = name3[3:]

        data["About the Project"] = (driver.find_element_by_css_selector(
            "p:nth-child(31)").text + "\n" + driver.find_element_by_css_selector("p.nitro-offscreen:nth-child(32)").text)

        ul1 = driver.find_elements_by_css_selector("ul.nitro-offscreen")[2]
        lis = ul1.find_elements_by_tag_name("li")
        data["Start date"] = str(lis[0].text).split(":")[1].strip()
        data["Total Airdrop Amount"] = str(lis[1].text).split(":")[1].strip()
        # Junior patch begin
        data["Total Airdrop Amount Value"] = getNumber(data["Total Airdrop Amount"] )
        # Junior patch end

        data["Number of Winners"] = str(lis[2].text).split(":")[1].strip()

        data["Guide"] = driver.find_elements_by_css_selector(
            "ol.nitro-offscreen")[2].text

        datas[name3[3:]] = data

        data = {}
        name4 = driver.find_element_by_css_selector("h2[id*='h-4']").text
        data["Name"] = name4[3:]

        data["About the Project"] = driver.find_element_by_css_selector(
            "p:nth-child(43)").text

        ul1 = driver.find_elements_by_css_selector("ul.nitro-offscreen")[3]
        lis = ul1.find_elements_by_tag_name("li")
        data["Start date"] = str(lis[0].text).split(":")[1].strip()
        data["Total Airdrop Amount"] = str(lis[1].text).split(":")[1].strip()
        data["Number of Winners"] = str(lis[2].text).split(":")[1].strip()
        # Junior patch begin
        data["Total Airdrop Amount Value"] = getNumber(data["Total Airdrop Amount"] )
        # Junior patch end
        data["Guide"] = driver.find_elements_by_css_selector(
            "ol.nitro-offscreen")[3].text

        datas[name4[3:]] = data
    except:
        pass

    driver.quit()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/crytoticker.csv")

    gc.collect()
