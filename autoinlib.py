import os 
import sys 
with open ('requirements.txt',"r",encoding='utf-8') as requirements:
    text = requirements.read().split()
    for library in text: 
        lib = library.replace('\n','')
        os.system(f'pip3 install {lib}')
  
    print('All done')
    exit_ = input()



