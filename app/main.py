
print("Main....!")


import json
from headCreatingFrame import adding_eyes_and_mouth
from code.utils.utils import path_creation_for_mouth, path_creation_for_eyes
import random
  
f = open('./json/phonemes_json.json')
frame_data = open('./json/json_data_for_frame/jamal_phonemes.json')

phonemes = json.load(f)
frames_json = json.load(frame_data)



face = "./images/head/character_1.png"

# eye = path_creation_for_eyes(1, "blinking", "happy", False, "L")

# print(eye)

# mouth = "./images/mouth/character_1/happy/th_h.png"

# adding_eyes_and_mouth(face, eye, mouth, "test")

emotion = "happy"


for each_fagment in frames_json['fragments']:
    for each_phoneme in each_fagment['phonemes']:
        if phonemes.get(each_phoneme):
            print(each_phoneme)
            phonem_dic = phonemes.get(each_phoneme)

            emotion_mouth_choice = random.choice(["happy","sad"])

            mouth_path = path_creation_for_mouth(1, emotion_mouth_choice)
            mouth_path = mouth_path + phonem_dic[emotion_mouth_choice]

            blinking_choice = random.choice(["blinking", "not_blinking"])
            intensity_choice = random.choice([True, False])
            eyes_position_choice = random.choice(["L", "R", "M"])
            eyes_emotion_choice = random.choice(["happy", "angry", "sad", "bore", "content", "glare",'sarcasm','worried'])

            eye = path_creation_for_eyes(1, blinking_choice, eyes_emotion_choice, intensity_choice, eyes_position_choice)
            name_file = each_fagment["id"] + "_" + each_phoneme
            adding_eyes_and_mouth(face, eye, mouth_path, name_file)
        else:
            print("---"*20)