from PIL import Image
import time
import PIL 

# Threshold Image 

print("...creating threshold image")
# threshold adjustment
img = Image.open("shuff.jpg")
width,height = img.size
pixels = img.load()

maxDepth = 256
threshold = .97
thresholdCutoff = maxDepth * 3 * threshold

width,height = img.size
black = (0,0,0)
white = (256,256,256)
pixels = img.load()

redScale = 1.00
greenScale = 1.00
blueScale = 1.00

for i in range(width):
    for j in range(height):
        total = sum(pixels[i,j])
        if total < thresholdCutoff:
            pixels[i,j] = black
        else:
            pixels[i,j] = white

img.show()
img.save('threshold.jpg')

