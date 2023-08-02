import requests
from bs4 import BeautifulSoup
import re
from os import path, getcwd
import json

url = "https://www.smogon.com/stats/"
cd = path.dirname(path.abspath(__file__))
data_folder = path.join(cd,"python/data") 

def moveset_to_json(file_path):
    pass
    - [ ] 
def usage_to_json(file_path):
    table_data = []
    with open(file_path, 'r') as file:
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

def getUsages(extension):
        file_path = get_formats(extension)
        file_path_url = "{}/{}/{}".format(url, extension, file_path[-1])
        table = get_table(file_path_url)
        file_destination = path.join(data_folder,file_path[-1])
        create_file(table,file_destination)
        if table:
            table_data = usage_to_json(file_destination)
            json_data = json.dumps(table_data, indent=2)
            create_file(table,path.join(data_folder,f'usages/{file_path[-1]}'))
            file_path[-1] = file_path[-1].replace('txt','json')
            with open(path.join(data_folder,f'usages/{file_path[-1]}'),'w') as f:
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
    smogon_file = get_formats(extension)
    smogon_url = "{}/{}/{}/{}".format(url,extension,"moveset", smogon_file[-1])
    file_path = path.join(getcwd(),"python/data/{}".format("moveset/"+smogon_file[-1]))
    table = get_table(smogon_url)
    with open(file_path,'w') as f:
        f.write(table)
        f.close()
    
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