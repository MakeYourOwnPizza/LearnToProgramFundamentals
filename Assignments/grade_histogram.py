import tkinter.filedialog
import grade

a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename,'r')
'''I checked that all lines read properly
for line in a1_file:
    print (line)
'''

a1_histfilename = tkinter.filedialog.askopenfilename()
a1_histfile = open(a1_histfilename,'r')

# Read the grades into a list.

# Count the grades per range.

# Write the histogram to the file.
'''
0-9:   *
10-10: **
20-29: *****
  :
90-00: **
100:   *
'''
