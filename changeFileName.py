import os
#os is python's standard library, you don't need to download.
#I recommend you to copy working directory, in case you accidentally mess up your data.

#set variable with your working directory
path = 'C:/path/of/your/working/directory'

#get file names in list
files = os.listdir(path)
#ex) print(files) = [file1.txt, file2.csv, file3.pdf]

#if you want to number your files, you can use enumerate.
#enumerate => give two variables, which are index, and file name. you can name them as you want.
#for file in enumerate(files):
#  print(file)

#result
# 0 file1.txt
# 1 file2.csv
# 2 file3.pdf

#add prefix to all the name
for file in files:
  os.rename(os.path.join(path,file), os.path.join(path,'prefix'+file))




