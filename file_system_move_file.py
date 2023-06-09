
import os

source = 'C:\Users\srishti\Downloads\Unconfirmed 972735.crdownload'

dest = 'newfile.txt'

os.rename(source, dest)
print("Source path renamed to destination path successfully.")