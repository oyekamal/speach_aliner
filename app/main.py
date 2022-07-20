
print("Main....!")


import json
from headCreatingFrame import adding_eyes_and_mouth
from code.utils.utils import path_creation_for_mouth
  
f = open('phonemes_json.json')
frame_data = open('jamal_phonemes.json')

phonemes = json.load(f)
frames_json = json.load(frame_data)



face = "./images/head/character_1.png"

eye = "./images/side_eyes/content side main M.png"

mouth = "./images/mouth/character_1/happy/th_h.png"

# adding_eyes_and_mouth(face, eye, mouth, "test")

emotion = "happy"


for each_fagment in frames_json['fragments']:
    for each_phoneme in each_fagment['phonemes']:
        if phonemes.get(each_phoneme):
            print(each_phoneme)
            phonem_dic = phonemes.get(each_phoneme)
            mouth_path = path_creation_for_mouth(1, emotion)
            mouth_path = mouth_path + phonem_dic[emotion]
            name_file = each_fagment["id"] + "_" + each_phoneme
            adding_eyes_and_mouth(face, eye, mouth_path, name_file)
        else:
            print("---"*20)