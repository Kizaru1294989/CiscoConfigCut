import csv
import json
import os
from Mask.mask_cidr import masque_cidr

wordresearch = 'interface'
Folder = "CSV"



####MANAGMENT INTERFACE

def interface_list_to_csv(output_file, data):
    print('interface list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    current_object_group = None
    current_lines = []
    #found_interface = False  
    
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
            if current_object_group is not None :
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
            #found_interface = True
        
   
            
        elif  in_interface_list_block:
            #print(line)
            if line.startswith("description") :
                if line.split()[1] == "VLAN":
                    current_description = line.split()[1] + " "+ line.split()[2]+ " "+line.split()[3] 
                else :
                    description = line.split()[1:]
                    description_string = ' '.join(description)
                    current_description = description_string
                    current_vlan = "NO"

              
                current_state_interface = "active"
            elif line.startswith("shutdown") :
                current_description = "NO"
                current_state_interface = "shutdown"
                current_vlan = "NO"
                
          
                
            elif line.startswith("vlan") :
                current_vlan = "VLAN " +  line.split()[1]
                
            elif line.startswith("nameif "):
                current_nameif = line.split()[1]
                
            elif line.startswith("no")  :
                if line.split()[1] == "nameif":
                    current_nameif = "NO"
                if line.split()[1] == "security-level":
                    current_security_level = "NO"
                if line.split()[1] == "ip":
                    current_IP_address = "NO"
                    current_Mask_address = " NO"
                
                
            elif line.startswith("security-level") :
                current_security_level = "level " + line.split()[1]
                
  
            
            elif line.startswith("ip address"): 
                current_Mask_address = masque_cidr(line.split()[3]) # + MASK
                current_IP_address = line.split()[2]
                
            elif line.startswith("!") :
                in_interface_list_block = False
       
    if current_object_group is not None :
        
            result.append({"Interface": current_object_group,
                               "State" : current_state_interface,
                               "Description": current_description,
                               "VLAN": current_vlan,
                               "Nameif": current_nameif,
                               "Security Level": current_security_level,
                               "IP": current_IP_address,
                               "MASK" : current_Mask_address
                               
                               
                               })
                

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Interface", "State" , "Description" , "VLAN", "Nameif", "Security Level", "IP" , "MASK" ])

        for group in result:
            object_group_name = group["Interface"].split(" ")[-1]
            writer.writerow([object_group_name, group["State"] ,  group["Description"], group["VLAN"], group["Nameif"],group["Security Level"], group["IP"] , group["MASK"]])


