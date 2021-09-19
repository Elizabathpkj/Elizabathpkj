import xml.etree.ElementTree as Xet

import csv

xmlparse = Xet.parse('testfile.xml')
root = xmlparse.getroot()
filename=[]
data=[]
for i in root[1][0]:
    p = i.find("CSVIntervalData").text
    data=p.split()
    break
for i in data:
        line=i.split(',')
        if line[0]=='200':
            filename.append(line[1])

for name in filename:
          with open(name+'.csv', 'w') as f:
            write = csv.writer(f)
             
            for i in data:
                line=i.split(',')
                
                    
                if line[0]=='100':
                    write.writerow(line)
                


                   
                if line[0] != '100':
                      write.writerow(line)
