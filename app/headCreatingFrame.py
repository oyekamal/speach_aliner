from PIL import Image
import numpy as np
import statistics


from code.editImage.addingImages import adding_image



def adding_eyes_and_mouth(face_path, eye_path, mouth_path):
    face = Image.open(face_path)

    eye = Image.open(eye_path)

    mouth = Image.open(mouth_path)

    im  = np.array(face.convert('RGB'))

    # Define the blue colour we want to find - PIL uses RGB ordering
    blue = [253,250,230]

    # Get X and Y coordinates of all blue pixels
    Y, X = np.where(np.all(im==blue,axis=2))
    x, y=statistics.mean(X),statistics.mean(Y)

    new_image = adding_image(face, eye, location=(x,y))
    new_image = adding_image(new_image, mouth, location=(111,322), mirror=True)
    new_image.show()
    new_image.save('new_G.png')
    return new_image




# #  #how to use this function:
face = "./images/head/character_1.png"

eye = "./images/side_eyes/content side main M.png"

mouth = "./images/mouth/character_1/mouth_happy/th_h.png"

new = adding_eyes_and_mouth(face, eye, mouth)