from PIL import Image
import numpy as np

from code.editImage.addingImages import adding_image

#  #how to use this function:
face = Image.open(r"new face1.png")

eye = Image.open(r"sad.png")

im  = np.array(face.convert('RGB'))

# Define the blue colour we want to find - PIL uses RGB ordering
blue = [253,250,230]

# Get X and Y coordinates of all blue pixels
Y, X = np.where(np.all(im==blue,axis=2))
x, y=statistics.mean(X),statistics.mean(Y)

new_image = adding_image(face, eye, location=(x,y), rotation=3)
new_image.show()
new_image.save('new_G.png')