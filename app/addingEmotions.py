import json
path = './json/json_data_for_frame/jamal_phonemes.json'

frame_data = open(path)

frames_json = json.load(frame_data)

for each_fagment in frames_json['fragments']:
    if 'emotion' in each_fagment:
        del each_fagment['emotion']

f = open("jamal.txt", "r")
text = ""
for each_word in f:
    text = text + " " +each_word
text = text.strip()
text = text.replace("\n", "")
text = text.replace("  ", " ")
if len(text.strip().split(' ')) != len(frames_json['fragments']):
    print("Error")
    print("word number doesn't match with frame number")
else:
    print("word number match with frame number")
    print("length of text: ", len(text.strip().split(' ')))
    print("length of frames: ", len(frames_json['fragments']))
length_of_text = len(frames_json['fragments'])

counter = length_of_text

while text != "":
    print(text)
    user_input = input("Enter the name of the file: ")
    length = len(user_input)
    user_input_list = user_input.split(" ")
    print("type of Emotion: ?")
    print("happy, sad, angry, bore, content, glare, sarcasm, worried")
    emotion = input("Enter from above emotions: ")

    for each_word in user_input_list:
        if frames_json['fragments'][length_of_text - counter ]['lines'][0] == each_word:
            if 'emtion' not in each_fagment:
                frames_json['fragments'][length_of_text - counter]['emotion'] = emotion
                counter -= 1


    text = text[length:].strip()

with open('./json/json_data_for_frame/emotions_jamal_phonemes.json', "w") as outfile:
    json.dump(frames_json, outfile)