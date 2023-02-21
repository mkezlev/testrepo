# Python merg files
# merge.phy /

import os
import string

def mergefile(srcfolder,destfile):
  
 data = ""
 with open (destfile, 'w') as fp:
    fp.write(data)

 for count, filename in enumerate(os.listdir(srcfolder)):
   with open(filename) as fp:
       data += fp.read()
   data += "\n"

 with open (destfile, 'w') as fp:
    fp.write(data)