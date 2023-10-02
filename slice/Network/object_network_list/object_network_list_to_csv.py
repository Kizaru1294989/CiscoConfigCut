import csv
import json
import os


wordresearch = 'object network'
Folder = "CSV"

def object_network_list_to_csv(output_file, data):
    print('Object Network list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    current_object_group = None
    current_lines = []
    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_group is not None:
                result.append({"Object Network": current_object_group, "config": current_lines})
            current_object_group = line
            current_lines = []
        elif current_object_group is not None and not line.startswith("object"):
            current_lines.append(line)

    if current_object_group is not None:
        result.append({"Object Network": current_object_group, "config": current_lines})

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Object Network", "config"])

        for group in result:
            object_group_name = group["Object Network"].split(" ")[-1]
            lines = ';'.join(group["config"])
            writer.writerow([object_group_name, lines])

