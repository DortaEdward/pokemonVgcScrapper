import requests
from bs4 import BeautifulSoup
import re
import json

def parse_table_line(line):
    # Function to parse each line of the table and extract the values
    return re.findall(r'\S+', line)

def txt_table_to_json(txt_file_path):
    table_data = []
    with open(txt_file_path, 'r') as file:
        # Skip the first two lines that contain non-tabular information
        next(file)
        next(file)

        # Skip the header line (we don't need it)

        for line in file:
            # Remove unwanted characters (+, -, |) from the line
            cleaned_line = line.replace('+', '').replace('-', '').replace('|', '').strip()
            row = parse_table_line(cleaned_line)

            # Ensure the row has enough elements before parsing
            if len(row) >= 6:
                # Convert the row data into a dictionary using appropriate keys
                row_data = {
                    "rank": row[0],
                    "name": row[1],
                    "raw": row[2],
                    "percent": row[3],
                    "real": row[4],
                    "percent_two": row[5]
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


def main():
    htmlRes = getReq(url)
    links = []

    if htmlRes:
        links = getLinks(htmlRes)

    if len(links) > 0:
        extension = links[-1]
        file_path = get_formats(extension)
        file_path.sort()
        file_path_url = "{}/{}/{}".format(url, extension, file_path[-1])
        table = get_table(file_path_url)
        print(table)
        if table:
            create_file(table,file_path[-1])
            txt_file_path = f"./{file_path[-1]}"
            table_data = txt_table_to_json(txt_file_path)
            json_data = json.dumps(table_data, indent=2)
            print(json_data)


if __name__ == "__main__":
    main()
    
