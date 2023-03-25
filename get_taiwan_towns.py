import json

import requests
import xmltodict

import taiwan


def main():
    towns = {}
    for city in taiwan.cities:
        countycode = city['countycode']
        url = f"https://api.nlsc.gov.tw/other/ListTown1/{countycode}"
        response = requests.get(url)
        dict_data = xmltodict.parse(response.content)
        towns[countycode] = dict_data['townItems']['townItem']

    # Serializing json. ensure_ascii=False for chinese town name
    json_string = json.dumps(towns, indent=2, ensure_ascii=False)

    # Writing to file. UTF-8 mode default since Python3.15. (https://peps.python.org/pep-0686)
    with open("towns.json", "w") as outfile:
        outfile.write(json_string)


if __name__ == "__main__":
    main()
