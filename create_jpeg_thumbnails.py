import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    print("infile:", infile)
    outfile = os.path.splitext(infile)[0] + ".thumbnail.jpeg"
    print("outfile:", outfile)
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
