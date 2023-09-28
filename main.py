import json

import requests
import xmltodict


def fetch(url):
    response = requests.get(url)
    return xmltodict.parse(response.content)


def fetchCounties():
    # reference: https://data.gov.tw/dataset/101905
    url = "https://api.nlsc.gov.tw/other/ListCounty"
    data = fetch(url)
    return data['countyItems']['countyItem']


def fetchTowns(countycode):
    # reference: https://data.gov.tw/dataset/102011
    url = f"https://api.nlsc.gov.tw/other/ListTown1/{countycode}"
    data = fetch(url)
    return data['townItems']['townItem']


def main():
    counties = fetchCounties()

    towns = {}
    for county in counties:
        countycode = county['countycode']
        towns[countycode] = fetchTowns(countycode)

    # Serializing json. ensure_ascii=False for chinese countyname and townname
    json_string_counties = json.dumps(counties, indent=2, ensure_ascii=False)
    json_string_towns = json.dumps(towns, indent=2, ensure_ascii=False)

    # Writing to file. UTF-8 mode default since Python3.15. (https://peps.python.org/pep-0686)
    with open("Taiwan/counties.json", "w") as outfile_counties:
        outfile_counties.write(json_string_counties)
    with open("Taiwan/towns.json", "w") as outfile_towns:
        outfile_towns.write(json_string_towns)


if __name__ == "__main__":
    main()
