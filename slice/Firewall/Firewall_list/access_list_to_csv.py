
import csv
import os
from slice.Firewall.Firewall_list.search_object.search_object import search_object
from slice.Firewall.Firewall_list.search_object.search_object_group import search_object_group

wordresearch = 'access-list'
Folder = "CSV"

def access_list_to_csv(output_file, data):
    print('Access list catch !')
    Path = os.path.join(Folder, output_file)
    result = []
    
    current_acl_list = None
    current_list_access = None
    current_list_source_port = None
    current_list_source_ip = None
    current_list_destination_port = None
    current_list_destination_ip = None
    

    for line in data:
        line = line.strip()
        if line.startswith(wordresearch):
       
            if current_acl_list is not None:
                result.append({
                                "List Name": current_acl_list,
                                "Access": current_list_access,
                                "Port Source" :  current_list_source_port,
                                "IP Source": current_list_source_ip,
                                "Port Destination": current_list_destination_port,
                                "IP Destination": current_list_destination_ip,  
                               })
                      
            #print(line)
            current_acl_list = line.split()[1]
            current_list_access = line.split()[3]
            

            
            if  line.split()[4] == "object" :
                
                
                service = search_object('Object_Service_list.csv',line.split()[5])
                network = search_object('Object_Network_list.csv',line.split()[5])
                if service:
                    current_list_source_port = "obj " +line.split()[5]
                    current_list_source_ip = line.split()[6]
                if network:
                    #print(current_acl_list)
                    current_list_source_port = "NO"
                    current_list_source_ip = "obj " + line.split()[5]
                    
                if line.split()[6] == "object-group":
                        #print(line.split()[8])
                        group = search_object_group('Group_Object_list.csv',line.split()[7])
                        if group == 'service' : 
                            current_list_source_port ="grp-obj " + line.split()[7]

                        if group == 'network' : 
                            current_list_destination_port = "NO"
                            current_list_source_ip = "grp-obj " + line.split()[7]
                        
                        
                        if line.split()[8] == "object-group":
                        #print(line.split()[8])
                            group1 = search_object_group('Group_Object_list.csv',line.split()[9])
                            if group1 == 'service' : 
                                current_list_destination_port ="grp-obj " + line.split()[9]
                                #current_list_destination_ip = "NO"
                            if group1 == 'network' : 
                                #current_list_destination_port = "NO"
                                current_list_destination_ip = "grp-obj " + line.split()[9]

                                
                                
                if line.split()[6] == "object":
                            service = search_object('Object_Service_list.csv',line.split()[7])
                            network = search_object('Object_Network_list.csv',line.split()[7])
                            if service:
                                current_list_source_port = "obj " +line.split()[7]
                            if network:
                                current_list_source_ip = "obj " + line.split()[7]
                            if line.split()[8] == "object":
                        #print(line.split()[8])
                                service = search_object('Object_Service_list.csv',line.split()[9])
                                network = search_object('Object_Network_list.csv',line.split()[9])
                                if service:
                                    current_list_destination_port = "obj " +line.split()[9]
                                if network:
                                    current_list_destination_ip = "obj " + line.split()[9]
                                    
                            if line.split()[8] == "object-group":
                        #print(line.split()[8])
                                group1 = search_object_group('Group_Object_list.csv',line.split()[9])
                                if group1 == 'service' : 
                                    current_list_destination_port ="grp-obj " + line.split()[9]
                                    #current_list_destination_ip = "NO"
                                if group1 == 'network' : 
                                #current_list_destination_port = "NO"
                                    current_list_destination_ip = "grp-obj " + line.split()[9]

                        
                    
                if line.split()[7] == "object-group":
                        #print(line.split()[8])
                        group = search_object_group('Group_Object_list.csv',line.split()[8])
                        if group == 'service' : 
                            current_list_destination_port ="grp-obj " + line.split()[8]
                            current_list_destination_ip = "NO"
                        if group == 'network' : 
                            current_list_destination_port = "NO"
                            current_list_destination_ip = "grp-obj " + line.split()[8]
                            
                if line.split()[7] == "object":
                        #print(line.split()[8])
                    service = search_object('Object_Service_list.csv',line.split()[8])
                    network = search_object('Object_Network_list.csv',line.split()[8])
                    if service:
                        current_list_destination_port = "obj " +line.split()[8]
                    if network:
                        current_list_destination_ip = "obj " + line.split()[8]
                    
            
            
  
            elif line.split()[4] == "object-group" :
                #print(line.split()[5])
                group = search_object_group('Group_Object_list.csv',line.split()[5])
                if group == 'service' : 
                    current_list_source_port ="grp-obj " + line.split()[5]
                    current_list_source_ip = line.split()[6]
                if group == 'network' : 
                    current_list_source_port = "NO"
                    current_list_source_ip = "grp-obj " + line.split()[5]
                if line.split()[6] == "object-group":
                        #print(line.split()[8])
                        group = search_object_group('Group_Object_list.csv',line.split()[7])
                        if group == 'service' : 
                            current_list_source_port ="grp-obj " + line.split()[7]
                            #current_list_source_ip = "NO"
                        if group == 'network' : 
                            #current_list_source_port = "NO"
                            current_list_source_ip = "grp-obj " + line.split()[7]
                if line.split()[7] == "object-group":
                        #print(line.split()[8])
                        group = search_object_group('Group_Object_list.csv',line.split()[8])
                        if group == 'service' : 
                            current_list_destination_port ="grp-obj " + line.split()[8]
                            current_list_destination_ip = "NO"
                        if group == 'network' : 
                            current_list_destination_port = "NO"
                            current_list_destination_ip = "grp-obj " + line.split()[8]
                    
                    
                    
            elif line.split()[4] != "object" and line.split()[4] != "object-group" :
                if line.split()[5] == "object-group": #dns case
                    
                        group = search_object_group('Group_Object_list.csv',line.split()[6])
                        if group == 'service' : 
                            current_list_source_port ="grp-obj " + line.split()[6]
                            current_list_source_ip = line.split()[4]
                        if group == 'network' : 
                            current_list_source_port = line.split()[4]
                            current_list_source_ip = "grp-obj " + line.split()[6]
                        
                        if line.split()[7] == "object-group":
                            obj_grp_case = line.split()[8]
                            group_dest = search_object_group('Group_Object_list.csv',obj_grp_case)
                        if group_dest == 'service' : 
                            current_list_destination_port ="grp-obj " + obj_grp_case
                            current_list_destination_ip = "NO"
                        if group_dest == 'network' : 
                            current_list_destination_port = "NO"
                            current_list_destination_ip = "grp-obj " + obj_grp_case
                else:
                    # "ip" case
                    #print(line.split()[4])
                    current_list_source_port = line.split()[4]
                    current_list_source_ip = line.split()[5]
                    
                    port = line.split()[7:]
                    port_dest = ' '.join(port)
                    ip = line.split()[6]
                    #print(port)
                    
                    #udp
                    if port_dest != "":
                        current_list_destination_port = port_dest
                        current_list_destination_ip = ip
                        #ip
                    elif port_dest == "":
                       
                        current_list_destination_port = line.split()[5]
                        current_list_destination_ip = ip
                        


    
    if current_acl_list is not None:
                result.append({
                                "List Name": current_acl_list,
                                "Access": current_list_access,
                                "Port Source" :  current_list_source_port,
                                "IP Source": current_list_source_ip,
                                "Port Destination": current_list_destination_port,
                                "IP Destination": current_list_destination_ip,  
                               })

    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["List Name", "Access" , "Port Source", "IP Source" , "Port Destination" , "IP Destination"])

        for group in result:
            object_group_name = group["List Name"].split(" ")[-1]
            writer.writerow([object_group_name, group["Access"],  group["Port Source"], group["IP Source"] , group["Port Destination"] , group["IP Destination"]])
