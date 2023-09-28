import csv
import json
import os


wordresearch = 'object-group'
Folder = "CSV"

def object_group_to_csv(output_file, data):
    print('Object-Group list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    current_object_group = None
    current_lines = []
    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_group is not None:
                result.append({"object-group": current_object_group, "lines": current_lines})
            current_object_group = line
            current_lines = []
        elif current_object_group is not None and not line.startswith("object"):
            current_lines.append(line)

    if current_object_group is not None:
        result.append({"object-group": current_object_group, "lines": current_lines})

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["object-group-Names", "lines"])

        for group in result:
            object_group_name = group["object-group"].split(" ")[-1]
            lines = ';'.join(group["lines"])
            writer.writerow([object_group_name, lines])

