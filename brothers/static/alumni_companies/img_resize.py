import os, sys
from PIL import Image

size = 10000, 75

for subdir, dirs, files in os.walk(os.getcwd()):
	for infile in files:
		outfile = os.path.splitext(infile)[0] + "_thumb.png"
		try:
			im = Image.open(infile)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(outfile, "PNG")
			print("<img src=\"../img/alumni_companies/" + outfile + "\" />")
			# print('"' + outfile + '",')
		except IOError:
			pass
			# print("cannot create thumbnail for '%s'", infile)