import gc
import requests
import pandas as pd


def tradingview():
    req = requests.post("https://scanner.tradingview.com/america/scan", json={"filter": [{"left": "name", "operation": "nempty"}], "options": {"lang": "en"}, "symbols": {"query": {
                        "types": []}, "tickers": []}, "columns": ["name", "description", "market_cap_basic", "number_of_employees", "sector", "volume", "High.All", "Low.All", "average_volume_30d_calc", "country", "exchange", "industry", "subtype"], "sort": {"sortBy": "name", "sortOrder": "desc"}})

    res = req.json()
    tot = res["totalCount"]

    datas = {}

    for i in range(tot):
        data = {}
        data["Ticker"] = res["data"][i]["d"][0]
        data["Name"] = res["data"][i]["d"][1]
        data["Market Cap"] = res["data"][i]["d"][2]
        data["EMPLYEES"] = res["data"][i]["d"][3]
        data["SECTOR"] = res["data"][i]["d"][4]
        data["VOL"] = res["data"][i]["d"][5]
        data["All Time High"] = res["data"][i]["d"][6]
        data["All Time Low"] = res["data"][i]["d"][7]
        data["AVG VOL(30)"] = res["data"][i]["d"][8]
        data["Country"] = res["data"][i]["d"][9]
        data["Exchange"] = res["data"][i]["d"][10]
        data["Industry"] = res["data"][i]["d"][11]
        data["Stock Type"] = res["data"][i]["d"][12]

        datas[res["data"][i]["d"][0]] = data

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/tradingview.csv")

    gc.collect()
