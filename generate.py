from ppf.datamatrix import DataMatrix
import os
from helpers import get_filepaths_by_extension, convert_svgs_to_pngs

print("Clear images folder")

filelist = [ f for f in os.listdir("./images")]
for f in filelist:
    os.remove(os.path.join("./images", f))

filename = "./texts.txt"

lines = None

print("Read texts.txt")

with open(filename) as file:
    lines = [line.rstrip() for line in file]

matrices = dict()

print("Generate DataMatrix")

for line in lines:
    matrices[line] = DataMatrix(line)

print("Write SVG")

for key in matrices.keys():
    f = open(f"./images/{key.replace("/","_")}.svg", "x")
    f.write(matrices[key].svg())
    f.close()

print("Convert SVG to PNG")
svgpaths = get_filepaths_by_extension("./images", 'svg')
pngpaths = convert_svgs_to_pngs(svgpaths)

print("Remove SVG from images folder")
filelist = [ f for f in os.listdir("./images") if f.endswith(".svg")]
for f in filelist:
    os.remove(os.path.join("./images", f))