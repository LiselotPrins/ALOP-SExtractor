import numpy as np
import matplotlib as plt

path = "C:\\Users\Lisel\ALOP\SExtractor\Experiment\cat_test.cat" #insert path to catalog
data = np.genfromtxt(path, usecols=(1,2,3,4),skip_header=5)
numberStars = len(data)
colors = ["red", "green", "blue", "pink"] #first color for extension 1

with open("table.reg", "w") as f:
    f.write("# Region file format: DS9 version 4.1\n")
    f.write(f"global color=green dashlist=8 3 width=1 font=\"helvetica 10 normal roman\" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n")
    f.write("physical\n") # or 'image'?
    for i in range(numberStars):  
        color=colors[int(data[i][0]-1)]
        f.write(f"circle({data[i][1]},{data[i][2]},{data[i][3]}) # color={color}\n")