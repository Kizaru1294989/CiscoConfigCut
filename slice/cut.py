import json
from read.read import read
from slice.Firewall.Firewall_list.access_list_to_csv import access_list_to_csv
from slice.Object.object_group_list.object_group_to_csv import object_group_to_csv
from slice.Firewall.access_group_list.access_group_list import access_group_list_to_csv
from slice.Network.interface_list.interface_list_to_csv import interface_list_to_csv
from slice.Network.object_network_list.object_network_list_to_csv import object_network_list_to_csv
from slice.Network.object_service_list.object_service_list_to_csv import object_service_list_to_csv

sourcefilepath = 'SourceFile/CloudFW.confg'
file = read(sourcefilepath)

def cut():
    object_service_list_to_csv('Object_Service_list.csv',file)
    object_network_list_to_csv('Object_Network_list.csv',file)
    access_list_to_csv('Firewall_ACL_list.csv',file)
    object_group_to_csv('Group_Object_list.csv',file)
    access_group_list_to_csv('Access_Group_list.csv',file)
    interface_list_to_csv('Interface_list.csv',file)