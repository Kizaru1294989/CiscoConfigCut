import csv
import json
import os


wordresearch = 'interface'
Folder = "CSV"

 

def interface_list_to_csv(output_file, data):
    print('interface list catch !')

    Path = os.path.join(Folder, output_file)
    result = []
    current_object_group = None
    current_lines = []

    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_group is not None:
                result.append({"interface": current_object_group, "content": current_lines})
            current_object_group = line
            current_lines = []
        elif current_object_group is not None:
            current_lines.append(line)

    if current_object_group is not None:
        print(line)
        result.append({"interface": current_object_group, "content": current_lines})

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["interface-Names", "content"])

        for group in result:
            object_group_name = group["interface"].split(" ")[-1]
            lines = ';'.join(group["content"])
            writer.writerow([object_group_name, lines])
