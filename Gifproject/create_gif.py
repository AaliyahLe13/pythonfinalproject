import imageio.v3 as iio

filenames = ["cat-image1.png", "cat-image2.png", "cat-image3.png"]
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("catkeyboard.gif", images, duration = 100, loop = 0)