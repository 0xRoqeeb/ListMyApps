from encodings import utf_8
import subprocess
import sys

file = open('output.txt', 'a')
sys.stdout = file


Data = subprocess.check_output(['wmic','product','get','name'])
a =str(Data)



try:
    
    
      for i in range(len(a)):
                print(a.split("\\r\\r\\n")[6:][i])
                                        
except IndexError as e:
     print  ("This Was Everything I could find")  
     
     
file.close