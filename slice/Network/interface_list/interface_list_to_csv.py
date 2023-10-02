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
    found_interface = False  
    
    current_description = None
    current_vlan = None
    current_nameif = None
    current_security_level = None
    current_IP_address = None
    current_Mask_address = None
    current_state_interface = None
    
    in_interface_list_block = True
    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_group is not None:
                result.append({"Interface": current_object_group,
                               "State" : current_state_interface,
                               "Description": current_description,
                               "VLAN": current_vlan,
                               "Nameif": current_nameif,
                               "Security Level": current_security_level,
                               "IP": current_IP_address,
                               "MASK" : current_Mask_address
                               
                               
                               })
            current_object_group = line
            current_description = None
            current_vlan = None
            current_nameif = None
            current_security_level = None
            current_IP_address = None
            current_Mask_address = None
            current_state_interface = None
            
            in_interface_list_block = True
            
        elif in_interface_list_block:
            if line.startswith("description") :
                current_description = line.split()[1]
              
                current_state_interface = "active"
            elif line.startswith("shutdown") :
                current_description = "No"
                current_state_interface = "shutdown"
                
            elif line.startswith("vlan") :
                current_vlan = line.split()[1]
            elif line.startswith("nameif "):
                current_nameif = line.split()[1]
            elif line.startswith("security-level") :
                current_security_level = line.split()[1]
            elif line.startswith("ip address"): # + MASK
                current_Mask_address = line.split()[3]
                current_IP_address = line.split()[2] 
                in_interface_list_block = False

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Interface", "State" , "Description" , "VLAN", "Nameif", "Security Level", "IP" , "MASK" ])

        for group in result:
            object_group_name = group["Interface"].split(" ")[-1]
            writer.writerow([object_group_name, group["State"] ,  group["Description"], group["VLAN"], group["Nameif"],group["Security Level"], group["IP"] , group["MASK"]])


