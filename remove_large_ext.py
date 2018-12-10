#Remove _large from extension of all files in current dir
import os,sys
folder = '.'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): 
           continue
       old_base = os.path.splitext(filename)
       new_name = infilename.replace('_large', '')
       output = os.rename(infilename, newname)
