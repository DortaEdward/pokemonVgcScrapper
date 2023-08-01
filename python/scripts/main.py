import requests
from bs4 import BeautifulSoup
import re
from os import path, getcwd

import json

def txt_to_json(txt_file_path):
    table_data = []
    with open(txt_file_path, 'r') as file:
        for _ in range(5):
            next(file)

        for line in file:
            if '|' not in line:
                continue
            data = line.strip().split('|')
            if len(data) < 3:
                continue
            
            row_data = {
                'Rank': data[1].strip(),
                'Pokemon': data[2].strip(),
                'Usage': data[3].strip()
            }
            table_data.append(row_data)
    return table_data

url = "https://www.smogon.com/stats/"
data_folder = path.join(getcwd(),"data")

def getUsages(extension):
        file_path = get_formats(extension)
        file_path_url = "{}/{}/{}".format(url, extension, file_path[-1])
        table = get_table(file_path_url)
        data_path = path.join(data_folder,file_path[-1])
        create_file(table,data_path)
        if table:
            table_data = txt_to_json(data_path)
            json_data = json.dumps(table_data, indent=2)
            create_file(table,path.join(data_folder,file_path[-1]))
            with open(path.join(getcwd(),f"data/data.json"),'w') as f:
                f.write(json_data)
                f.close()

def getLinks(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    return links

def getReq(url):
    res = requests.get(url)
    links = []
    if res.status_code != 200:
        return print("Error: There was an error with the request", res.status_code)
    else:
        return res.text

def vgc_links(arr):
    links = []
    for el in arr:
        if "vgc" in el:
            links.append(el)
    return links

def get_formats(extension):
    new_url = url + "/" + extension
    data = getReq(new_url)
    soup = BeautifulSoup(data, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    links.sort()
    return vgc_links(links)


def get_table(url):
    res = getReq(url)
    return res


def create_file(data, name):
    with open(name, 'w') as f:
        f.write(data)
        f.close()


def print_els(arr):
    for el in arr:
        print(el)

def getMovesets(extension):
    file_path = get_formats(extension)
    file_path_url = "{}/{}/{}/{}".format(url,extension,"moveset", file_path[-1])
    table = get_table(file_path_url)
    print(table)


def main():
    htmlRes = getReq(url)
    links = []

    if htmlRes:
        links = getLinks(htmlRes)

    if len(links) > 0:
        # getUsages(links[-1])
        getMovesets(links[-1])

if __name__ == "__main__":
    main()
    
'''
    - [x] get pokemon usages
    - [ ] get pokemon movesets
    - [ ] 
    - [ ]
'''

"""
IMPORTANT LINKS
https://www.smogon.com/stats/2023-06/moveset/gen9vgc2023regulationd-1760.txt
https://www.smogon.com/stats/2023-06/metagame/gen9vgc2023regulationd-1760.txt
https://www.smogon.com/stats/2023-06/leads/gen9vgc2023regulationd-1760.txt
https://www.smogon.com/stats/2023-06/gen9vgc2023regulationd-1760.txt
"""

'''
 +----------------------------------------+
 | Basculin                               |
 +----------------------------------------+
 | Raw count: 514                         |
 | Avg. weight: 0.00188765971474          |
 | Viability Ceiling: 73                  |
 +----------------------------------------+
 | Abilities                              |
 | Adaptability 82.204%                   |
 | Mold Breaker 16.776%                   |
 | Rock Head  0.968%                      |
 | Rattled  0.051%                        |
 | Reckless  0.001%                       |
 +----------------------------------------+
 | Items                                  |
 | Eviolite 99.316%                       |
 | Other  0.684%                          |
 +----------------------------------------+
 | Spreads                                |
 | Adamant:252/252/0/0/0/4 64.281%        |
 | Lax:0/4/252/0/0/252 16.776%            |
 | Jolly:76/220/4/0/4/204 13.952%         |
 | Other  4.991%                          |
 +----------------------------------------+
 | Moves                                  |
 | Protect 95.592%                        |
 | Last Respects 81.718%                  |
 | Wave Crash 69.272%                     |
 | Zen Headbutt 64.281%                   |
 | Icy Wind 30.780%                       |
 | Aqua Jet 21.272%                       |
 | Soak 16.776%                           |
 | Liquidation 13.952%                    |
 | Other  6.358%                          |
 +----------------------------------------+
 | Teammates                              |
 | Sneasler 65.619%                       |
 | Thundurus 65.619%                      |
 | Chesnaught 62.386%                     |
 | Flutter Mane 62.334%                   |
 | Heatran 62.334%                        |
 | Regieleki 17.312%                      |
 | Amoonguss 10.323%                      |
 | Tornadus  9.483%                       |
 | Rillaboom  9.483%                      |
 | Chi-Yu  9.483%                         |
 | Zapdos-Galar  8.307%                   |
 +----------------------------------------+
 | Checks and Counters                    |
 +----------------------------------------+

'''