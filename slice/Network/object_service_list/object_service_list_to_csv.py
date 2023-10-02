import csv
import os

wordresearch = 'object service'
Folder = "CSV"

def object_service_list_to_csv(output_file, data):
    print('Object Service list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    current_object_service = None
    current_protocol = None
    current_destination = None
    current_description = None
    in_service_block = False

    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_service is not None:
                result.append({"Object Service": current_object_service,
                               "Service": current_protocol,
                               "Destination": current_destination,
                               "Description": current_description})
            current_object_service = line
            current_protocol = None
            current_destination = None
            current_description = None
            in_service_block = True
        elif in_service_block:
            if line.startswith("service"):
                #print(line)
                current_protocol = line.split()[1]
                current_destination = line.split()[4]  
            elif line.startswith("description"):
                current_description = line[len("description "):]
                in_service_block = False

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Object Service", "Service" , "Destination", "Description"])

        for group in result:
            object_group_name = group["Object Service"].split(" ")[-1]
            writer.writerow([object_group_name, group["Service"], group["Destination"], group["Description"]])
