import os
from PIL import Image

path = "C:\\input\\Chapter 00"
destpath = "C:\\output"

for infile in os.listdir(path):
    outfile = destpath + os.path.splitext(infile)[0] + ".pdf"
    current = path + infile

    if infile != outfile:
        im = Image.open(current)
        dpi = im.info['dpi']

        im.save(outfile, "PDF", resolution=100.0)