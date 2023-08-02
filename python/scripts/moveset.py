from os import path, getcwd
import json
file_path = path.join(getcwd(),'python/data/moveset/gen9vgc2023regulationd-1760.txt')

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



def main():
    with open(file_path, 'r') as file:
        lines = file.read()

    parsed_data = parse_table_data(lines)
    # json_data = json.dumps(parsed_data, indent=2)


main()
'''