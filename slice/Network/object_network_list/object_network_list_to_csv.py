import csv
import json
import os


wordresearch = 'object network'
Folder = "CSV"

def object_network_list_to_csv(output_file, data):
    print('Object Network list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    current_object_network = None
    current_lines = []
    current_host= None
    current_description = None
    current_mask = None
    found_service = False
    in_network_block = True
    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_network is not None:
                result.append({"Object Network": current_object_network, 
                               "Host": current_host,
                               "Mask" : current_mask,
                               "Description" : current_description
                               })
            current_object_network = line
            current_host = None
            current_description = None
            current_mask = None
            
            in_network_block = True
            
        elif in_network_block:
            if line.startswith("host") :
                current_host = line.split()[1]
                current_mask = "/32"
            elif line.startswith("subnet") :
                current_host = line.split()[1]
                current_mask = line.split()[2]
            elif line.startswith("description"):
                current_description = line[len("description "):]
                in_network_block = False
  
                
                
  

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Object Network", "Host" , "Mask" , "Description"])

        for group in result:
            object_group_name = group["Object Network"].split(" ")[-1]
            writer.writerow([object_group_name, group["Host"], group["Mask"], group["Description"],])

