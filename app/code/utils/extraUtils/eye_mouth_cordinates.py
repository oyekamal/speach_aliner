import pandas as pd
import json


df = pd.read_excel('image_cordinates.xlsx').to_dict()
clean_eye_json = {}
clean_mouth_json = {}


# print(df)

for each_eye_key, value in df['eye_name'].items():
    print(value)
    if value != 'nan':
        try:
            clean_eye_json[value] = {"eye_size": [int(i) for i in df['eye_size'][each_eye_key].split(",")],"eye_location": [int(i) for i in  df['eye_location'][each_eye_key].split(",")] }
        except:
            pass


with open("eyes_cordinations.json", "w") as outfile:
    json.dump(clean_eye_json, outfile)  


for each_eye_key, value in df['imouth_name'].items():
    print(value)
    if value != 'nan':
        clean_mouth_json[value] = {"mouth_size": [int(i) for i in  df['mouth_size'][each_eye_key].split(",")],"mouth_location": [int(i) for i in  df['mouth_location'][each_eye_key].split(",")] }



with open("mouth_cordinations.json", "w") as outfile:
    json.dump(clean_mouth_json, outfile)  