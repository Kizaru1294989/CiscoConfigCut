import csv
import os

wordresearch = 'access-list'
Folder = "CSV"

def access_list_to_csv(output_file , data):
    useless_info = [0, 1, 2]
    result = []
    Path = os.path.join(Folder, output_file)
    for line in data:
        if line.strip().startswith(wordresearch):
            columns = line.strip(" ").split()
            columns = [columns[i] for i in range(len(columns)) if i not in useless_info]
            result.append(columns)
    headers = ['Autorisation', 'Obj' , 'Protocol-Source' , 'Protocol-Destination' , 'IP-Source' , 'IP-Destination' , 'Optionnal']
    print('FireWall ACL list catch !')
    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(headers)
        writer.writerows(result)
    



