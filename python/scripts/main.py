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



"""
IMPORTANT LINKS
https://www.smogon.com/stats/2023-06/moveset/gen9vgc2023regulationd-1760.txt
https://www.smogon.com/stats/2023-06/metagame/gen9vgc2023regulationd-1760.txt
https://www.smogon.com/stats/2023-06/leads/gen9vgc2023regulationd-1760.txt
https://www.smogon.com/stats/2023-06/gen9vgc2023regulationd-1760.txt
"""

url = "https://www.smogon.com/stats/"

def getUsages(extension):
        data_folder = path.join(getcwd(),"data")
        # extension = links[-1]
        file_path = get_formats(extension)
        file_path.sort()
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

def getMovesets():
    pass


def main():
    htmlRes = getReq(url)
    links = []

    if htmlRes:
        links = getLinks(htmlRes)

    if len(links) > 0:
        getUsages(links[-1])
        getMovesets()

            


if __name__ == "__main__":
    main()
    

'''
    - [ ] get pokemon usages
    - [ ] get pokemon movesets
    - [ ] 
    - [ ]
'''