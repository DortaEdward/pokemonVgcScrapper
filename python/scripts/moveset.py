from os import path, getcwd
import json

file_path = path.join(getcwd(),'python/data/moveset/gen9vgc2023regulationd-1760.txt')
row_sep = "+"
keys = ['Abilities','Moves','Teammates','Spreads','Items']

def split(file_path):
    with open(file_path,'r') as file:
        cut = []
        for x,line in enumerate(file):
            
            if line.startswith(' +'):
                cut.append(x)          
        file.close()
    return cut

def key_index(file):
    with open(file_path,'r') as file:
        key_value = []
        for x,line in enumerate(file):   
            for key in keys:
                if key in line:
                    value = {
                        "index":x,
                        "key":key
                    }
                    key_value.append(value)
        file.close()    
    return key_value



def parse_data(cut_arr,key_index, file_path):
    final_data = []
    with open(file_path,'r') as file:
        for i,line in enumerate(file):
            temp_data = {}
            active = False
            if i in cut_arr:
                active = True
                continue
            for item in key_index:
                if item['index'] == i:
                    key = item['key']
                    temp_data[key] = []
                    final_data.append(temp_data)
                
        print(final_data)
        file.close()

def main():
    cut_arr = split(file_path)
    ki = key_index(file_path)
    parse_data(cut_arr,ki,file_path)

main()

'''
def parse_table_data(lines):
    lines = lines.split(" +----------------------------------------+ ")
    lines_sep = []
    for i,line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        if line.startswith("+"):
            continue
        line = line.replace('|','').strip()
        line = line.split()
        print("Line: ",line)
        # if len(line) > 2:
        #     new_line = []
        #     new_line.append(line[0] + ' ' + line[1])
        #     new_line.append(line[2])
            
        #     line = new_line
            
        lines_sep.append(line)
        
    sections = [lines_sep[i:i+8] for i in range(0, len(lines_sep), 8)]
    section_dicts = []

    for section in sections:
        section_name = " ".join(section[0])
        section_data = {}
        for i in range(2, len(section)):
            section_data[section[i][0]] = section[i][1:]
        section_dict = {section_name: section_data}
        section_dicts.append(section_dict)

    # Combine all sections into a single list of dictionaries
    result = {}
    for section_dict in section_dicts:
        result.update(section_dict)

    # Convert to a JSON object
    json_object = json.dumps(result, indent=4)

    # Write JSON object to a file
    with open('output.json', 'w') as file:
        file.write(json_object)

        
        =========
start = False
        key_picked = None
        obj = {}
        for line in f:
            if len(line) > 2 and line[1] == row_sep:
                if not start:
                    start = True
                else:
                    start = False
            else:
                if key_picked == None:
                    for key in keys:
                        if key in line:
                            key_picked = key
                else:
                    while line.
                    print('passed')
=================================
   lines = table_data.strip().split("\n")
    data_arr = []
    current_section = None

    for line in lines:
        data_dict = {}
        temp_dict = {}
        if line[1] == "|":
            parts = line.strip("| ").split(":")
            if len(parts) == 2:
                data_key = parts[0].strip()
                data_value = parts[1].strip()
                if current_section is None:
                    current_section = data_key
                    data_dict[current_section] = {}
                else:
                    temp_dict[data_key] = data_value
                    data_dict[current_section]= temp_dict
            elif len(parts) == 1 and current_section is not None:
                data_value = parts[0].strip()
                if current_section not in data_dict:
                    data_dict[current_section] = []
                data_dict[current_section] = data_value
            data_arr.append(data_dict)
    
    for data in data_arr:
        print(data)
    return data_arr
'''