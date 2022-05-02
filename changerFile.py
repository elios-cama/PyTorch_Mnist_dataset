import os,sys
folder = r'C:\Users\elios\STAGE_DAYMODE\dataset_poke\dataset\dracaufeu'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.jfif', '.jpg')
       output = os.rename(infilename, newname)