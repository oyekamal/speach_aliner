import pandas as pd
import json


df = pd.read_excel('image_cordinates.xlsx').to_dict()
clean_eye_json = {}
clean_mouth_json = {}


# print(df)

for each_eye_key, value in df['eye_name'].items():
    print(value)
    if value != 'nan':
        clean_eye_json[value] = {"eye_size": df['eye_size'][each_eye_key],"eye_location": df['eye_location'][each_eye_key] }



with open("eyes_cordinations.json", "w") as outfile:
    json.dump(clean_eye_json, outfile)  


for each_eye_key, value in df['imouth_name'].items():
    print(value)
    if value != 'nan':
        clean_mouth_json[value] = {"mouth_size": df['mouth_size'][each_eye_key],"mouth_location": df['mouth_location'][each_eye_key] }



with open("mouth_cordinations.json", "w") as outfile:
    json.dump(clean_mouth_json, outfile)  