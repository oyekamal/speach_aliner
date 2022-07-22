from PIL import Image
import numpy as np
import json

from code.editImage.addingImages import adding_image



eyes_cordinations = open('./json/character_cordinates/character_1_eyes_cordinations.json')
mouth_cordinations = open('./json/character_cordinates/character_1_mouth_cordinations.json')

eyes_cordinations = json.load(eyes_cordinations)
mouth_cordinations = json.load(mouth_cordinations)


def adding_eyes_and_mouth(face_path, eye_path, mouth_path, frame_name):
    face = Image.open(face_path)

    eye = Image.open(eye_path)

    mouth = Image.open(mouth_path)

    eye_phenome = eye_path.split('/')[-2]

    print(eye_phenome)

    mouth_phenome = mouth_path.split('/')[-1].split('.')[0]


    new_image = adding_image(face, eye, 
                            location=eyes_cordinations[eye_phenome]['eye_location'], 
                            rotation=0, 
                            mirror=False, 
                            size_cordinates=eyes_cordinations[eye_phenome]['eye_size'])


    new_image = adding_image(new_image, mouth, 
                            location=mouth_cordinations[mouth_phenome]['mouth_location'], 
                            mirror=True,
                            size_cordinates=mouth_cordinations[mouth_phenome]['mouth_size'])
    # new_image.show()
    new_image.save(f'./frames/headFrames/{frame_name}.png')
    # return new_image




# #  #how to use this function:
# face = "./images/head/character_1.png"

# eye = "./images/side_eyes/content side main M.png"

# mouth = "./images/mouth/character_1/mouth_happy/th_h.png"

# new = adding_eyes_and_mouth(face, eye, mouth)