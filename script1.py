"""
file_lines= open ('myfile.txt').readlines()


for line in open ('myfile.txt').readlines():
    line= line.rstrip()
    print line


for line in file_lines:
    line= line.rstrip()
    print line
    
    
    
    for line in open ('myfile.txt'):
    line= line.rstrip()
    print line
"""


file_lines = []

for line in open ('myfile.txt'):
    line= line.rstrip()
    file_lines.append(line)
    
    
file_lines= [line.rstrip() for line in open('myfile.txt')]



 
  


















