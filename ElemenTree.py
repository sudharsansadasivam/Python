import xml.etree.ElementTree as ET
import csv
s_no=1
f=open('xmlDataExtract.csv','w')
my=csv.writer(f,delimiter=' ',lineterminator='\n')
head=['s.no','Attribute Name','Visible Name']
my.writerow(head)
root = ET.parse('xmlFilePath').getroot()
for type_tag in root.findall('typedef/attribute'):
    print(type_tag)
    attributeValue = type_tag.get('name')
    visbileValue = type_tag.get('visible')
    if visbileValue == None:
        visbileValue = 'true'
    print(attributeValue , visbileValue)
    my.writerow([s_no,attributeValue,visbileValue])
    s_no+=1
    
f.close()
