import csv
import os

wordresearch = 'access-group'
Folder = "CSV"

def access_group_list_to_csv(output_file , data):
    useless_info = [0,3]
    result = []
    Path = os.path.join(Folder, output_file)
    for line in data:
        if line.strip().startswith(wordresearch):
            columns = line.strip(" ").split()
            columns = [columns[i] for i in range(len(columns)) if i not in useless_info]
            result.append(columns)
    headers = ['Situation', 'Type' , 'Interface']
    print('Access Group list catch !')
    with open(Path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(headers)
        writer.writerows(result)
    



