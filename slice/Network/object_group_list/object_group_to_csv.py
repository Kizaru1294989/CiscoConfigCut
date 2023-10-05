import csv
import json
import os

wordresearch = 'object-group'
Folder = "CSV"

def object_group_to_csv(output_file, data):
    print('object group list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    current_object_group = None
    current_lines = []
    found_interface = False  
    
    current_type = None
    current_description = None
    current_object = ""
    current_object_number = 0
    
    in_object_group_list_block = False  
    
    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
            if current_object_group is not None:
                result.append({"Object-Group": current_object_group,
                               "Type" : current_type,
                               "Description" : current_description,
                               "Number Object" : str(current_object_number) + " Group",
                               "Object" : current_object,
                               })
            current_object_group = line
            current_description = "NO"
            current_object = ""
            current_object_number = 0
            current_type = line.split()[1]
            
            in_object_group_list_block = True
            
        elif in_object_group_list_block:
            
            if line.startswith("description") :
                description = line.split()[1:]
                description_string = ''.join(description)
                current_description = description_string
            elif current_type == "network":
                obj = line.split()[2:]
                obj_string = ' '.join(obj)
                current_object += obj_string + " | "
                current_object_number += 1
            elif current_type == "service":
                if line.split()[1] == "object":
                    obj = line.split()[2:]
                    obj_string = ' '.join(obj)
                    current_object += obj_string + " | "
                    current_object_number += 1
                else:
                    obj = line.split()[1:]
                    obj_string = ' '.join(obj)
                    current_object += obj_string + " | "
                    current_object_number += 1
                    
            if line.startswith("access"):
                result.append({"Object-Group": current_object_group,
                               "Type" : current_type,
                               "Description" : current_description,
                               "Number Object" : str(current_object_number) + " Group",
                               "Object" : current_object,
                               })
                # Stop processing this object-group when an access-list is encountered
                in_object_group_list_block = False
               
                
            

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["Object-Group","Type" , "Description" ,"Number Object" ,  "Object"  ])
        
        for group in result:
            object_group_name = group["Object-Group"].split(" ")[-1]
            writer.writerow([object_group_name, group["Type"] ,group["Description"], group["Number Object"] , group["Object"]])
