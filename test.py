import re
import csv

# Votre texte avec les interfaces
config_text = """
interface GigabitEthernet1/4
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet1/5
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet1/6
 description Secbox
 duplex full
 nameif secbox
 security-level 50
 ip address 10.254.1.2 255.255.255.252 
!
interface GigabitEthernet1/7
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet1/8
 description Acces DTI via Innovation
 nameif innov
 security-level 0
 ip address 10.196.32.5 255.255.252.0 
!
"""

# Utilisez une expression régulière pour diviser le texte en blocs d'interface
interface_blocks = re.split(r'!\s*interface\s+', config_text.strip())



def test():
    # Créez un fichier CSV pour écrire les données
    with open('i.csv', 'w', newline='') as csvfile:
        fieldnames = ['Interface', 'Contenu']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Parcourez chaque bloc d'interface
        for interface_block in interface_blocks[1:]:
            lines = interface_block.strip().split('\n')
            interface_name = lines[0].strip()
            interface_content = '\n'.join(lines[1:]).strip()
            writer.writerow({'Interface': interface_name, 'Contenu': interface_content})

    print("Les données ont été extraites et enregistrées dans 'interfaces.csv'.")
