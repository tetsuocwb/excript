import sys
try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")
print(droppedFile)

import tkFileDialog
f = tkFileDialog.askopenfilename()
# Go on from there; f is a handle to the file that the user picked